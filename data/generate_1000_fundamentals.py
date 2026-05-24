#!/usr/bin/env python3
"""
Generate 1000 narrow-scope DSA operations dataset.
Focus: Efficient single operations, NOT broad problem solutions.
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
    
    # ========== HASH MAP OPERATIONS (150 examples) ==========
    
    def hash_single_lookups(self) -> List[Dict]:
        """Single lookup operations with hash maps."""
        examples = []
        
        variations = [
            ("Verifique se elemento existe em hash map", "elemento in hash_map", "O(1)"),
            ("Obtenha valor de hash map com valor padrao", "hash_map.get(chave, padrao)", "O(1)"),
            ("Atualize contagem em hash map", "hash_map[chave] = hash_map.get(chave, 0) + 1", "O(1)"),
            ("Delete chave de hash map", "del hash_map[chave]", "O(1)"),
            ("Verifique se hash map esta vazio", "len(hash_map) == 0", "O(1)"),
            ("Itere sobre chaves do hash map", "for chave in hash_map:", "O(n)"),
            ("Itere sobre valores do hash map", "for valor in hash_map.values():", "O(n)"),
            ("Itere sobre pares chave-valor", "for chave, valor in hash_map.items():", "O(n)"),
            ("Verifique se todas chaves existem", "all(chave in hash_map for chave in chaves)", "O(k)"),
            ("Mesclar dois hash maps", "dict1.update(dict2)", "O(m)"),
        ]
        
        for instr, code, comp in variations:
            # Multiple contexts for same operation
            for context in ["contagem", "mapeamento", "cache", "indice"]:
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{instr} (contexto: {context})",
                    "input": f"hash_map = {{'a': 1, 'b': 2}}, chave = 'a'",
                    "output": f"# Operacao: {instr}\n{code}\n\n# Complexidade: {comp}",
                    "category": "hash-map-operations",
                    "difficulty": "easy"
                })
        
        return examples
    
    def hash_patterns(self) -> List[Dict]:
        """Common hash-based algorithm patterns."""
        examples = []
        
        patterns = [
            {
                "name": "frequency-count",
                "instruction": "Conte frequencia de cada elemento",
                "code": "from collections import Counter\nfreq = Counter(array)",
                "complexity": "O(n)"
            },
            {
                "name": "two-sum-hash",
                "instruction": "Encontre complemento no hash map",
                "code": "for num in nums:\n    if alvo - num in seen:\n        return [seen[alvo-num], i]\n    seen[num] = i",
                "complexity": "O(n)"
            },
            {
                "name": "group-by-key",
                "instruction": "Agrupe elementos por categoria",
                "code": "grupos = {}\nfor item in items:\n    categoria = item.categoria\n    if categoria not in grupos:\n        grupos[categoria] = []\n    grupos[categoria].append(item)",
                "complexity": "O(n)"
            },
            {
                "name": "first-unique",
                "instruction": "Encontre primeiro elemento unico",
                "code": "for num in nums:\n    if freq[num] == 1:\n        return num",
                "complexity": "O(n)"
            },
        ]
        
        for pattern in patterns:
            # Generate 20 variations with different contexts
            for i in range(20):
                array_type = random.choice(["inteiros", "strings", "objetos", "tuplas"])
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{pattern['instruction']} (array de {array_type})",
                    "input": f"array = [...]  # lista de {array_type}",
                    "output": f"# Padrao: {pattern['name']}\n{pattern['code']}\n\n# Complexidade: {pattern['complexity']}",
                    "category": "hash-patterns",
                    "difficulty": random.choice(["easy", "medium"])
                })
        
        return examples
    
    # ========== TWO POINTERS OPERATIONS (150 examples) ==========
    
    def pointer_movements(self) -> List[Dict]:
        """Single pointer movement operations."""
        examples = []
        
        movements = [
            ("Incremente ponteiro esquerdo", "esq += 1", "move towards center"),
            ("Decremente ponteiro direito", "dir -= 1", "move towards center"),
            ("Avance ponteiro rapido 2 passos", "rapido = rapido.proximo.proximo", "tortoise-hare"),
            ("Avance ponteiro lento 1 passo", "lento = lento.proximo", "tortoise-hare"),
            ("Compare elementos nos dois ponteiros", "if arr[esq] == arr[dir]:", "palindrome check"),
            ("Soma elementos dos dois ponteiros", "soma = arr[esq] + arr[dir]", "two sum sorted"),
            ("Mova ponteiros baseado na soma", "if soma < alvo: esq += 1 else: dir -= 1", "two sum logic"),
            ("Encontre meio com dois ponteiros", "while rapido and rapido.next: lento=lento.next; rapido=rapido.next.next", "middle element"),
        ]
        
        for instr, code, context in movements:
            # Multiple data structure contexts
            for ds in ["array", "lista-ligada", "string"]:
                for i in range(10):
                    examples.append({
                        "id": self.next_id(),
                        "instruction": f"{instr} em {ds}",
                        "input": f"# Contexto: {context}\n# Estrutura: {ds}",
                        "output": f"# Operacao: {instr}\n{code}",
                        "category": "two-pointers-movement",
                        "difficulty": "easy"
                    })
        
        return examples
    
    def pointer_patterns(self) -> List[Dict]:
        """Two pointer algorithm patterns."""
        examples = []
        
        patterns = [
            {
                "name": "reverse-in-place",
                "code": "while esq < dir:\n    arr[esq], arr[dir] = arr[dir], arr[esq]\n    esq += 1\n    dir -= 1",
                "desc": "Inverta array no lugar"
            },
            {
                "name": "partition",
                "code": "while esq <= dir:\n    while esq <= dir and arr[esq] < pivo:\n        esq += 1\n    while esq <= dir and arr[dir] > pivo:\n        dir -= 1\n    if esq <= dir:\n        arr[esq], arr[dir] = arr[dir], arr[esq]\n        esq += 1\n        dir -= 1",
                "desc": "Particione array em torno do pivo"
            },
            {
                "name": "merge-sorted",
                "code": "while i < len(arr1) and j < len(arr2):\n    if arr1[i] <= arr2[j]:\n        resultado.append(arr1[i])\n        i += 1\n    else:\n        resultado.append(arr2[j])\n        j += 1\nresultado.extend(arr1[i:])\nresultado.extend(arr2[j:])",
                "desc": "Mescle dois arrays ordenados"
            },
        ]
        
        for pattern in patterns:
            for i in range(30):
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{pattern['desc']} (variacao {i+1})",
                    "input": "Dois ponteiros: esq=0, dir=n-1",
                    "output": f"# Padrao: {pattern['name']}\n{pattern['code']}\n\n# Complexidade: O(n)",
                    "category": "two-pointers-patterns",
                    "difficulty": "medium"
                })
        
        return examples
    
    # ========== SLIDING WINDOW OPERATIONS (150 examples) ==========
    
    def window_operations(self) -> List[Dict]:
        """Sliding window single operations."""
        examples = []
        
        operations = [
            ("Adicione elemento na janela", "soma += arr[dir]", "expand window"),
            ("Remova elemento da janela", "soma -= arr[esq]", "shrink window"),
            ("Mova janela um passo", "soma = soma - arr[i-k] + arr[i]", "slide window"),
            ("Verifique tamanho da janela", "if dir - esq + 1 == k:", "window size check"),
            ("Atualize maximo na janela", "max_val = max(max_val, window_sum)", "track max"),
            ("Atualize minimo na janela", "min_val = min(min_val, window_sum)", "track min"),
            ("Conte elementos na janela", "count = dir - esq + 1", "count elements"),
            ("Verifique se elemento esta na janela", "if x in arr[esq:dir+1]:", "membership check"),
        ]
        
        for instr, code, context in operations:
            for i in range(15):
                problem_type = random.choice(["soma", "maximo", "media", "contagem"])
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{instr} para problema de {problem_type}",
                    "input": f"# Contexto: {context}\n# Tipo: {problem_type}",
                    "output": f"# Operacao: {instr}\n{code}\n\n# Complexidade: O(1)",
                    "category": "sliding-window-operations",
                    "difficulty": "easy"
                })
        
        return examples
    
    def window_patterns(self) -> List[Dict]:
        """Common sliding window patterns."""
        examples = []
        
        patterns = [
            {
                "name": "fixed-window",
                "code": "soma = sum(arr[:k])\nmax_soma = soma\nfor i in range(k, len(arr)):\n    soma += arr[i] - arr[i-k]\n    max_soma = max(max_soma, soma)",
                "desc": "Encontre maxima soma de subarray de tamanho k"
            },
            {
                "name": "variable-window",
                "code": "while dir < len(arr):\n    janela.add(arr[dir])\n    while len(janela) > k:\n        janela.remove(arr[esq])\n        esq += 1\n    max_len = max(max_len, dir - esq + 1)\n    dir += 1",
                "desc": "Encontre maior substring com k caracteres unicos"
            },
            {
                "name": "two-window",
                "code": "while dir < len(arr):\n    freq[arr[dir]] += 1\n    while len(freq) > 2:\n        freq[arr[esq]] -= 1\n        if freq[arr[esq]] == 0:\n            del freq[arr[esq]]\n        esq += 1\n    max_len = max(max_len, dir - esq + 1)\n    dir += 1",
                "desc": "Fruit into baskets (max 2 types)"
            },
        ]
        
        for pattern in patterns:
            for i in range(30):
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{pattern['desc']} (variacao {i+1})",
                    "input": "Array e tamanho de janela",
                    "output": f"# Padrao: {pattern['name']}\n{pattern['code']}\n\n# Complexidade: O(n)",
                    "category": "sliding-window-patterns",
                    "difficulty": "medium"
                })
        
        return examples
    
    # ========== BINARY SEARCH OPERATIONS (100 examples) ==========
    
    def binary_search_steps(self) -> List[Dict]:
        """Individual binary search steps."""
        examples = []
        
        steps = [
            ("Calcule indice do meio", "meio = (esq + dir) // 2", "avoid overflow"),
            ("Calcule meio sem overflow", "meio = esq + (dir - esq) // 2", "safe mid"),
            ("Compare com elemento do meio", "if arr[meio] == alvo: return meio", "found"),
            ("Va para esquerda", "dir = meio - 1", "search left"),
            ("Va para direita", "esq = meio + 1", "search right"),
            ("Verifique se elemento nao existe", "if esq > dir: return -1", "not found"),
            ("Encontre boundary esquerda", "if arr[meio] < alvo: esq = meio + 1 else: dir = meio", "lower bound"),
            ("Encontre boundary direita", "if arr[meio] <= alvo: esq = meio + 1 else: dir = meio", "upper bound"),
        ]
        
        for instr, code, context in steps:
            for i in range(12):
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{instr}",
                    "input": f"# Contexto: {context}\n# Array ordenado",
                    "output": f"# Operacao: {instr}\n{code}\n\n# Complexidade: O(1)",
                    "category": "binary-search-steps",
                    "difficulty": "easy"
                })
        
        return examples
    
    # ========== STACK OPERATIONS (100 examples) ==========
    
    def stack_operations(self) -> List[Dict]:
        """Single stack operations."""
        examples = []
        
        operations = [
            ("Empilhe elemento", "pilha.append(x)", "push"),
            ("Desempilhe elemento", "x = pilha.pop()", "pop"),
            ("Olhe topo", "topo = pilha[-1]", "peek"),
            ("Verifique se vazia", "if not pilha:", "is empty"),
            ("Obtenha tamanho", "tamanho = len(pilha)", "size"),
            ("Itere sobre pilha", "for elem in reversed(pilha):", "iterate"),
            ("Copie pilha", "pilha_copy = pilha.copy()", "copy"),
        ]
        
        for instr, code, context in operations:
            for i in range(14):
                use_case = random.choice(["validacao", "dfs", "calculo", "parse"])
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{instr} (caso: {use_case})",
                    "input": f"pilha = []",
                    "output": f"# Operacao: {instr}\n{code}\n\n# Contexto: {context}",
                    "category": "stack-operations",
                    "difficulty": "easy"
                })
        
        return examples
    
    # ========== RECURSION OPERATIONS (100 examples) ==========
    
    def recursion_patterns(self) -> List[Dict]:
        """Recursion fundamental patterns."""
        examples = []
        
        patterns = [
            {
                "name": "base-case",
                "code": "if n <= 1:\n    return n",
                "desc": "Defina caso base da recursao"
            },
            {
                "name": "recursive-step",
                "code": "return n * fatorial(n-1)",
                "desc": "Passo recursivo com chamada reduzida"
            },
            {
                "name": "tail-recursion",
                "code": "def helper(n, acc):\n    if n == 0:\n        return acc\n    return helper(n-1, n*acc)",
                "desc": "Recursao de cauda com acumulador"
            },
            {
                "name": "divide-conquer",
                "code": "meio = len(arr) // 2\nesq = merge_sort(arr[:meio])\ndir = merge_sort(arr[meio:])\nreturn merge(esq, dir)",
                "desc": "Divida e conquiste"
            },
        ]
        
        for pattern in patterns:
            for i in range(25):
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{pattern['desc']} (variacao {i+1})",
                    "input": "Funcao recursiva",
                    "output": f"# Padrao: {pattern['name']}\n{pattern['code']}",
                    "category": "recursion-patterns",
                    "difficulty": random.choice(["easy", "medium"])
                })
        
        return examples
    
    # ========== TREE OPERATIONS (150 examples) ==========
    
    def tree_traversal_steps(self) -> List[Dict]:
        """Single tree traversal steps."""
        examples = []
        
        steps = [
            ("Visite no", "resultado.append(no.val)", "visit"),
            ("Va para filho esquerdo", "dfs(no.esquerda)", "left"),
            ("Va para filho direito", "dfs(no.direita)", "right"),
            ("Verifique se no e nulo", "if not no: return", "null check"),
            ("Obtenha valor do no", "valor = no.val", "get value"),
            ("Crie no", "no = No(valor)", "create node"),
            ("Conecte filho", "no.esquerda = filho", "connect"),
        ]
        
        for instr, code, context in steps:
            for traversal in ["in-order", "pre-order", "post-order"]:
                for i in range(5):
                    examples.append({
                        "id": self.next_id(),
                        "instruction": f"{instr} ({traversal})",
                        "input": f"No atual",
                        "output": f"# Passo: {context}\n{code}",
                        "category": "tree-traversal-steps",
                        "difficulty": "easy"
                    })
        
        return examples
    
    def bfs_operations(self) -> List[Dict]:
        """BFS single operations."""
        examples = []
        
        operations = [
            ("Inicialize fila BFS", "fila = deque([raiz])", "init"),
            ("Processe nivel atual", "for _ in range(len(fila)):", "process level"),
            ("Remova da fila", "no = fila.popleft()", "dequeue"),
            ("Adicione filhos", "if no.esquerda: fila.append(no.esquerda)", "enqueue left"),
            ("Adicione filhos", "if no.direita: fila.append(no.direita)", "enqueue right"),
            ("Verifique fim de nivel", "if i == len(fila) - 1: # ultimo do nivel", "level end"),
        ]
        
        for instr, code, context in operations:
            for i in range(15):
                examples.append({
                    "id": self.next_id(),
                    "instruction": f"{instr}",
                    "input": f"Arvore binaria",
                    "output": f"# Operacao BFS: {context}\n{code}\n\nfrom collections import deque",
                    "category": "bfs-operations",
                    "difficulty": "medium"
                })
        
        return examples
    
    # ========== GENERATE ALL ==========
    
    def generate_all(self) -> List[Dict]:
        """Generate all 1000 examples."""
        all_examples = []
        
        print("🔧 Generating narrow-scope operations dataset...")
        
        print("  - Hash map operations...")
        all_examples.extend(self.hash_single_lookups())
        all_examples.extend(self.hash_patterns())
        
        print("  - Two pointers operations...")
        all_examples.extend(self.pointer_movements())
        all_examples.extend(self.pointer_patterns())
        
        print("  - Sliding window operations...")
        all_examples.extend(self.window_operations())
        all_examples.extend(self.window_patterns())
        
        print("  - Binary search operations...")
        all_examples.extend(self.binary_search_steps())
        
        print("  - Stack operations...")
        all_examples.extend(self.stack_operations())
        
        print("  - Recursion operations...")
        all_examples.extend(self.recursion_patterns())
        
        print("  - Tree operations...")
        all_examples.extend(self.tree_traversal_steps())
        all_examples.extend(self.bfs_operations())
        
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
    
    save_dataset(examples, "narrow_scope_1000.jsonl")
    
    print("\n🎯 Dataset characteristics:")
    print("  • Focus: Single efficient operations (NOT broad problems)")
    print("  • Scope: Narrow, atomic algorithmic steps")
    print("  • Language: Portuguese instructions")
    print("  • Code: Python 3.13 compatible")
    print("  • Examples:")
    print("     - Hash map single lookups")
    print("     - Pointer movements")
    print("     - Window slide operations")
    print("     - Binary search steps")
    print("     - Stack single operations")
    print("     - Recursion base cases")
    print("     - Tree traversal steps")


if __name__ == "__main__":
    main()
