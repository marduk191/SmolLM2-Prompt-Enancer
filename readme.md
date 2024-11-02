# SmolLM2 ComfyUI Node

A custom node for ComfyUI that integrates SmolLM2, a lightweight language model specialized in prompt enhancement and creative text generation. This node allows you to generate and enhance prompts directly within your ComfyUI workflow.

## Features

- 🤖 Integrates SmolLM2-Prompt-Enhance model
- 🎯 Automatic model downloading and management
- 🎲 Seed control for reproducible outputs
- ⚙️ Adjustable generation parameters
- 💻 CPU and CUDA support
- 🔄 Seamless integration with other ComfyUI nodes

## Installation

1. Navigate to your ComfyUI's custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/yourusername/comfyui-smollm2
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

The model will be automatically downloaded when you first use the node.

## Usage

After installation, you'll find the "SmolLM2 Text Generator" node in the "text" category of ComfyUI's node menu.

### Input Parameters

- **prompt** (string): Your input text prompt
- **seed** (int): Seed for reproducible generation (0 to 2^64-1)
- **max_new_tokens** (int): Maximum number of tokens to generate (1 to 1024)
- **repetition_penalty** (float): Penalty for repeating words (0.1 to 10.0)

### Output

- **STRING**: The generated text response

### Example Workflow

1. Add the SmolLM2 Text Generator node to your workspace
2. Connect a text input or primitive node to the "prompt" input
3. Adjust generation parameters as needed
4. Connect the output to other nodes that accept text input (e.g., SDXL prompt nodes)

## Example Input/Output

Input prompt:
```
cat
```

Output:
```
a gray cat with white fur and black eyes is in the center of an open window on a concrete floor. 
The front wall has two large windows that have light grey frames behind them. 
There is a small wooden door to the left side of the frame at the bottom right corner.
```

## Model Information

This node uses:
- Model: gokaygokay/SmolLM2-Prompt-Enhance
- Tokenizer: HuggingFaceTB/SmolLM2-135M-Instruct

Models will be automatically downloaded to your ComfyUI's `models/smollm2/` directory.

## Requirements

- ComfyUI
- Python 3.8+
- PyTorch
- Transformers library

## License

[MIT License](LICENSE)

## Credits

- Original SmolLM2 model by [gokaygokay](https://huggingface.co/gokaygokay)
- ComfyUI by [comfyanonymous](https://github.com/comfyanonymous/ComfyUI)

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please open an issue on the GitHub repository.
