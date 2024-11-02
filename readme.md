# SmolLM2 ComfyUI Node

A custom node for ComfyUI that integrates SmolLM2, a lightweight language model specialized in prompt enhancement and creative text generation. This node allows you to generate and enhance prompts directly within your ComfyUI workflow.

## Features

- 🤖 Integrates SmolLM2-Prompt-Enhance model
- 🎯 Automatic model downloading and management
- 🎲 Seed control for reproducible outputs
- ⚙️ Advanced generation parameters
- 💻 CPU and CUDA support
- 🔄 Seamless integration with other ComfyUI nodes

## Installation

1. Navigate to your ComfyUI's custom nodes directory:
```bash
cd ComfyUI/custom_nodes/
```

2. Clone this repository:
```bash
git clone https://github.com/marduk191/comfyui-smollm2
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

The model will be automatically downloaded when you first use the node.

## Parameters

The node provides several parameters to control text generation:

- **prompt** (string): Your input text prompt
- **seed** (int): Seed for reproducible generation (0 to 4,294,967,295)
- **random_seed** (boolean): Toggle random seed generation
- **max_new_tokens** (int): Maximum number of tokens to generate (1 to 1024)
- **repetition_penalty** (float): Penalty for repeating words (0.1 to 10.0)
- **temperature** (float): Controls randomness of generation (0.1 to 2.0)
- **top_p** (float): Controls nucleus sampling (0.0 to 1.0)

### Parameter Guidelines

- **temperature**: 
  - Lower values (0.1-0.7): More focused and deterministic outputs
  - Higher values (0.7-2.0): More creative and diverse outputs
  - Default: 0.7

- **top_p**:
  - Lower values (0.1-0.5): More focused on likely tokens
  - Higher values (0.5-1.0): More diverse token selection
  - Default: 0.9

- **repetition_penalty**:
  - Lower values (0.1-1.0): More repetition allowed
  - Higher values (1.0-10.0): Less repetition allowed
  - Default: 1.2

## Usage

After installation, you'll find the "SmolLM2 Text Generator" node in the "text" category of ComfyUI's node menu.

### Basic Workflow

1. Add the SmolLM2 Text Generator node to your workspace
2. Connect a text input or primitive node to the "prompt" input
3. Adjust generation parameters as needed
4. Connect the output to other nodes that accept text input (e.g., SDXL prompt nodes)

### Example Use Cases

1. **Prompt Enhancement**:
```python
Input: "cat"
Output: "a gray cat with white fur and black eyes is in the center of an open window..."
```

2. **Scene Description**:
```python
Input: "forest morning"
Output: "a misty morning in a dense forest, sunbeams filtering through tall pine trees..."
```

## Model Information

This node uses:
- Model: gokaygokay/SmolLM2-Prompt-Enhance
- Tokenizer: HuggingFaceTB/SmolLM2-135M-Instruct

Models will be automatically downloaded to your ComfyUI's `models/smollm2/` directory.

## Requirements

- ComfyUI
- Python 3.8+
- PyTorch >= 2.0.0
- Transformers >= 4.36.0
- Other dependencies listed in requirements.txt

## Troubleshooting

Common issues and solutions:

1. **CUDA Out of Memory**:
   - Reduce max_new_tokens
   - Use CPU if GPU memory is limited

2. **Generation Too Random/Conservative**:
   - Adjust temperature and top_p values
   - Use lower temperature for more focused outputs
   - Use higher temperature for more creative outputs

3. **Reproducibility Issues**:
   - Ensure random_seed is disabled
   - Use the same seed value
   - Keep all other parameters identical

## License

[MIT License](LICENSE)

## Credits

- Original SmolLM2 model by [gokaygokay](https://huggingface.co/gokaygokay)
- ComfyUI by [comfyanonymous](https://github.com/comfyanonymous/ComfyUI)

## Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

### Development Guidelines

- Follow PEP 8 style guide
- Add tests for new features
- Update documentation as needed
- Maintain compatibility with ComfyUI's main branch

## Support

If you encounter any issues or have questions:
1. Check the troubleshooting section
2. Look through existing GitHub issues
3. Open a new issue with:
   - ComfyUI version
   - Python version
   - Full error message
   - Steps to reproduce
