#!/usr/bin/env python3
"""
Generate high-quality DSA operations dataset with REAL variations.
Each example is unique with different contexts, data types, and use cases.
NO "variacao N" - only meaningful differences.
"""

import json
from typing import List, Dict


class QualityDSAOperations:
    """Generate unique, high-quality DSA operations."""
    
    def __init__(self):
        self.example_id = 0
        
    def next_id(self):
        self.example_id += 1
        return self.example_id
    
    def _create_example(self, instruction: str, input_text: str, output_code: str, 
                        category: str, difficulty: str = "easy") -> Dict:
        return {
            "id": self.next_id(),
            "instruction": instruction,
            "input": input_text,
            "output": output_code.strip(),
            "category": category,
            "difficulty": difficulty
        }
    
    # ========== HASH MAP - REAL VARIATIONS ==========
    
    def hash_map_operations(self) -> List[Dict]:
        """Hash map operations with real different contexts."""
        examples = []
        
        # Different lookup scenarios
        examples.append(self._create_example(
            "Verifique se usuario existe no cache",
            "cache = {'user_1': 'Joao', 'user_2': 'Maria'}, user_id = 'user_1'",
            "existe = user_id in cache",
            "hash-map-lookup",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Verifique se palavra ja foi vista em analise de texto",
            "palavras_vistas = {'python': True, 'codigo': True}, palavra = 'java'",
            "ja_vista = palavra in palavras_vistas",
            "hash-map-lookup",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Verifique se produto esta em estoque",
            "estoque = {'mouse': 10, 'teclado': 5}, produto = 'monitor'",
            "tem_estoque = produto in estoque and estoque[produto] > 0",
            "hash-map-lookup",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Verifique se aluno ja fez prova",
            "provas_feitas = {'Joao': 8.5, 'Maria': 9.0}, aluno = 'Pedro'",
            "fez_prova = aluno in provas_feitas",
            "hash-map-lookup",
            "easy"
        ))
        
        # Get with default - different scenarios
        examples.append(self._create_example(
            "Obtenha preco do produto ou retorne 0 se nao existir",
            "precos = {'cafe': 5.0, 'cha': 4.0}, produto = 'suco'",
            "preco = precos.get(produto, 0.0)",
            "hash-map-get",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Obtenha nota do aluno ou retorne 'N/A' se nao tiver",
            "notas = {'Joao': 8.5}, aluno = 'Maria'",
            "nota = notas.get(aluno, 'N/A')",
            "hash-map-get",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Obtenha configuracao ou use valor padrao",
            "config = {'tema': 'escuro'}, chave = 'fonte'",
            "valor = config.get(chave, 'padrao')",
            "hash-map-get",
            "easy"
        ))
        
        # Count frequency - different data types
        examples.append(self._create_example(
            "Conte frequencia de numeros em array de inteiros",
            "numeros = [1, 2, 2, 3, 3, 3]",
            "from collections import Counter\nfreq = Counter(numeros)",
            "hash-map-frequency",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Conte frequencia de palavras em texto",
            "palavras = ['python', 'e', 'python', 'legal']",
            "from collections import Counter\nfreq = Counter(palavras)",
            "hash-map-frequency",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Conte frequencia de caracteres em string",
            "texto = 'abracadabra'",
            "from collections import Counter\nfreq = Counter(texto)",
            "hash-map-frequency",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Conte ocorrencias de elementos em tuplas",
            "dados = [('a', 1), ('b', 2), ('a', 1)]",
            "from collections import Counter\nfreq = Counter(dados)",
            "hash-map-frequency",
            "easy"
        ))
        
        # Update operations
        examples.append(self._create_example(
            "Incremente contador de votos para candidato",
            "votos = {'candidato_A': 100}, candidato = 'candidato_A'",
            "votos[candidato] = votos.get(candidato, 0) + 1",
            "hash-map-update",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Atualize estoque ao vender produto",
            "estoque = {'camiseta': 50}, produto = 'camiseta'",
            "if produto in estoque:\n    estoque[produto] -= 1",
            "hash-map-update",
            "easy"
        ))
        
        examples.append(self._create_example(
            "Some pontos ao score do jogador",
            "scores = {'player1': 100}, jogador = 'player1', pontos = 10",
            "scores[jogador] = scores.get(jogador, 0) + pontos",
            "hash-map-update",
            "easy"
        ))
        
        # Two sum variations
        examples.append(self._create_example(
            "Encontre dois numeros que somam ao alvo em array ordenado",
            "nums = [2, 7, 11, 15], alvo = 9",
            "vistos = {}\nfor i, num in enumerate(nums):\n    complemento = alvo - num\n    if complemento in vistos:\n        print([vistos[complemento], i])\n    vistos[num] = i",
            "hash-map-two-sum",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre par de precos que somam ao orcamento",
            "precos = [20, 30, 50, 70], orcamento = 90",
            "vistos = {}\nfor i, preco in enumerate(precos):\n    complemento = orcamento - preco\n    if complemento in vistos:\n        print([vistos[complemento], i])\n    vistos[preco] = i",
            "hash-map-two-sum",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre duas idades que somam a meta",
            "idades = [25, 35, 45, 55], meta = 80",
            "vistos = {}\nfor i, idade in enumerate(idades):\n    complemento = meta - idade\n    if complemento in vistos:\n        print([vistos[complemento], i])\n    vistos[idade] = i",
            "hash-map-two-sum",
            "medium"
        ))
        
        # Group by
        examples.append(self._create_example(
            "Agrupe alunos por turma",
            "alunos = [('Joao', 'A'), ('Maria', 'B'), ('Pedro', 'A')]",
            "grupos = {}\nfor aluno, turma in alunos:\n    if turma not in grupos:\n        grupos[turma] = []\n    grupos[turma].append(aluno)",
            "hash-map-group",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Agrupe produtos por categoria",
            "produtos = [('mouse', 'informatica'), ('cafe', 'alimentos')]",
            "grupos = {}\nfor produto, categoria in produtos:\n    if categoria not in grupos:\n        grupos[categoria] = []\n    grupos[categoria].append(produto)",
            "hash-map-group",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Agrupe palavras por tamanho",
            "palavras = ['python', 'java', 'go', 'ruby']",
            "grupos = {}\nfor palavra in palavras:\n    tam = len(palavra)\n    if tam not in grupos:\n        grupos[tam] = []\n    grupos[tam].append(palavra)",
            "hash-map-group",
            "medium"
        ))
        
        return examples
    
    # ========== TWO POINTERS - REAL VARIATIONS ==========
    
    def two_pointers_operations(self) -> List[Dict]:
        """Two pointers with real different scenarios."""
        examples = []
        
        # Reverse array variations
        examples.append(self._create_example(
            "Inverta array de numeros no lugar",
            "arr = [1, 2, 3, 4, 5]",
            "esq, dir = 0, len(arr) - 1\nwhile esq < dir:\n    arr[esq], arr[dir] = arr[dir], arr[esq]\n    esq += 1\n    dir -= 1",
            "two-pointers-reverse",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Inverta string convertendo para lista",
            "s = 'python'",
            "arr = list(s)\nesq, dir = 0, len(arr) - 1\nwhile esq < dir:\n    arr[esq], arr[dir] = arr[dir], arr[esq]\n    esq += 1\n    dir -= 1\nresultado = ''.join(arr)",
            "two-pointers-reverse",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Inverta apenas metade do array",
            "arr = [1, 2, 3, 4, 5, 6]",
            "esq, dir = 0, len(arr) // 2 - 1\nwhile esq < dir:\n    arr[esq], arr[dir] = arr[dir], arr[esq]\n    esq += 1\n    dir -= 1",
            "two-pointers-reverse",
            "medium"
        ))
        
        # Two sum sorted variations
        examples.append(self._create_example(
            "Encontre dois numeros que somam ao alvo em array ordenado",
            "arr = [2, 7, 11, 15], alvo = 9",
            "esq, dir = 0, len(arr) - 1\nwhile esq < dir:\n    soma = arr[esq] + arr[dir]\n    if soma == alvo:\n        print([esq, dir])\n        break\n    elif soma < alvo:\n        esq += 1\n    else:\n        dir -= 1",
            "two-pointers-sum",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre dois precos dentro do orcamento mais proximo possivel",
            "precos = [10, 20, 30, 40], orcamento = 55",
            "esq, dir = 0, len(precos) - 1\nmais_proximo = 0\nwhile esq < dir:\n    soma = precos[esq] + precos[dir]\n    if soma <= orcamento:\n        mais_proximo = max(mais_proximo, soma)\n        esq += 1\n    else:\n        dir -= 1\nprint(mais_proximo)",
            "two-pointers-sum",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Conte pares que somam menos que o alvo",
            "arr = [1, 2, 3, 4, 5], alvo = 7",
            "esq, dir = 0, len(arr) - 1\ncontagem = 0\nwhile esq < dir:\n    if arr[esq] + arr[dir] < alvo:\n        contagem += dir - esq\n        esq += 1\n    else:\n        dir -= 1\nprint(contagem)",
            "two-pointers-sum",
            "medium"
        ))
        
        # Palindrome variations
        examples.append(self._create_example(
            "Verifique se string e palindromo considerando apenas letras",
            "s = 'A man, a plan, a canal: Panama'",
            "esq, dir = 0, len(s) - 1\neh_palindromo = True\nwhile esq < dir:\n    while esq < dir and not s[esq].isalnum():\n        esq += 1\n    while esq < dir and not s[dir].isalnum():\n        dir -= 1\n    if s[esq].lower() != s[dir].lower():\n        eh_palindromo = False\n        break\n    esq += 1\n    dir -= 1\nprint(eh_palindromo)",
            "two-pointers-palindrome",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Verifique se array e palindromo",
            "arr = [1, 2, 3, 2, 1]",
            "esq, dir = 0, len(arr) - 1\neh_palindromo = True\nwhile esq < dir:\n    if arr[esq] != arr[dir]:\n        eh_palindromo = False\n        break\n    esq += 1\n    dir -= 1\nprint(eh_palindromo)",
            "two-pointers-palindrome",
            "easy"
        ))
        
        # Merge sorted arrays
        examples.append(self._create_example(
            "Mescle dois arrays ordenados",
            "arr1 = [1, 3, 5], arr2 = [2, 4, 6]",
            "resultado = []\ni, j = 0, 0\nwhile i < len(arr1) and j < len(arr2):\n    if arr1[i] <= arr2[j]:\n        resultado.append(arr1[i])\n        i += 1\n    else:\n        resultado.append(arr2[j])\n        j += 1\nresultado.extend(arr1[i:])\nresultado.extend(arr2[j:])",
            "two-pointers-merge",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre intersecao de dois arrays ordenados",
            "arr1 = [1, 2, 3, 4], arr2 = [2, 4, 6]",
            "intersecao = []\ni, j = 0, 0\nwhile i < len(arr1) and j < len(arr2):\n    if arr1[i] == arr2[j]:\n        intersecao.append(arr1[i])\n        i += 1\n        j += 1\n    elif arr1[i] < arr2[j]:\n        i += 1\n    else:\n        j += 1\nprint(intersecao)",
            "two-pointers-intersection",
            "medium"
        ))
        
        return examples
    
    # ========== SLIDING WINDOW - REAL VARIATIONS ==========
    
    def sliding_window_operations(self) -> List[Dict]:
        """Sliding window with real different problems."""
        examples = []
        
        # Fixed window maximum sum
        examples.append(self._create_example(
            "Encontre subarray de tamanho k com maior soma",
            "arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4",
            "soma = sum(arr[:k])\nmax_soma = soma\nfor i in range(k, len(arr)):\n    soma += arr[i] - arr[i-k]\n    max_soma = max(max_soma, soma)\nprint(max_soma)",
            "sliding-window-fixed",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre media maxima de subarray de tamanho k",
            "arr = [1, 12, -5, -6, 50, 3], k = 4",
            "soma = sum(arr[:k])\nmax_media = soma / k\nfor i in range(k, len(arr)):\n    soma += arr[i] - arr[i-k]\n    max_media = max(max_media, soma / k)\nprint(max_media)",
            "sliding-window-fixed",
            "medium"
        ))
        
        # Variable window - longest substring without repeating
        examples.append(self._create_example(
            "Encontre maior substring sem caracteres repetidos",
            "s = 'abcabcbb'",
            "vistos = set()\nesq = max_len = 0\nfor dir in range(len(s)):\n    while s[dir] in vistos:\n        vistos.remove(s[esq])\n        esq += 1\n    vistos.add(s[dir])\n    max_len = max(max_len, dir - esq + 1)\nprint(max_len)",
            "sliding-window-variable",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Encontre maior subarray com soma positiva",
            "arr = [1, -2, 3, 4, -1, 2, 1, -5, 4]",
            "esq = max_len = 0\nsoma = 0\nfor dir in range(len(arr)):\n    soma += arr[dir]\n    while soma <= 0 and esq <= dir:\n        soma -= arr[esq]\n        esq += 1\n    max_len = max(max_len, dir - esq + 1)\nprint(max_len)",
            "sliding-window-variable",
            "medium"
        ))
        
        # Count occurrences
        examples.append(self._create_example(
            "Conte ocorrencias de anagrama em string",
            "s = 'cbaebabacd', p = 'abc'",
            "from collections import Counter\ncontagem = 0\np_freq = Counter(p)\njanela = Counter(s[:len(p)-1])\nfor i in range(len(p)-1, len(s)):\n    janela[s[i]] += 1\n    if janela == p_freq:\n        contagem += 1\n    janela[s[i-len(p)+1]] -= 1\n    if janela[s[i-len(p)+1]] == 0:\n        del janela[s[i-len(p)+1]]\nprint(contagem)",
            "sliding-window-anagram",
            "hard"
        ))
        
        # Minimum window substring
        examples.append(self._create_example(
            "Encontre menor substring contendo todos os caracteres",
            "s = 'ADOBECODEBANC', t = 'ABC'",
            "from collections import Counter\nnecessario = Counter(t)\nesq = min_len = float('inf')\nmin_janela = ''\nformado = 0\nfor dir in range(len(s)):\n    if s[dir] in necessario:\n        necessario[s[dir]] -= 1\n        if necessario[s[dir]] >= 0:\n            formado += 1\n    while formado == len(t):\n        if dir - esq + 1 < min_len:\n            min_len = dir - esq + 1\n            min_janela = s[esq:dir+1]\n        if s[esq] in necessario:\n            necessario[s[esq]] += 1\n            if necessario[s[esq]] > 0:\n                formado -= 1\n        esq += 1\nprint(min_janela)",
            "sliding-window-minimum",
            "hard"
        ))
        
        return examples
    
    # ========== BINARY SEARCH - REAL VARIATIONS ==========
    
    def binary_search_operations(self) -> List[Dict]:
        """Binary search with real different scenarios."""
        examples = []
        
        # Classic binary search
        examples.append(self._create_example(
            "Encontre indice de elemento em array ordenado",
            "arr = [1, 3, 5, 7, 9, 11], alvo = 7",
            "esq, dir = 0, len(arr) - 1\nwhile esq <= dir:\n    meio = (esq + dir) // 2\n    if arr[meio] == alvo:\n        print(meio)\n        break\n    elif arr[meio] < alvo:\n        esq = meio + 1\n    else:\n        dir = meio - 1\nelse:\n    print(-1)",
            "binary-search-classic",
            "medium"
        ))
        
        # Lower bound
        examples.append(self._create_example(
            "Encontre primeira ocorrencia de elemento",
            "arr = [1, 2, 2, 2, 3, 4], alvo = 2",
            "esq, dir = 0, len(arr)\nwhile esq < dir:\n    meio = (esq + dir) // 2\n    if arr[meio] < alvo:\n        esq = meio + 1\n    else:\n        dir = meio\nprint(esq if esq < len(arr) and arr[esq] == alvo else -1)",
            "binary-search-lower-bound",
            "medium"
        ))
        
        # Upper bound
        examples.append(self._create_example(
            "Encontre ultima ocorrencia de elemento",
            "arr = [1, 2, 2, 2, 3, 4], alvo = 2",
            "esq, dir = 0, len(arr)\nwhile esq < dir:\n    meio = (esq + dir) // 2\n    if arr[meio] <= alvo:\n        esq = meio + 1\n    else:\n        dir = meio\npos = esq - 1\nprint(pos if pos >= 0 and arr[pos] == alvo else -1)",
            "binary-search-upper-bound",
            "medium"
        ))
        
        # Search in rotated array
        examples.append(self._create_example(
            "Busque em array ordenado rotacionado",
            "arr = [4, 5, 6, 7, 0, 1, 2], alvo = 0",
            "esq, dir = 0, len(arr) - 1\nwhile esq <= dir:\n    meio = (esq + dir) // 2\n    if arr[meio] == alvo:\n        print(meio)\n        break\n    if arr[esq] <= arr[meio]:\n        if arr[esq] <= alvo < arr[meio]:\n            dir = meio - 1\n        else:\n            esq = meio + 1\n    else:\n        if arr[meio] < alvo <= arr[dir]:\n            esq = meio + 1\n        else:\n            dir = meio - 1\nelse:\n    print(-1)",
            "binary-search-rotated",
            "hard"
        ))
        
        # Find peak element
        examples.append(self._create_example(
            "Encontre pico em array (maior que vizinhos)",
            "arr = [1, 2, 3, 1]",
            "esq, dir = 0, len(arr) - 1\nwhile esq < dir:\n    meio = (esq + dir) // 2\n    if arr[meio] > arr[meio + 1]:\n        dir = meio\n    else:\n        esq = meio + 1\nprint(esq)",
            "binary-search-peak",
            "medium"
        ))
        
        return examples
    
    # ========== STACK - REAL VARIATIONS ==========
    
    def stack_operations(self) -> List[Dict]:
        """Stack operations with real different scenarios."""
        examples = []
        
        # Valid parentheses
        examples.append(self._create_example(
            "Valide se expressao tem parenteses balanceados",
            "s = '()[]{}'",
            "pilha = []\npares = {')': '(', ']': '[', '}': '{'}\nfor char in s:\n    if char in '([{':\n        pilha.append(char)\n    elif char in ')]}':\n        if not pilha or pilha[-1] != pares[char]:\n            print(False)\n            break\n        pilha.pop()\nelse:\n    print(len(pilha) == 0)",
            "stack-parentheses",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Valide tags HTML aninhadas",
            "tags = ['<div>', '<p>', '</p>', '</div>']",
            "pilha = []\nfor tag in tags:\n    if tag[1] != '/':\n        pilha.append(tag)\n    else:\n        if not pilha or pilha[-1] != tag.replace('/', ''):\n            print(False)\n            break\n        pilha.pop()\nelse:\n    print(len(pilha) == 0)",
            "stack-parentheses",
            "medium"
        ))
        
        # Daily temperatures
        examples.append(self._create_example(
            "Calcule dias ate temperatura mais quente",
            "temperaturas = [73, 74, 75, 71, 69, 72, 76, 73]",
            "resposta = [0] * len(temperaturas)\npilha = []\nfor i, temp in enumerate(temperaturas):\n    while pilha and temperaturas[pilha[-1]] < temp:\n        idx = pilha.pop()\n        resposta[idx] = i - idx\n    pilha.append(i)\nprint(resposta)",
            "stack-monotonic",
            "medium"
        ))
        
        # Next greater element
        examples.append(self._create_example(
            "Encontre proximo elemento maior para cada posicao",
            "arr = [4, 5, 2, 10, 8]",
            "resposta = [-1] * len(arr)\npilha = []\nfor i in range(len(arr)):\n    while pilha and arr[pilha[-1]] < arr[i]:\n        idx = pilha.pop()\n        resposta[idx] = arr[i]\n    pilha.append(i)\nprint(resposta)",
            "stack-monotonic",
            "medium"
        ))
        
        # Evaluate RPN
        examples.append(self._create_example(
            "Avalie expressao em notacao polonesa reversa",
            "tokens = ['2', '1', '+', '3', '*']",
            "pilha = []\nfor token in tokens:\n    if token in '+-*/':\n        b = pilha.pop()\n        a = pilha.pop()\n        if token == '+':\n            pilha.append(a + b)\n        elif token == '-':\n            pilha.append(a - b)\n        elif token == '*':\n            pilha.append(a * b)\n        else:\n            pilha.append(int(a / b))\n    else:\n        pilha.append(int(token))\nprint(pilha[0])",
            "stack-evaluation",
            "medium"
        ))
        
        return examples
    
    # ========== TREES - REAL VARIATIONS ==========
    
    def tree_operations(self) -> List[Dict]:
        """Tree operations with real different scenarios."""
        examples = []
        
        # DFS traversals
        examples.append(self._create_example(
            "Percorra arvore em ordem (in-order) DFS",
            "raiz = no_arvore",
            "def in_order(no):\n    if no:\n        in_order(no.esquerda)\n        print(no.val)\n        in_order(no.direita)\nin_order(raiz)",
            "tree-dfs",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Percorra arvore em pre-ordem DFS",
            "raiz = no_arvore",
            "def pre_order(no):\n    if no:\n        print(no.val)\n        pre_order(no.esquerda)\n        pre_order(no.direita)\npre_order(raiz)",
            "tree-dfs",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Percorra arvore em pos-ordem DFS",
            "raiz = no_arvore",
            "def post_order(no):\n    if no:\n        post_order(no.esquerda)\n        post_order(no.direita)\n        print(no.val)\npost_order(raiz)",
            "tree-dfs",
            "medium"
        ))
        
        # BFS level order
        examples.append(self._create_example(
            "Percorra arvore por niveis (BFS)",
            "raiz = no_arvore",
            "from collections import deque\nfila = deque([raiz])\nwhile fila:\n    no = fila.popleft()\n    print(no.val)\n    if no.esquerda:\n        fila.append(no.esquerda)\n    if no.direita:\n        fila.append(no.direita)",
            "tree-bfs",
            "medium"
        ))
        
        examples.append(self._create_example(
            "Percorra arvore por niveis separados",
            "raiz = no_arvore",
            "from collections import deque\nfila = deque([raiz])\nwhile fila:\n    nivel = []\n    for _ in range(len(fila)):\n        no = fila.popleft()\n        nivel.append(no.val)\n        if no.esquerda:\n            fila.append(no.esquerda)\n        if no.direita:\n            fila.append(no.direita)\n    print(nivel)",
            "tree-bfs-levels",
            "medium"
        ))
        
        # Tree depth
        examples.append(self._create_example(
            "Calcule profundidade maxima da arvore",
            "raiz = no_arvore",
            "def profundidade(no):\n    if not no:\n        return 0\n    return 1 + max(profundidade(no.esquerda), profundidade(no.direita))\nprint(profundidade(raiz))",
            "tree-depth",
            "easy"
        ))
        
        # Check balanced
        examples.append(self._create_example(
            "Verifique se arvore esta balanceada",
            "raiz = no_arvore",
            "def altura(no):\n    if not no:\n        return 0\n    esq = altura(no.esquerda)\n    dir = altura(no.direita)\n    if abs(esq - dir) > 1 or esq == -1 or dir == -1:\n        return -1\n    return 1 + max(esq, dir)\nprint(altura(raiz) != -1)",
            "tree-balanced",
            "medium"
        ))
        
        return examples
    
    # ========== LINKED LIST - REAL VARIATIONS ==========
    
    def linked_list_operations(self) -> List[Dict]:
        """Linked list operations with real different scenarios."""
        examples = []
        
        # Reverse
        examples.append(self._create_example(
            "Inverta lista ligada iterativamente",
            "cabeca = no_inicial",
            "anterior = None\natual = cabeca\nwhile atual:\n    proximo = atual.proximo\n    atual.proximo = anterior\n    anterior = atual\n    atual = proximo\ncabeca = anterior",
            "linked-list-reverse",
            "medium"
        ))
        
        # Find middle
        examples.append(self._create_example(
            "Encontre elemento do meio da lista",
            "cabeca = no_inicial",
            "lento = rapido = cabeca\nwhile rapido and rapido.proximo:\n    lento = lento.proximo\n    rapido = rapido.proximo.proximo\nprint(lento.val)",
            "linked-list-middle",
            "medium"
        ))
        
        # Detect cycle
        examples.append(self._create_example(
            "Detecte ciclo em lista ligada",
            "cabeca = no_inicial",
            "lento = rapido = cabeca\ntem_ciclo = False\nwhile rapido and rapido.proximo:\n    lento = lento.proximo\n    rapido = rapido.proximo.proximo\n    if lento == rapido:\n        tem_ciclo = True\n        break\nprint(tem_ciclo)",
            "linked-list-cycle",
            "medium"
        ))
        
        # Merge two sorted
        examples.append(self._create_example(
            "Mescle duas listas ligadas ordenadas",
            "l1 = lista1, l2 = lista2",
            "dummy = No(0)\natual = dummy\nwhile l1 and l2:\n    if l1.val <= l2.val:\n        atual.proximo = l1\n        l1 = l1.proximo\n    else:\n        atual.proximo = l2\n        l2 = l2.proximo\n    atual = atual.proximo\natual.proximo = l1 or l2",
            "linked-list-merge",
            "medium"
        ))
        
        # Remove nth from end
        examples.append(self._create_example(
            "Remova n-esimo elemento do fim da lista",
            "cabeca = no_inicial, n = 2",
            "dummy = No(0)\ndummy.proximo = cabeca\natras = frente = dummy\nfor _ in range(n + 1):\n    frente = frente.proximo\nwhile frente:\n    atras = atras.proximo\n    frente = frente.proximo\natras.proximo = atras.proximo.proximo",
            "linked-list-remove",
            "medium"
        ))
        
        return examples
    
    # ========== GENERATE ALL ==========
    
    def generate_all(self) -> List[Dict]:
        """Generate all high-quality examples."""
        all_examples = []
        
        print("🔧 Generating high-quality DSA operations with REAL variations...")
        
        print("  - Hash map operations...")
        all_examples.extend(self.hash_map_operations())
        
        print("  - Two pointers operations...")
        all_examples.extend(self.two_pointers_operations())
        
        print("  - Sliding window operations...")
        all_examples.extend(self.sliding_window_operations())
        
        print("  - Binary search operations...")
        all_examples.extend(self.binary_search_operations())
        
        print("  - Stack operations...")
        all_examples.extend(self.stack_operations())
        
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
    
    print(f"\n✅ Saved {len(examples)} high-quality examples to {filepath}")
    
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
    generator = QualityDSAOperations()
    examples = generator.generate_all()
    
    save_dataset(examples, "high_quality_dsa_operations.jsonl")
    
    print("\n🎯 Dataset characteristics:")
    print("  • NO 'variacao N' - each example is unique")
    print("  • Real different contexts and scenarios")
    print("  • Slightly different code for each use case")
    print("  • Focus on practical, useful operations")
    print("  • Portuguese instructions")
    print("  • Python 3.13 compatible")
    print("  • Output: PURE CODE (no comments)")


if __name__ == "__main__":
    main()
