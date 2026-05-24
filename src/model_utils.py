#!/usr/bin/env python3
"""
Model loading and utility functions.
"""

import torch
from unsloth import FastLanguageModel
from transformers import AutoModelForCausalLM, AutoTokenizer


def load_base_model(model_name: str = "Qwen/Qwen2.5-Coder-0.5B-Instruct", max_seq_length: int = 2048):
    """Load base model with Unsloth optimizations."""
    model, tokenizer = FastLanguageModel.from_pretrained(
        model_name=model_name,
        max_seq_length=max_seq_length,
        dtype=torch.bfloat16 if torch.cuda.is_bf16_supported() else torch.float16,
        load_in_4bit=True,
    )
    return model, tokenizer


def load_finetuned_model(model_path: str, max_seq_length: int = 2048):
    """Load fine-tuned model for inference."""
    tokenizer = AutoTokenizer.from_pretrained(model_path)
    model = AutoModelForCausalLM.from_pretrained(
        model_path,
        torch_dtype=torch.float16,
        device_map="auto",
    )
    return model, tokenizer


def get_model_info(model_name: str):
    """Get information about a model."""
    info = {
        "Qwen/Qwen2.5-Coder-0.5B-Instruct": {
            "parameters": "0.5B",
            "context_length": 32768,
            "languages": ["en", "zh", "multilingual"],
            "task": "code-generation",
            "license": "Apache-2.0",
        },
        "Qwen/Qwen2.5-Coder-1.5B-Instruct": {
            "parameters": "1.5B",
            "context_length": 32768,
            "languages": ["en", "zh", "multilingual"],
            "task": "code-generation",
            "license": "Apache-2.0",
        },
    }
    return info.get(model_name, {"parameters": "unknown"})


def estimate_memory_usage(model_name: str, batch_size: int = 1, seq_length: int = 2048):
    """Estimate VRAM usage for training/inference."""
    # Rough estimates for 4-bit quantized models
    base_memory = {
        "0.5B": 0.5,  # GB
        "1.5B": 1.2,
        "3B": 2.0,
        "7B": 4.0,
    }
    
    # Extract parameter count from model name
    params = "0.5B"  # default
    for key in base_memory:
        if key in model_name:
            params = key
            break
    
    base = base_memory.get(params, 1.0)
    activation_memory = (batch_size * seq_length * 4) / (1024 ** 3)  # ~4 bytes per token
    
    return {
        "model_weights": base,
        "activations": activation_memory,
        "total_estimate": base + activation_memory + 0.5,  # +0.5 for overhead
    }
