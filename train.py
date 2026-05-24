#!/usr/bin/env python3
"""
Main training script for fine-tuning Qwen2.5-Coder-0.5B with Unsloth.
Optimized for Portuguese code generation tasks.
"""

import os
import argparse
import torch
from unsloth import FastLanguageModel
from trl import SFTTrainer
from transformers import TrainingArguments
from datasets import load_dataset


def parse_args():
    parser = argparse.ArgumentParser(description="Fine-tune Qwen2.5-Coder-0.5B for Portuguese code generation")
    parser.add_argument("--data_path", type=str, required=True, help="Path to training data JSONL file")
    parser.add_argument("--output_dir", type=str, default="./model_output", help="Output directory for trained model")
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen2.5-Coder-0.5B-Instruct", help="Base model name")
    parser.add_argument("--max_seq_length", type=int, default=2048, help="Maximum sequence length")
    parser.add_argument("--batch_size", type=int, default=2, help="Training batch size per device")
    parser.add_argument("--gradient_accumulation_steps", type=int, default=4, help="Gradient accumulation steps")
    parser.add_argument("--num_epochs", type=int, default=3, help="Number of training epochs")
    parser.add_argument("--learning_rate", type=float, default=2e-4, help="Learning rate")
    parser.add_argument("--lora_r", type=int, default=16, help="LoRA rank")
    parser.add_argument("--lora_alpha", type=int, default=16, help="LoRA alpha")
    parser.add_argument("--seed", type=int, default=3407, help="Random seed")
    return parser.parse_args()


def format_prompt(example):
    """Format example into training prompt."""
    instruction = example.get("instruction", "")
    input_text = example.get("input", "")
    output = example.get("output", "")
    
    if input_text and input_text.strip():
        prompt = f"### Instrução:\n{instruction}\n\n### Entrada:\n{input_text}\n\n### Resposta:\n{output}"
    else:
        prompt = f"### Instrução:\n{instruction}\n\n### Resposta:\n{output}"
    
    return {"text": prompt}


def main():
    args = parse_args()
    
    print(f"🚀 Starting fine-tuning with Unsloth")
    print(f"   Base model: {args.model_name}")
    print(f"   Data path: {args.data_path}")
    print(f"   Output directory: {args.output_dir}")
    
    # Create output directory
    os.makedirs(args.output_dir, exist_ok=True)
    
    # Load model with Unsloth optimizations
    print("\n📥 Loading model...")
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=args.model_name,
        max_seq_length=args.max_seq_length,
        dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
        load_in_4bit=True,
    )
    
    # Add LoRA adapters
    print("🔧 Adding LoRA adapters...")
    model = FastLanguageModel.get_peft_model(
        model,
        r=args.lora_r,
        target_modules=[
            "q_proj", "k_proj", "v_proj", "o_proj",
            "gate_proj", "up_proj", "down_proj",
        ],
        lora_alpha=args.lora_alpha,
        lora_dropout=0,
        bias="none",
        use_gradient_checkpointing="unsloth",
        random_state=args.seed,
    )
    
    # Load and prepare dataset
    print(f"\n📊 Loading dataset from {args.data_path}...")
    dataset = load_dataset("json", data_files=args.data_path, split="train")
    print(f"   Loaded {len(dataset)} examples")
    
    # Format dataset
    dataset = dataset.map(format_prompt)
    
    # Set up training arguments
    training_args = TrainingArguments(
        per_device_train_batch_size=args.batch_size,
        gradient_accumulation_steps=args.gradient_accumulation_steps,
        warmup_steps=5,
        num_train_epochs=args.num_epochs,
        learning_rate=args.learning_rate,
        fp16=not torch.cuda.is_bf16_supported(),
        bf16=torch.cuda.is_bf16_supported(),
        logging_steps=1,
        optim="adamw_8bit",
        weight_decay=0.01,
        lr_scheduler_type="linear",
        seed=args.seed,
        output_dir=args.output_dir,
        save_strategy="epoch",
        save_total_limit=2,
    )
    
    # Initialize trainer
    print("\n🏋️  Initializing trainer...")
    trainer = SFTTrainer(
        model=model,
        tokenizer=tokenizer,
        train_dataset=dataset,
        dataset_text_field="text",
        max_seq_length=args.max_seq_length,
        args=training_args,
    )
    
    # Train
    print("\n🎯 Starting training...")
    trainer.train()
    
    # Save model
    print(f"\n💾 Saving model to {args.output_dir}...")
    model.save_pretrained_merged(
        args.output_dir,
        tokenizer,
        save_method="merged_16bit",
    )
    
    print(f"\n✅ Training complete! Model saved to {args.output_dir}")
    print(f"\nNext steps:")
    print(f"   1. Test the model: python src/inference.py --model_path {args.output_dir}")
    print(f"   2. Export to ONNX: python export_onnx.py --model_path {args.output_dir}")


if __name__ == "__main__":
    main()
