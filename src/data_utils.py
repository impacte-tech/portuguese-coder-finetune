#!/usr/bin/env python3
"""
Data processing utilities.
"""

import json
from typing import List, Dict
from datasets import Dataset


def load_jsonl(filepath: str) -> List[Dict]:
    """Load JSONL file."""
    data = []
    with open(filepath, 'r', encoding='utf-8') as f:
        for line in f:
            data.append(json.loads(line.strip()))
    return data


def save_jsonl(data: List[Dict], filepath: str):
    """Save data to JSONL file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(json.dumps(item, ensure_ascii=False) + '\n')


def format_alpaca_prompt(instruction: str, input_text: str, output: str) -> str:
    """Format example in Alpaca prompt style."""
    if input_text and input_text.strip():
        return f"### Instrução:\n{instruction}\n\n### Entrada:\n{input_text}\n\n### Resposta:\n{output}"
    else:
        return f"### Instrução:\n{instruction}\n\n### Resposta:\n{output}"


def format_chatml_prompt(messages: List[Dict]) -> str:
    """Format messages in ChatML format."""
    prompt = ""
    for msg in messages:
        role = msg.get("role", "user")
        content = msg.get("content", "")
        prompt += f"<|im_start|>{role}\n{content}<|im_end|>\n"
    prompt += "<|im_start|>assistant\n"
    return prompt


def validate_dataset(data: List[Dict]) -> Dict:
    """Validate dataset format and return statistics."""
    stats = {
        "total_examples": len(data),
        "with_input": 0,
        "without_input": 0,
        "avg_instruction_length": 0,
        "avg_output_length": 0,
        "languages_detected": set(),
    }
    
    total_instr_len = 0
    total_output_len = 0
    
    for item in data:
        # Check required fields
        if "instruction" not in item or "output" not in item:
            raise ValueError(f"Missing required fields in example: {item}")
        
        # Count with/without input
        if item.get("input"):
            stats["with_input"] += 1
        else:
            stats["without_input"] += 1
        
        # Calculate lengths
        total_instr_len += len(item["instruction"])
        total_output_len += len(item["output"])
    
    if data:
        stats["avg_instruction_length"] = total_instr_len / len(data)
        stats["avg_output_length"] = total_output_len / len(data)
    
    return stats


def split_dataset(data: List[Dict], train_ratio: float = 0.8, val_ratio: float = 0.1):
    """Split dataset into train/val/test."""
    import random
    random.seed(42)
    
    shuffled = data.copy()
    random.shuffle(shuffled)
    
    n = len(shuffled)
    train_end = int(n * train_ratio)
    val_end = train_end + int(n * val_ratio)
    
    return {
        "train": shuffled[:train_end],
        "validation": shuffled[train_end:val_end],
        "test": shuffled[val_end:],
    }


def merge_datasets(filepaths: List[str], output_path: str):
    """Merge multiple JSONL files into one."""
    all_data = []
    for filepath in filepaths:
        all_data.extend(load_jsonl(filepath))
    
    save_jsonl(all_data, output_path)
    print(f"✅ Merged {len(filepaths)} files into {output_path}")
    print(f"   Total examples: {len(all_data)}")


def preview_dataset(filepath: str, n: int = 3):
    """Preview first n examples from dataset."""
    data = load_jsonl(filepath)
    
    print(f"📊 Dataset: {filepath}")
    print(f"   Total examples: {len(data)}")
    print(f"\n📝 First {n} examples:\n")
    
    for i, item in enumerate(data[:n], 1):
        print(f"--- Example {i} ---")
        print(f"Instruction: {item.get('instruction', 'N/A')[:100]}...")
        print(f"Input: {item.get('input', 'N/A')[:100]}...")
        print(f"Output: {item.get('output', 'N/A')[:100]}...")
        print()


if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        preview_dataset(sys.argv[1])
    else:
        print("Usage: python data_utils.py <path_to_jsonl>")
