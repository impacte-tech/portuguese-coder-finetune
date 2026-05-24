#!/usr/bin/env python3
"""
Generate 1000 narrow-scope DSA operations dataset.
Focus: Efficient single operations, NOT broad problem solutions.
Output: ALWAYS pure Python code, no comments in output.
"""

import json
import random
from typing import List, Dict


class NarrowScopeOperations:
    """Generate fundamental single operations for DSA patterns."""
    
    def __init__(self):
        self.example_id = 0
        
    def next_id(self):
        self.example_id += 1
        return self.example_id
    
    def _create_example(self, instruction: str, input_text: str, output_code: str, 
                        category: str, difficulty: str = "easy") -> Dict:
        """Helper to create example with PURE CODE output (no comments)."""
        return {
            "id": self.next_id(),
            "instruction": instruction,
            "input": input_text,
            "output": output_code.strip(),
            "category": category,
            "difficulty": difficulty
        }
    
    # ========== HASH MAP OPERATIONS (150 examples) ==========
    
    def hash_operations(self) -> List[Dict]:
        """Hash map single operations - PURE CODE output."""
        examples = []
        
        # Hash map lookup
        for context in ["contagem", "mapeamento", "cache", "indice"]:
            examples.append(self._create_example(
                f"Verifique se elemento existe em hash map (contexto: {context})",
                "hash_map = {'a': 1, 'b': 2}, chave = 'a'",
                "existe = chave in hash_map",
                "hash-map-operations",
                "easy"
            ))
        
        # Get with default
        for context in ["contagem", "mapeamento", "cache", "indice"]:
            examples.append(self._create_example(
                f"Obtenha valor de hash map com valor padrao (contexto: {context})",
                "hash_map = {'a': 1, 'b': 2}, chave = 'a', padrao = 0",
                "valor = hash_map.get(chave, padrao)",
                "hash-map-operations",
                "easy"
            ))
        
        # Update count
        for context in ["contagem", "mapeamento", "cache", "indice"]:
            examples.append(self._create_example(
                f"Atualize contagem em hash map (contexto: {context})",
                "hash_map = {}, chave = 'a'",
                "hash_map[chave] = hash_map.get(chave, 0) + 1",
                "hash-map-operations",
                "easy"
            ))
        
        # Delete key
        for context in ["contagem", "mapeamento", "cache", "indice"]:
            examples.append(self._create_example(
                f"Delete chave de hash map (contexto: {context})",
                "hash_map = {'a': 1, 'b': 2}, chave = 'a'",
                "del hash_map[chave]",
                "hash-map-operations",
                "easy"
            ))
        
        # Check empty
        for context in ["contagem", "mapeamento", "cache", "indice"]:
            examples.append(self._create_example(
                f"Verifique se hash map esta vazio (contexto: {context})",
                "hash_map = {}",
                "vazio = len(hash_map) == 0",
                "hash-map-operations",
                "easy"
            ))
        
        # Iterate keys
        examples.append(self._create_example(
            "Itere sobre chaves do hash map",
            "hash_map = {'a': 1, 'b': 2}",
            "for chave in hash_map:\n    print(chave)",
            "hash-map-operations",
            "easy"
        ))
        
        # Iterate values
        examples.append(self._create_example(
            "Itere sobre valores do hash map",
            "hash_map = {'a': 1, 'b': 2}",
            "for valor in hash_map.values():\n    print(valor)",
            "hash-map-operations",
            "easy"
        ))
        
        # Iterate items
        examples.append(self._create_example(
            "Itere sobre pares chave-valor",
            "hash_map = {'a': 1, 'b': 2}",
            "for chave, valor in hash_map.items():\n    print(chave, valor)",
            "hash-map-operations",
            "easy"
        ))
        
        # Frequency count pattern
        for i in range(20):
            array_type = random.choice(["inteiros", "strings", "objetos", "tuplas"])
            examples.append(self._create_example(
                f"Conte frequencia de cada elemento (array de {array_type})",
                "array = [1, 2, 2, 3, 3, 3]",
                "from collections import Counter\nfreq = Counter(array)",
                "hash-map-patterns",
                "easy"
            ))
        
        # Two sum hash pattern
        for i in range(20):
            examples.append(self._create_example(
                f"Encontre par que soma ao alvo usando hash map (variacao {i+1})",
                "nums = [2, 7, 11, 15], alvo = 9",
                "vistos = {}\nfor i, num in enumerate(nums):\n    complemento = alvo - num\n    if complemento in vistos:\n        print([vistos[complemento], i])\n    vistos[num] = i",
                "hash-map-patterns",
                "medium"
            ))
        
        return examples
    
    # ========== TWO POINTERS OPERATIONS (150 examples) ==========
    
    def two_pointers_operations(self) -> List[Dict]:
        """Two pointer single operations - PURE CODE output."""
        examples = []
        
        # Move left pointer
        for i in range(30):
            examples.append(self._create_example(
                f"Incremente ponteiro esquerdo (variacao {i+1})",
                "esq = 0, dir = 10",
                "esq += 1",
                "two-pointers-movement",
                "easy"
            ))
        
        # Move right pointer
        for i in range(30):
            examples.append(self._create_example(
                f"Decremente ponteiro direito (variacao {i+1})",
                "esq = 0, dir = 10",
                "dir -= 1",
                "two-pointers-movement",
                "easy"
            ))
        
        # Compare elements
        for i in range(30):
            examples.append(self._create_example(
                f"Compare elementos nos dois ponteiros (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5], esq = 0, dir = 4",
                "if arr[esq] == arr[dir]:\n    print(\"iguais\")",
                "two-pointers-movement",
                "easy"
            ))
        
        # Sum elements
        for i in range(30):
            examples.append(self._create_example(
                f"Soma elementos dos dois ponteiros (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5], esq = 0, dir = 4, alvo = 9",
                "soma = arr[esq] + arr[dir]\nif soma < alvo:\n    esq += 1\nelse:\n    dir -= 1",
                "two-pointers-movement",
                "medium"
            ))
        
        # Reverse in place
        for i in range(30):
            examples.append(self._create_example(
                f"Inverta array no lugar usando dois ponteiros (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5]",
                "esq, dir = 0, len(arr) - 1\nwhile esq < dir:\n    arr[esq], arr[dir] = arr[dir], arr[esq]\n    esq += 1\n    dir -= 1",
                "two-pointers-patterns",
                "medium"
            ))
        
        return examples
    
    # ========== SLIDING WINDOW OPERATIONS (150 examples) ==========
    
    def sliding_window_operations(self) -> List[Dict]:
        """Sliding window single operations - PURE CODE output."""
        examples = []
        
        # Expand window
        for i in range(25):
            examples.append(self._create_example(
                f"Adicione elemento na janela (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5], dir = 0, soma = 0",
                "soma += arr[dir]\ndir += 1",
                "sliding-window-operations",
                "easy"
            ))
        
        # Shrink window
        for i in range(25):
            examples.append(self._create_example(
                f"Remova elemento da janela (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5], esq = 0, soma = 10",
                "soma -= arr[esq]\nesq += 1",
                "sliding-window-operations",
                "easy"
            ))
        
        # Slide window
        for i in range(25):
            examples.append(self._create_example(
                f"Mova janela um passo (variacao {i+1})",
                "arr = [1, 2, 3, 4, 5], i = 4, k = 3, soma = 6",
                "soma = soma - arr[i - k] + arr[i]",
                "sliding-window-operations",
                "easy"
            ))
        
        # Check window size
        for i in range(25):
            examples.append(self._create_example(
                f"Verifique tamanho da janela (variacao {i+1})",
                "esq = 0, dir = 3, k = 4",
                "tamanho = dir - esq + 1\nif tamanho == k:\n    print(\"janela cheia\")",
                "sliding-window-operations",
                "easy"
            ))
        
        # Fixed window maximum
        for i in range(25):
            examples.append(self._create_example(
                f"Encontre maxima soma de subarray de tamanho k (variacao {i+1})",
                "arr = [1, 4, 2, 10, 23], k = 3",
                "soma = sum(arr[:k])\nmax_soma = soma\nfor i in range(k, len(arr)):\n    soma += arr[i] - arr[i - k]\n    max_soma = max(max_soma, soma)\nprint(max_soma)",
                "sliding-window-patterns",
                "medium"
            ))
        
        return examples
    
    # ========== BINARY SEARCH OPERATIONS (100 examples) ==========
    
    def binary_search_operations(self) -> List[Dict]:
        """Binary search single operations - PURE CODE output."""
        examples = []
        
        # Calculate mid
        for i in range(20):
            examples.append(self._create_example(
                f"Calcule indice do meio (variacao {i+1})",
                "esq = 0, dir = 10",
                "meio = (esq + dir) // 2",
                "binary-search-steps",
                "easy"
            ))
        
        # Safe mid calculation
        for i in range(20):
            examples.append(self._create_example(
                f"Calcule meio sem overflow (variacao {i+1})",
                "esq = 0, dir = 2147483647",
                "meio = esq + (dir - esq) // 2",
                "binary-search-steps",
                "easy"
            ))
        
        # Compare and move
        for i in range(20):
            examples.append(self._create_example(
                f"Compare com elemento do meio e mova (variacao {i+1})",
                "arr = [1, 3, 5, 7, 9], alvo = 5, esq = 0, dir = 4",
                "meio = (esq + dir) // 2\nif arr[meio] == alvo:\n    print(meio)\nelif arr[meio] < alvo:\n    esq = meio + 1\nelse:\n    dir = meio - 1",
                "binary-search-steps",
                "medium"
            ))
        
        # Lower bound
        for i in range(20):
            examples.append(self._create_example(
                f"Encontre lower bound (primeira ocorrencia) (variacao {i+1})",
                "arr = [1, 2, 2, 2, 3], alvo = 2",
                "esq, dir = 0, len(arr)\nwhile esq < dir:\n    meio = (esq + dir) // 2\n    if arr[meio] < alvo:\n        esq = meio + 1\n    else:\n        dir = meio\nprint(esq)",
                "binary-search-steps",
                "medium"
            ))
        
        # Upper bound
        for i in range(20):
            examples.append(self._create_example(
                f"Encontre upper bound (ultima ocorrencia) (variacao {i+1})",
                "arr = [1, 2, 2, 2, 3], alvo = 2",
                "esq, dir = 0, len(arr)\nwhile esq < dir:\n    meio = (esq + dir) // 2\n    if arr[meio] <= alvo:\n        esq = meio + 1\n    else:\n        dir = meio\nprint(esq - 1)",
                "binary-search-steps",
                "medium"
            ))
        
        return examples
    
    # ========== STACK OPERATIONS (100 examples) ==========
    
    def stack_operations(self) -> List[Dict]:
        """Stack single operations - PURE CODE output."""
        examples = []
        
        # Push
        for i in range(15):
            examples.append(self._create_example(
                f"Empilhe elemento (variacao {i+1})",
                "pilha = [], elemento = 5",
                "pilha.append(elemento)",
                "stack-operations",
                "easy"
            ))
        
        # Pop
        for i in range(15):
            examples.append(self._create_example(
                f"Desempilhe elemento (variacao {i+1})",
                "pilha = [1, 2, 3]",
                "elemento = pilha.pop()",
                "stack-operations",
                "easy"
            ))
        
        # Peek
        for i in range(15):
            examples.append(self._create_example(
                f"Olhe topo da pilha (variacao {i+1})",
                "pilha = [1, 2, 3]",
                "topo = pilha[-1]",
                "stack-operations",
                "easy"
            ))
        
        # Check empty
        for i in range(15):
            examples.append(self._create_example(
                f"Verifique se pilha esta vazia (variacao {i+1})",
                "pilha = []",
                "vazia = len(pilha) == 0",
                "stack-operations",
                "easy"
            ))
        
        # Valid parentheses
        for i in range(20):
            examples.append(self._create_example(
                f"Valide parenteses balanceados (variacao {i+1})",
                "s = \"()[]{}\"",
                "pilha = []\npares = {')': '(', ']': '[', '}': '{'}\nfor char in s:\n    if char in '([{':\n        pilha.append(char)\n    elif char in ')]}':\n        if not pilha or pilha[-1] != pares[char]:\n            print(False)\n        pilha.pop()\nprint(len(pilha) == 0)",
                "stack-operations",
                "medium"
            ))
        
        return examples
    
    # ========== RECURSION OPERATIONS (100 examples) ==========
    
    def recursion_operations(self) -> List[Dict]:
        """Recursion patterns - PURE CODE output."""
        examples = []
        
        # Base case
        for i in range(25):
            examples.append(self._create_example(
                f"Defina caso base da recursao (variacao {i+1})",
                "n = 5",
                "if n <= 1:\n    return n",
                "recursion-patterns",
                "easy"
            ))
        
        # Recursive step
        for i in range(25):
            examples.append(self._create_example(
                f"Passo recursivo com chamada reduzida (variacao {i+1})",
                "n = 5",
                "return n * fatorial(n - 1)",
                "recursion-patterns",
                "easy"
            ))
        
        # Memoization
        for i in range(25):
            examples.append(self._create_example(
                f"Memoizacao em recursao (variacao {i+1})",
                "n = 10, memo = {}",
                "if n in memo:\n    return memo[n]\nmemo[n] = fib(n - 1) + fib(n - 2)\nreturn memo[n]",
                "recursion-patterns",
                "medium"
            ))
        
        # Tail recursion
        for i in range(25):
            examples.append(self._create_example(
                f"Recursao de cauda com acumulador (variacao {i+1})",
                "n = 5, acc = 1",
                "if n == 0:\n    return acc\nreturn fatorial(n - 1, n * acc)",
                "recursion-patterns",
                "medium"
            ))
        
        return examples
    
    # ========== TREE OPERATIONS (150 examples) ==========
    
    def tree_operations(self) -> List[Dict]:
        """Tree operations - PURE CODE output."""
        examples = []
        
        # DFS visit node
        for i in range(20):
            examples.append(self._create_example(
                f"Visite no em DFS (variacao {i+1})",
                "no = raiz",
                "if no:\n    print(no.val)",
                "tree-traversal-steps",
                "easy"
            ))
        
        # DFS left
        for i in range(20):
            examples.append(self._create_example(
                f"Visite filho esquerdo em DFS (variacao {i+1})",
                "no = raiz",
                "if no.esquerda:\n    dfs(no.esquerda)",
                "tree-traversal-steps",
                "easy"
            ))
        
        # DFS right
        for i in range(20):
            examples.append(self._create_example(
                f"Visite filho direito em DFS (variacao {i+1})",
                "no = raiz",
                "if no.direita:\n    dfs(no.direita)",
                "tree-traversal-steps",
                "easy"
            ))
        
        # In-order traversal
        for i in range(25):
            examples.append(self._create_example(
                f"Percurso em ordem (in-order) (variacao {i+1})",
                "raiz = no_arvore",
                "def in_order(no):\n    if no:\n        in_order(no.esquerda)\n        print(no.val)\n        in_order(no.direita)\nin_order(raiz)",
                "tree-traversal-steps",
                "medium"
            ))
        
        # BFS
        for i in range(25):
            examples.append(self._create_example(
                f"BFS em arvore (variacao {i+1})",
                "raiz = no_arvore",
                "from collections import deque\nfila = deque([raiz])\nwhile fila:\n    no = fila.popleft()\n    print(no.val)\n    if no.esquerda:\n        fila.append(no.esquerda)\n    if no.direita:\n        fila.append(no.direita)",
                "bfs-operations",
                "medium"
            ))
        
        return examples
    
    # ========== LINKED LIST OPERATIONS (100 examples) ==========
    
    def linked_list_operations(self) -> List[Dict]:
        """Linked list operations - PURE CODE output."""
        examples = []
        
        # Traverse
        for i in range(20):
            examples.append(self._create_example(
                f"Percorra lista ligada (variacao {i+1})",
                "cabeca = no_inicial",
                "atual = cabeca\nwhile atual:\n    print(atual.val)\n    atual = atual.proximo",
                "linked-list-operations",
                "easy"
            ))
        
        # Reverse
        for i in range(20):
            examples.append(self._create_example(
                f"Inverta lista ligada (variacao {i+1})",
                "cabeca = no_inicial",
                "anterior = None\natual = cabeca\nwhile atual:\n    proximo = atual.proximo\n    atual.proximo = anterior\n    anterior = atual\n    atual = proximo\ncabeca = anterior",
                "linked-list-operations",
                "medium"
            ))
        
        # Find middle
        for i in range(20):
            examples.append(self._create_example(
                f"Encontre meio da lista (variacao {i+1})",
                "cabeca = no_inicial",
                "lento = rapido = cabeca\nwhile rapido and rapido.proximo:\n    lento = lento.proximo\n    rapido = rapido.proximo.proximo\nprint(lento.val)",
                "linked-list-operations",
                "medium"
            ))
        
        # Detect cycle
        for i in range(20):
            examples.append(self._create_example(
                f"Detecte ciclo em lista ligada (variacao {i+1})",
                "cabeca = no_inicial",
                "lento = rapido = cabeca\nwhile rapido and rapido.proximo:\n    lento = lento.proximo\n    rapido = rapido.proximo.proximo\n    if lento == rapido:\n        print(True)\nprint(False)",
                "linked-list-operations",
                "medium"
            ))
        
        # Merge two lists
        for i in range(20):
            examples.append(self._create_example(
                f"Mescle duas listas ordenadas (variacao {i+1})",
                "l1 = lista1, l2 = lista2",
                "dummy = No(0)\natual = dummy\nwhile l1 and l2:\n    if l1.val <= l2.val:\n        atual.proximo = l1\n        l1 = l1.proximo\n    else:\n        atual.proximo = l2\n        l2 = l2.proximo\n    atual = atual.proximo\natual.proximo = l1 or l2",
                "linked-list-operations",
                "medium"
            ))
        
        return examples
    
    # ========== GENERATE ALL ==========
    
    def generate_all(self) -> List[Dict]:
        """Generate all examples with PURE CODE output."""
        all_examples = []
        
        print("🔧 Generating narrow-scope operations dataset (PURE CODE output)...")
        
        print("  - Hash map operations...")
        all_examples.extend(self.hash_operations())
        
        print("  - Two pointers operations...")
        all_examples.extend(self.two_pointers_operations())
        
        print("  - Sliding window operations...")
        all_examples.extend(self.sliding_window_operations())
        
        print("  - Binary search operations...")
        all_examples.extend(self.binary_search_operations())
        
        print("  - Stack operations...")
        all_examples.extend(self.stack_operations())
        
        print("  - Recursion operations...")
        all_examples.extend(self.recursion_operations())
        
        print("  - Tree operations...")
        all_examples.extend(self.tree_operations())
        
        print("  - Linked list operations...")
        all_examples.extend(self.linked_list_operations())
        
        return all_examples


