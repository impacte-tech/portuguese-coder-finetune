// Blind 75 Fundamentals - Portuguese
const blind75Questions = [
    {
        id: 1,
        title: "Two Sum - Par de Números",
        category: "array",
        difficulty: "Fácil",
        description: "Verifique se existe um par de números em um array que somam a um valor alvo usando hash map.",
        example: "arr = [2, 7, 11, 15], alvo = 9\nSaída: [0, 1] (porque 2 + 7 = 9)",
        hints: ["Use um hash map para armazenar valores vistos", "Para cada número, calcule o complemento (alvo - num)"],
        testCases: [
            { input: "tem_par_soma([2, 7, 11, 15], 9)", expected: "[0, 1]" },
            { input: "tem_par_soma([3, 2, 4], 6)", expected: "[1, 2]" },
            { input: "tem_par_soma([3, 3], 6)", expected: "[0, 1]" }
        ]
    },
    {
        id: 2,
        title: "Contador de Frequência",
        category: "array",
        difficulty: "Fácil",
        description: "Conte a frequência de cada elemento em um array usando Counter.",
        example: "arr = [1, 2, 2, 3, 3, 3]\nSaída: {1: 1, 2: 2, 3: 3}",
        hints: ["Use collections.Counter", "Converta para dict se necessário"],
        testCases: [
            { input: "contar_frequencia([1, 2, 2, 3, 3, 3])", expected: "{1: 1, 2: 2, 3: 3}" },
            { input: "contar_frequencia(['a', 'b', 'a'])", expected: "{'a': 2, 'b': 1}" }
        ]
    },
    {
        id: 3,
        title: "Soma de Janela Deslizante",
        category: "array",
        difficulty: "Médio",
        description: "Calcule a soma de todas as subarrays de tamanho k usando janela deslizante.",
        example: "arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4\nSaída: [17, 39, 37, 27, 24]",
        hints: ["Calcule a soma inicial dos primeiros k elementos", "Deslize: subtrai o elemento que sai, adiciona o que entra"],
        testCases: [
            { input: "soma_janela_deslizante([1, 4, 2, 10, 23, 3, 1, 0, 20], 4)", expected: "[17, 39, 37, 27, 24]" }
        ]
    },
    {
        id: 4,
        title: "Dois Ponteiros - Soma",
        category: "array",
        difficulty: "Médio",
        description: "Encontre dois números em array ordenado que somam ao alvo usando dois ponteiros.",
        example: "arr = [2, 7, 11, 15], alvo = 9\nSaída: [0, 1]",
        hints: ["Um ponteiro no início, outro no final", "Se soma < alvo, mova esquerda; se >, mova direita"],
        testCases: [
            { input: "dois_numeros_soma([2, 7, 11, 15], 9)", expected: "[0, 1]" },
            { input: "dois_numeros_soma([1, 3, 4, 8], 7)", expected: "[1, 2]" }
        ]
    },
    {
        id: 5,
        title: "Implementar Pilha (Stack)",
        category: "stack",
        difficulty: "Fácil",
        description: "Implemente uma pilha (stack) com operações push, pop, peek e is_empty.",
        example: "Operações: push(10), push(20), pop(), peek()\nSaída: 20, depois 10",
        hints: ["Use uma lista Python", "append() para push, pop() para pop", "O último elemento é o topo"],
        testCases: [
            { input: "p = Pilha(); p.push(10); p.push(20); print(p.pop())", expected: "20" },
            { input: "p = Pilha(); p.push(5); print(p.peek())", expected: "5" }
        ]
    },
    {
        id: 6,
        title: "Busca Binária",
        category: "array",
        difficulty: "Fácil",
        description: "Implemente busca binária para encontrar índice de elemento em array ordenado.",
        example: "arr = [1, 3, 5, 7, 9, 11, 13], alvo = 7\nSaída: 3",
        hints: ["Calcule o meio: (esquerda + direita) // 2", "Compare com alvo e descarte metade"],
        testCases: [
            { input: "busca_binaria([1, 3, 5, 7, 9, 11, 13], 7)", expected: "3" },
            { input: "busca_binaria([1, 3, 5, 7], 4)", expected: "-1" }
        ]
    },
    {
        id: 7,
        title: "Reverter Lista Ligada",
        category: "linkedlist",
        difficulty: "Médio",
        description: "Inverta uma lista ligada iterativamente.",
        example: "Lista: 1 -> 2 -> 3 -> 4 -> None\nSaída: 4 -> 3 -> 2 -> 1 -> None",
        hints: ["Use três ponteiros: anterior, atual, próximo", "Inverte os ponteiros um por um"],
        testCases: [
            { input: "reverter_lista(No(1, No(2, No(3))))", expected: "Cabeça com val=3" }
        ]
    },
    {
        id: 8,
        title: "Percurso Em-Ordem (In-Order)",
        category: "tree",
        difficulty: "Fácil",
        description: "Implemente percurso em ordem (in-order) em árvore binária.",
        example: "Árvore:    1\n          / \\\n         2   3\n        / \\\n       4   5\nSaída: [4, 2, 5, 1, 3]",
        hints: ["Esquerda -> Raiz -> Direita", "Use recursão ou pilha"],
        testCases: [
            { input: "percurso_em_ordem(raiz)", expected: "[4, 2, 5, 1, 3]" }
        ]
    },
    {
        id: 9,
        title: "Fibonacci com Memoização",
        category: "dp",
        difficulty: "Fácil",
        description: "Calcule Fibonacci com memoização (top-down).",
        example: "n = 10\nSaída: 55",
        hints: ["Use @lru_cache ou dicionário", "Armazene resultados já calculados"],
        testCases: [
            { input: "fibonacci(10)", expected: "55" },
            { input: "fibonacci(20)", expected: "6765" }
        ]
    },
    {
        id: 10,
        title: "Fibonacci com Tabulação",
        category: "dp",
        difficulty: "Fácil",
        description: "Calcule Fibonacci com tabulação (bottom-up, iterativo).",
        example: "n = 10\nSaída: 55",
        hints: ["Use apenas duas variáveis para O(1) espaço", "Itere de 2 até n"],
        testCases: [
            { input: "fibonacci_tabulacao(10)", expected: "55" },
            { input: "fibonacci_tabulacao(50)", expected: "12586269025" }
        ]
    }
];

// Export for use in app.js
if (typeof module !== 'undefined' && module.exports) {
    module.exports = blind75Questions;
}
