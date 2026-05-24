# 🇧🇷 Portuguese Code Assistant - Fine-tuning with Unsloth

This repository contains a complete setup for fine-tuning the **Qwen2.5-Coder-0.5B** model for Portuguese-speaking software engineering students working on LeetCode-style problems.

## 🎯 Purpose

Fine-tune a small (<2B) code model that:
- Runs offline via **transformers.js**
- Understands **Portuguese** instructions
- Specializes in a specific **programming language**
- Helps with **LeetCode-style algorithmic problems**

## 📁 Repository Structure

```
.
├── README.md                      # This file
├── requirements.txt               # Python dependencies
├── config.yaml                    # Axolotl configuration (alternative)
├── train.py                       # Main Unsloth training script
├── export_onnx.py                 # Export to ONNX for transformers.js
├── data/
│   ├── sample_data.jsonl          # Example training data
│   └── generate_dataset.py        # Dataset generation utilities
├── src/
│   ├── model_utils.py             # Model loading utilities
│   ├── data_utils.py              # Data processing utilities
│   └── inference.py               # Test inference script
└── notebooks/
    └── explore_model.ipynb        # Jupyter notebook for exploration
```

## 🚀 Quick Start

### 1. Installation

```bash
# Clone the repository
git clone <your-repo-url>
cd portuguese-coder-finetune

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Prepare Your Dataset

Edit `data/sample_data.jsonl` with your Portuguese code examples:

```jsonl
{"instruction": "Escreva uma função em Python para inverter uma string", "input": "", "output": "def inverter_string(s):\n    return s[::-1]"}
{"instruction": "Implemente uma busca binária", "input": "Array ordenado: [1, 3, 5, 7, 9]\nAlvo: 5", "output": "def busca_binaria(arr, alvo):\n    esq, dir = 0, len(arr) - 1\n    while esq <= dir:\n        meio = (esq + dir) // 2\n        if arr[meio] == alvo:\n            return meio\n        elif arr[meio] < alvo:\n            esq = meio + 1\n        else:\n            dir = meio - 1\n    return -1"}
```

### 3. Train the Model

```bash
# Basic training
python train.py --data_path data/sample_data.jsonl --output_dir ./model_output

# With custom settings
python train.py \
    --data_path data/sample_data.jsonl \
    --output_dir ./model_output \
    --num_epochs 3 \
    --learning_rate 2e-4 \
    --batch_size 2
```

### 4. Export to ONNX (for transformers.js)

```bash
python export_onnx.py --model_path ./model_output --output_dir ./onnx_model
```

## 📊 Hardware Requirements

| GPU | VRAM | Training Time (1k examples) |
|-----|------|----------------------------|
| RTX 4090 | ~6GB | ~10 minutes |
| RTX 3060 | ~6GB | ~20 minutes |
| Colab T4 | ~8GB | ~30 minutes |
| CPU only | ~16GB RAM | ~2 hours |

## 🛠️ Customization

### Change Programming Language

Edit the dataset to focus on your target language:

**For JavaScript:**
```jsonl
{"instruction": "Crie uma função para ordenar um array", "input": "", "output": "function ordenarArray(arr) {\n    return arr.sort((a, b) => a - b);\n}"}
```

**For Java:**
```jsonl
{"instruction": "Implemente uma classe Pilha (Stack)", "input": "", "output": "public class Pilha<T> {\n    private List<T> elementos = new ArrayList<>();\n    \n    public void push(T item) {\n        elementos.add(item);\n    }\n    \n    public T pop() {\n        if (estaVazia()) throw new EmptyStackException();\n        return elementos.remove(elementos.size() - 1);\n    }\n    \n    public boolean estaVazia() {\n        return elementos.isEmpty();\n    }\n}"}
```

### Adjust Training Parameters

Edit `train.py` or use command-line arguments:

```bash
python train.py \
    --data_path data/sample_data.jsonl \
    --output_dir ./model_output \
    --model_name Qwen/Qwen2.5-Coder-0.5B-Instruct \
    --max_seq_length 2048 \
    --batch_size 2 \
    --gradient_accumulation_steps 4 \
    --num_epochs 3 \
    --learning_rate 2e-4 \
    --lora_r 16 \
    --lora_alpha 16
```

## 📚 Dataset Format

The training data uses **Alpaca format**:

```json
{
  "instruction": "Descrição do que fazer (em Português)",
  "input": "Contexto adicional (opcional)",
  "output": "Código ou resposta esperada"
}
```

### Recommended Dataset Size

- **Minimum**: 500 examples
- **Good**: 2,000-5,000 examples
- **Excellent**: 10,000+ examples

## 🧪 Testing the Model

```bash
# Run inference test
python src/inference.py --model_path ./model_output --prompt "Escreva uma função para calcular fatorial"
```

## 🌐 Using with transformers.js

After exporting to ONNX:

```javascript
import { pipeline } from '@xenova/transformers';

const generator = await pipeline('text-generation', './onnx_model', {
  dtype: 'q4',
});

const prompt = `### Instrução:
Escreva uma função em Python para verificar se um número é primo

### Resposta:
`;

const result = await generator(prompt, {
  max_new_tokens: 100,
  temperature: 0.2,
});

console.log(result[0].generated_text);
```

## 🔧 Troubleshooting

### Out of Memory
- Reduce `batch_size` to 1
- Reduce `max_seq_length` to 1024
- Use `load_in_4bit: true` (already enabled by default)

### Poor Results
- Increase dataset size
- Train for more epochs
- Adjust `learning_rate` (try 1e-4 to 5e-4)
- Check data quality

### Slow Training
- Enable `use_gradient_checkpointing`
- Use a GPU if available
- Reduce `max_seq_length`

## 📖 Resources

- [Unsloth Documentation](https://docs.unsloth.ai/)
- [transformers.js Documentation](https://huggingface.co/docs/transformers.js/)
- [Qwen2.5-Coder Model Card](https://huggingface.co/Qwen/Qwen2.5-Coder-0.5B-Instruct)

## 🤝 Contributing

Feel free to open issues or submit PRs with improvements!

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

**Note**: The base model (Qwen2.5-Coder-0.5B-Instruct) is licensed under Apache 2.0.
