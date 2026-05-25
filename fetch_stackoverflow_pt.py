#!/usr/bin/env python3
"""
Fetch Portuguese Python Q&A from Stack Overflow (PT).
Filters by upvotes, excludes already fetched questions.
"""

import requests
import json
import time
import os
from datetime import datetime
from pathlib import Path
from typing import List, Dict, Set, Optional


class StackOverflowPTCollector:
    """Collect high-quality Portuguese Python Q&A from Stack Overflow PT."""
    
    API_BASE = "https://api.stackexchange.com/2.3"
    
    def __init__(
        self,
        min_upvotes: int = 5,
        min_answers: int = 1,
        has_accepted_answer: bool = True,
        output_file: str = "data/stackoverflow_pt_python.jsonl",
        state_file: str = "data/.stackoverflow_state.json"
    ):
        self.min_upvotes = min_upvotes
        self.min_answers = min_answers
        self.has_accepted_answer = has_accepted_answer
        self.output_file = Path(output_file)
        self.state_file = Path(state_file)
        
        # Track fetched question IDs to avoid duplicates
        self.fetched_ids: Set[int] = self._load_state()
        
        # Ensure output directory exists
        self.output_file.parent.mkdir(exist_ok=True)
        
    def _load_state(self) -> Set[int]:
        """Load previously fetched question IDs."""
        if self.state_file.exists():
            with open(self.state_file, 'r') as f:
                state = json.load(f)
                return set(state.get('fetched_ids', []))
        return set()
    
    def _save_state(self):
        """Save fetched question IDs."""
        state = {
            'fetched_ids': list(self.fetched_ids),
            'last_updated': datetime.now().isoformat(),
            'total_fetched': len(self.fetched_ids)
        }
        with open(self.state_file, 'w') as f:
            json.dump(state, f, indent=2)
    
    def _make_request(self, endpoint: str, params: Dict) -> Optional[Dict]:
        """Make API request with rate limiting."""
        url = f"{self.API_BASE}/{endpoint}"
        
        try:
            response = requests.get(url, params=params, timeout=30)
            
            if response.status_code == 429:
                print("Rate limited! Waiting 60 seconds...")
                time.sleep(60)
                return self._make_request(endpoint, params)
            
            response.raise_for_status()
            return response.json()
            
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            return None
    
    def search_questions(
        self,
        tag: str = "python",
        sort: str = "votes",
        order: str = "desc",
        pagesize: int = 100,
        page: int = 1
    ) -> List[Dict]:
        """Search for questions with quality filters."""
        
        params = {
            "order": order,
            "sort": sort,
            "tagged": tag,
            "site": "pt.stackoverflow",
            "pagesize": pagesize,
            "page": page,
            "filter": "withbody",  # Include question body
            "min": self.min_upvotes,  # Minimum score
        }
        
        print(f"Fetching page {page} (tag: {tag}, min_upvotes: {self.min_upvotes})...")
        
        data = self._make_request("questions", params)
        if not data:
            return []
        
        questions = data.get('items', [])
        
        # Filter out already fetched and apply quality criteria
        new_questions = []
        for q in questions:
            q_id = q['question_id']
            
            # Skip if already fetched
            if q_id in self.fetched_ids:
                continue
            
            # Apply filters
            if q['score'] < self.min_upvotes:
                continue
            if q['answer_count'] < self.min_answers:
                continue
            if self.has_accepted_answer and not q.get('accepted_answer_id'):
                continue
                
            new_questions.append(q)
        
        print(f"Found {len(new_questions)} new questions (filtered {len(questions) - len(new_questions)})")
        return new_questions
    
    def get_answers(self, question_id: int) -> List[Dict]:
        """Fetch answers for a specific question."""
        
        params = {
            "order": "desc",
            "sort": "votes",
            "site": "pt.stackoverflow",
            "filter": "withbody",
            "pagesize": 5  # Top 5 answers max
        }
        
        data = self._make_request(f"questions/{question_id}/answers", params)
        if not data:
            return []
        
        return data.get('items', [])
    
    def process_qa_pair(self, question: Dict, answers: List[Dict]) -> Optional[Dict]:
        """Process Q&A into training format."""
        
        if not answers:
            return None
        
        # Get best answer (highest voted)
        best_answer = answers[0]
        
        # Clean HTML from bodies (basic cleaning)
        q_body = self._clean_html(question.get('body', ''))
        a_body = self._clean_html(best_answer.get('body', ''))
        
        # Skip if no code in answer
        if '```' not in a_body and 'def ' not in a_body and 'class ' not in a_body:
            return None
        
        # Format for training
        formatted = {
            "text": f"<|im_start|>user\n{question['title']}\n\n{q_body}\n<|im_start|>assistant\n{a_body}",
            "metadata": {
                "question_id": question['question_id'],
                "question_score": question['score'],
                "answer_score": best_answer['score'],
                "tags": question.get('tags', []),
                "url": question.get('link', ''),
                "fetched_at": datetime.now().isoformat()
            }
        }
        
        return formatted
    
    def _clean_html(self, html: str) -> str:
        """Basic HTML cleaning."""
        import re
        
        # Remove HTML tags
        text = re.sub(r'<[^>]+>', '', html)
        
        # Decode HTML entities
        text = text.replace('&lt;', '<').replace('&gt;', '>')
        text = text.replace('&amp;', '&').replace('&quot;', '"')
        text = text.replace('&#39;', "'").replace('&nbsp;', ' ')
        
        # Clean up whitespace
        text = '\n'.join(line.strip() for line in text.split('\n'))
        text = re.sub(r'\n{3,}', '\n\n', text)
        
        return text.strip()
    
    def fetch_batch(self, target_count: int = 100) -> int:
        """Fetch a batch of questions up to target count."""
        
        fetched_this_batch = 0
        page = 1
        max_pages = 10  # Safety limit
        
        print(f"🚀 Starting batch fetch (target: {target_count}, already have: {len(self.fetched_ids)})")
        
        while fetched_this_batch < target_count and page <= max_pages:
            questions = self.search_questions(page=page)
            
            if not questions:
                print("No more questions found.")
                break
            
            for question in questions:
                if fetched_this_batch >= target_count:
                    break
                
                q_id = question['question_id']
                
                # Fetch answers
                answers = self.get_answers(q_id)
                
                # Process Q&A
                qa_pair = self.process_qa_pair(question, answers)
                
                if qa_pair:
                    # Append to file
                    with open(self.output_file, 'a', encoding='utf-8') as f:
                        f.write(json.dumps(qa_pair, ensure_ascii=False) + '\n')
                    
                    fetched_this_batch += 1
                    print(f"  ✓ Saved Q&A {fetched_this_batch}/{target_count} (Score: {question['score']})")
                
                # Mark as fetched
                self.fetched_ids.add(q_id)
                
                # Rate limiting
                time.sleep(0.5)
            
            page += 1
            time.sleep(1)  # Be nice to the API
        
        # Save state
        self._save_state()
        
        print(f"\n✅ Batch complete! Fetched {fetched_this_batch} new Q&A pairs")
        print(f"📊 Total unique questions in dataset: {len(self.fetched_ids)}")
        
        return fetched_this_batch
    
    def get_stats(self) -> Dict:
        """Get collection statistics."""
        stats = {
            'total_fetched': len(self.fetched_ids),
            'output_file_exists': self.output_file.exists(),
            'output_file_size_mb': 0
        }
        
        if self.output_file.exists():
            stats['output_file_size_mb'] = round(
                self.output_file.stat().st_size / (1024 * 1024), 2
            )
            
            # Count lines
            with open(self.output_file, 'r', encoding='utf-8') as f:
                stats['total_examples'] = sum(1 for _ in f)
        
        return stats


