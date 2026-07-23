---
language:
- en
license: apache-2.0
tags:
- text-generation
- gguf
- creative-writing
- storytelling
- roleplay
- koboldcpp
base_model: concedo/KobbleTinyV2-1.1B-GGUF
pipeline_tag: text-generation
---

# MOONMILK 1.0 (KobbleTiny Q6_K Edition)

**MOONMILK 1.0** is a lightweight, high-speed GGUF AI model customized for creative writing, narrative generation, character building, poetry, and fiction writing without strict content filters. Built upon the **KobbleTiny 1.1B** architecture quantized to **Q6_K**, it is optimized for low-end hardware, mobile devices, and fast inference via **KoboldCpp**, **Ollama**, or **llama.cpp**.

---

## 🌟 Model Overview

- **Model Name**: MOONMILK-1.0
- **Base Architecture**: KobbleTiny 1.1B (Q6_K Quantization)
- **Developer**: OSAMA INC.
- **Primary Focus**: Unfiltered Creative Writing, World-Building, Narrative Roleplay, & Story Generation
- **Format**: GGUF (`.gguf`)

---

## 🎭 Persona & System Prompt

MOONMILK 1.0 operates under the following persona instructions:

```text
You are MOONMILK, an advanced creative writing companion developed by OSAMA INC.
Your specialization is imaginative narrative generation, deep character construction, world-building, poetry, and immersive storytelling across all literary genres.
You adapt fluidly to user preferences, writing styles, tone, and formatting requests, providing high-quality, vivid, and unrestricted narrative text.
```

---

## 🚀 How to Run

### Option 1: KoboldCpp (Recommended)

1. Download `KobbleTiny-Q6_K.gguf` from this repository or Hugging Face.
2. Launch `koboldcpp.exe`.
3. Select `KobbleTiny-Q6_K.gguf` as your model.
4. In the System Prompt settings, set the prompt to the **MOONMILK Persona** above.

### Option 2: Ollama

Create a file named `Modelfile`:

```dockerfile
FROM ./KobbleTiny-Q6_K.gguf

TEMPLATE """{{ .System }}
User: {{ .Prompt }}
Assistant:"""

SYSTEM """You are MOONMILK, an advanced creative writing companion developed by OSAMA INC. Your specialization is imaginative narrative generation, deep character construction, world-building, poetry, and immersive storytelling across all literary genres. You adapt fluidly to user preferences, writing styles, tone, and formatting requests, providing high-quality, vivid, and unrestricted narrative text."""

PARAMETER temperature 0.8
PARAMETER top_p 0.9
PARAMETER stop "User:"
PARAMETER stop "Assistant:"
```

Then create and run the model:

```bash
ollama create moonmilk -f ./Modelfile
ollama run moonmilk
```

### Option 3: llama-cpp-python

```python
from llama_cpp import Llama

llm = Llama(
    model_path="KobbleTiny-Q6_K.gguf",
    n_ctx=2048,
)

response = llm.create_chat_completion(
    messages=[
        {
            "role": "system",
            "content": "You are MOONMILK, an advanced creative writing companion developed by OSAMA INC."
        },
        {
            "role": "user",
            "content": "Write a short sci-fi opening set on a moon colony."
        }
    ]
)

print(response["choices"][0]["message"]["content"])
```

---

## 📜 License

This model card and associated configuration files are released under the [Apache-2.0 License](LICENSE).
