#!/usr/bin/env python3
"""
Inference script for testing fine-tuned models.
"""

import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def parse_args():
    parser = argparse.ArgumentParser(description="Test fine-tuned model")
    parser.add_argument("--model_path", type=str, required=True, help="Path to fine-tuned model")
    parser.add_argument("--prompt", type=str, default=None, help="Prompt for generation")
    parser.add_argument("--max_tokens", type=int, default=200, help="Maximum tokens to generate")
    parser.add_argument("--temperature", type=float, default=0.2, help="Sampling temperature")
    parser.add_argument("--interactive", action="store_true", help="Interactive mode")
    return parser.parse_args()


def load_model(model_path: str):
    """Load model and tokenizer."""
    print(f"📥 Loading model from {model_path}...")
    
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    model.eval()
    
    return model, tokenizer


def generate(model, tokenizer, prompt: str, max_tokens: int = 200, temperature: float = 0.2):
    """Generate text from prompt."""
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=max_tokens,
            temperature=temperature,
            do_sample=temperature > 0,
            top_p=0.95,
            pad_token_id=tokenizer.eos_token_id,
        )
    
    generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return generated_text


def format_code_prompt(instruction: str, input_text: str = "") -> str:
    """Format prompt in Alpaca style."""
    if input_text:
        return f"### Instrução:\n{instruction}\n\n### Entrada:\n{input_text}\n\n### Resposta:\n"
    else:
        return f"### Instrução:\n{instruction}\n\n### Resposta:\n"


def interactive_mode(model, tokenizer, max_tokens: int, temperature: float):
    """Run interactive inference loop."""
    print("\n🤖 Interactive Mode")
    print("Type your instruction (or 'quit' to exit):\n")
    
    while True:
        try:
            instruction = input("Instrução: ").strip()
            
            if instruction.lower() in ["quit", "exit", "q"]:
                print("👋 Goodbye!")
                break
            
            if not instruction:
                continue
            
            prompt = format_code_prompt(instruction)
            print("\n📝 Generating...\n")
            
            result = generate(model, tokenizer, prompt, max_tokens, temperature)
            
            # Extract only the generated part (after the prompt)
            generated = result[len(prompt):].strip()
            print("🎯 Resposta:")
            print("-" * 50)
            print(generated)
            print("-" * 50)
            print()
            
        except KeyboardInterrupt:
            print("\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")


def main():
    args = parse_args()
    
    # Load model
    model, tokenizer = load_model(args.model_path)
    
    if args.interactive:
        interactive_mode(model, tokenizer, args.max_tokens, args.temperature)
    elif args.prompt:
        # Single prompt mode
        prompt = format_code_prompt(args.prompt)
        print(f"\n📝 Prompt:\n{prompt}")
        print("\n🤖 Generating...\n")
        
        result = generate(model, tokenizer, prompt, args.max_tokens, args.temperature)
        
        # Extract only the generated part
        generated = result[len(prompt):].strip()
        print("🎯 Resposta:")
        print("-" * 50)
        print(generated)
        print("-" * 50)
    else:
        # Demo mode with example prompts
        print("\n🎯 Running demo with example prompts:\n")
        
        examples = [
            "Escreva uma função em Python para calcular o fatorial de um número",
            "Implemente uma busca binária",
            "Crie uma classe Pilha (Stack)",
            "Escreva uma função para verificar se um número é primo",
        ]
        
        for i, instruction in enumerate(examples, 1):
            print(f"\n--- Example {i} ---")
            print(f"Instrução: {instruction}")
            
            prompt = format_code_prompt(instruction)
            result = generate(model, tokenizer, prompt, args.max_tokens, args.temperature)
            
            generated = result[len(prompt):].strip()
            print(f"\nResposta:\n{generated[:300]}...")
            print()


if __name__ == "__main__":
    main()
