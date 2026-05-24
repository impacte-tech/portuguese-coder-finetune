#!/usr/bin/env python3
"""
Utility to generate synthetic training data for Portuguese code fine-tuning.
"""

import json
import random
from typing import List, Dict


class DatasetGenerator:
    """Generate synthetic code training data in Portuguese."""
    
    def __init__(self):
        self.templates = {
            "python": self._python_templates(),
            "javascript": self._javascript_templates(),
            "java": self._java_templates(),
        }
    
    def _python_templates(self) -> List[Dict]:
        return [
            {
                "instruction": "Escreva uma função em Python para {task}",
                "tasks": [
                    "calcular o MDC (máximo divisor comum)",
                    "calcular o MMC (mínimo múltiplo comum)",
                    "converter decimal para binário",
                    "encontrar o segundo maior elemento de um array",
                    "remover duplicatas de um array",
                    "rotacionar um array para a direita",
                    "encontrar o elemento que aparece mais vezes",
                    "verificar se duas strings são anagramas",
                    "contar o número de vogais em uma string",
                    "inverter as palavras de uma frase",
                ]
            },
            {
                "instruction": "Crie uma classe em Python que implemente {data_structure}",
                "tasks": [
                    "uma fila (queue)",
                    "uma lista ligada (linked list)",
                    "um dicionário/hash map",
                    "uma árvore binária de busca",
                    "um grafo usando lista de adjacência",
                    "um cache LRU",
                    "um conjunto (set)",
                ]
            },
        ]
    
    def _javascript_templates(self) -> List[Dict]:
        return [
            {
                "instruction": "Escreva uma função em JavaScript para {task}",
                "tasks": [
                    "filtrar números pares de um array",
                    "mapear um array para seus quadrados",
                    "reduzir um array para a soma dos elementos",
                    "implementar debounce",
                    "implementar throttle",
                    "criar uma Promise a partir de um callback",
                    "fazer uma requisição fetch com retry",
                    "agrupar elementos de um array por propriedade",
                ]
            },
        ]
    
    def _java_templates(self) -> List[Dict]:
        return [
            {
                "instruction": "Implemente uma classe Java para {task}",
                "tasks": [
                    "representar um estudante com nome e notas",
                    "implementar uma calculadora com operações básicas",
                    "criar um sistema de biblioteca simples",
                    "representar uma conta bancária",
                    "implementar um carrinho de compras",
                ]
            },
        ]
    
    def generate_instruction(self, language: str) -> Dict:
        """Generate a single instruction-output pair."""
        templates = self.templates.get(language, self.templates["python"])
        template = random.choice(templates)
        task = random.choice(template["tasks"])
        
        instruction = template["instruction"].format(task=task)
        
        return {
            "instruction": instruction,
            "input": "",
            "output": f"# TODO: Implement solution for: {task}\n# Language: {language}"
        }
    
    def generate_dataset(self, language: str, num_examples: int) -> List[Dict]:
        """Generate a dataset of specified size."""
        dataset = []
        for _ in range(num_examples):
            example = self.generate_instruction(language)
            dataset.append(example)
        return dataset
    
    def save_dataset(self, dataset: List[Dict], filepath: str):
        """Save dataset to JSONL file."""
        with open(filepath, 'w', encoding='utf-8') as f:
            for example in dataset:
                f.write(json.dumps(example, ensure_ascii=False) + '\n')
        print(f"✅ Saved {len(dataset)} examples to {filepath}")


def main():
    generator = DatasetGenerator()
    
    # Generate datasets for different languages
    languages = ["python", "javascript", "java"]
    
    for lang in languages:
        print(f"\n📝 Generating {lang} dataset...")
        dataset = generator.generate_dataset(lang, num_examples=50)
        generator.save_dataset(dataset, f"data/generated_{lang}_data.jsonl")
    
    # Generate mixed dataset
    print("\n📝 Generating mixed language dataset...")
    mixed_dataset = []
    for lang in languages:
        mixed_dataset.extend(generator.generate_dataset(lang, num_examples=30))
    
    random.shuffle(mixed_dataset)
    generator.save_dataset(mixed_dataset, "data/generated_mixed_data.jsonl")
    
    print("\n✅ All datasets generated successfully!")
    print("\nNext steps:")
    print("   1. Review and edit the generated files in data/")
    print("   2. Add actual code implementations to the 'output' fields")
    print("   3. Combine with sample_data.jsonl for training")


if __name__ == "__main__":
    main()
