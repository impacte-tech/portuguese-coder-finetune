#!/usr/bin/env python3
"""
Export fine-tuned model to ONNX format for use with transformers.js.
"""

import os
import argparse
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer


def parse_args():
    parser = argparse.ArgumentParser(description="Export model to ONNX for transformers.js")
    parser.add_argument("--model_path", type=str, required=True, help="Path to fine-tuned model")
    parser.add_argument("--output_dir", type=str, default="./onnx_model", help="Output directory for ONNX model")
    parser.add_argument("--task", type=str, default="text-generation", help="ONNX task type")
    return parser.parse_args()


def export_with_optimum(model_path, output_dir, task):
    """Export using Optimum CLI."""
    import subprocess
    
    cmd = [
        "optimum-cli", "export", "onnx",
        "--model", model_path,
        "--task", task,
        output_dir
    ]
    
    print(f"Running: {' '.join(cmd)}")
    subprocess.run(cmd, check=True)


def export_manual(model_path, output_dir):
    """Manual export with torch.onnx."""
    print("Loading model and tokenizer...")
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="cpu"
    )
    model.eval()
    
    # Create dummy input
    dummy_input = tokenizer("This is a test", return_tensors="pt")
    
    # Export
    os.makedirs(output_dir, exist_ok=True)
    onnx_path = os.path.join(output_dir, "model.onnx")
    
    print(f"Exporting to {onnx_path}...")
    torch.onnx.export(
        model,
        (dummy_input["input_ids"],),
        onnx_path,
        input_names=["input_ids"],
        output_names=["logits"],
        dynamic_axes={
            "input_ids": {0: "batch_size", 1: "sequence"},
            "logits": {0: "batch_size", 1: "sequence"},
        },
        opset_version=14,
    )
    
    # Save tokenizer
    tokenizer.save_pretrained(output_dir)
    print(f"✅ Export complete! Model saved to {output_dir}")


def main():
    args = parse_args()
    
    print(f"🔄 Exporting model to ONNX format")
    print(f"   Model path: {args.model_path}")
    print(f"   Output directory: {args.output_dir}")
    
    try:
        # Try optimum first
        export_with_optimum(args.model_path, args.output_dir, args.task)
    except Exception as e:
        print(f"Optimum export failed: {e}")
        print("Falling back to manual export...")
        export_manual(args.model_path, args.output_dir)
    
    print(f"\n✅ Export complete!")
    print(f"\nTo use with transformers.js:")
    print(f"   1. Upload the '{args.output_dir}' folder to Hugging Face or your server")
    print(f"   2. Use with: pipeline('text-generation', 'path/to/{args.output_dir}')")


if __name__ == "__main__":
    main()