def main():
    """Main entry point."""
    import argparse
    
    parser = argparse.ArgumentParser(
        description="Fetch Portuguese Python Q&A from Stack Overflow PT"
    )
    parser.add_argument(
        '--count', '-n',
        type=int,
        default=100,
        help='Number of Q&A pairs to fetch (default: 100)'
    )
    parser.add_argument(
        '--min-upvotes', '-m',
        type=int,
        default=5,
        help='Minimum upvotes required (default: 5)'
    )
    parser.add_argument(
        '--output',
        default='data/stackoverflow_pt_python.jsonl',
        help='Output file path'
    )
    parser.add_argument(
        '--stats',
        action='store_true',
        help='Show statistics and exit'
    )
    
    args = parser.parse_args()
    
    collector = StackOverflowPTCollector(
        min_upvotes=args.min_upvotes,
        output_file=args.output
    )
    
    if args.stats:
        stats = collector.get_stats()
        print("📊 Collection Statistics:")
        for key, value in stats.items():
            print(f"  {key}: {value}")
        return
    
    # Fetch batch
    fetched = collector.fetch_batch(target_count=args.count)
    
    if fetched > 0:
        print(f"\n💾 Data saved to: {args.output}")
        print(f"📋 State saved to: {collector.state_file}")


if __name__ == "__main__":
    main()