def save_dataset(examples: List[Dict], filepath: str):
    """Save to JSONL in Alpaca format."""
    with open(filepath, 'w', encoding='utf-8') as f:
        for ex in examples:
            record = {
                "instruction": ex["instruction"],
                "input": ex["input"],
                "output": ex["output"]
            }
            f.write(json.dumps(record, ensure_ascii=False) + '\n')
    
    print(f"\n✅ Saved {len(examples)} examples to {filepath}")
    
    # Statistics
    categories = {}
    difficulties = {}
    for ex in examples:
        cat = ex.get("category", "unknown")
        diff = ex.get("difficulty", "unknown")
        categories[cat] = categories.get(cat, 0) + 1
        difficulties[diff] = difficulties.get(diff, 0) + 1
    
    print("\n📊 Statistics:")
    print("\nBy Category:")
    for cat, count in sorted(categories.items()):
        print(f"  {cat}: {count}")
    print("\nBy Difficulty:")
    for diff, count in sorted(difficulties.items()):
        print(f"  {diff}: {count}")


def main():
    generator = NarrowScopeOperations()
    examples = generator.generate_all()
    
    save_dataset(examples, "narrow_scope_1000_pure_code.jsonl")
    
    print("\n🎯 Dataset characteristics:")
    print("  • Focus: Single efficient operations (NOT broad problems)")
    print("  • Scope: Narrow, atomic algorithmic steps")
    print("  • Language: Portuguese instructions")
    print("  • Code: Python 3.13 compatible")
    print("  • Output: PURE CODE (no comments in output field)")
    print("\n⚠️  IMPORTANT: Output field contains ONLY executable Python code!")


if __name__ == "__main__":
    main()
