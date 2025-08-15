# Qwen-Image-Lightning

We are excited to release the distilled version of [Qwen-Image](https://github.com/QwenLM/Qwen-Image). It preserves the capability of complex text rendering.

## 🔥 Latest News
* Aug 12, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V1.1](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.1.safetensors).
* Aug 12, 2025: 👋 Upload the bf16 version of the 8-step model [Qwen-Image-Lightning-8steps-V1.1-bf16](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.1-bf16.safetensors) and 4-step model [Qwen-Image-Lightning-4steps-V1.0-bf16](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0-bf16.safetensors).
* Aug 11, 2025: 👋 Release [Qwen-Image-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors).
* Aug 08, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.0.safetensors).

## 📑 Todo List

* [x] Qwen-Image-Lightning-8steps-V1.1
* [x] Qwen-Image-Lightning-8steps-V1.0
* [x] Qwen-Image-Lightning-4steps-V1.0
* [x] ComfyUI Workflow
* [x] Improve Quality

## 📑 Performance Report

To assess the distilled models' performance characteristics, including their **strengths and constraints**, please refer to the [performance report](./performance_report/README.md).


## 🚀 Run Evaluation and Test

### Installation

Please follow [Qwen-Image](https://github.com/QwenLM/Qwen-Image) to install the **Python Environment** and download the **Base Model**.

### Model Download

Download models using huggingface-cli:

``` sh
pip install "huggingface_hub[cli]"
huggingface-cli download lightx2v/Qwen-Image-Lightning --local-dir ./Qwen-Image-Lightning
```

### Run 8-step Model

``` sh
# 8 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--out_dir test_lora_8_step_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Lightning-8steps-V1.0.safetensors \
--base_seed 42 --steps 8 --cfg 1.0
```

### Run 4-step Model

``` sh
# 4 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--out_dir test_lora_4_step_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Lightning-4steps-V1.0.safetensors \
--base_seed 42 --steps 4 --cfg 1.0
```

### Run base Model

``` sh
# 50 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--out_dir test_base_results \
--base_seed 42 --steps 50 --cfg 4.0
```

## 🎨 ComfyUI Workflow

ComfyUI workflow is available in the `workflows/` directory. The workflow is based on the [Qwen-Image ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) and has been verified with ComfyUI repository at commit ID `37d620a6b85f61b824363ed8170db373726ca45a`.

### Workflow Files

* `workflows/qwen-image-8steps.json` - 8-step lightning workflow for Qwen-Image
* `workflows/qwen-image-4steps.json` - 4-step lightning workflow for Qwen-Image

### Usage

1. Install ComfyUI following the [official instructions](https://github.com/comfyanonymous/ComfyUI)
2. Download and place the Qwen-Image base model following the [Qwen-Image ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) (include UNet/CLIP/VAE files into proper ComfyUI folders)
3. For 8-step workflow:
   * Load `workflows/qwen-image-8steps.json`
   * Put `Qwen-Image-Lightning-8steps-V1.0.safetensors` into `ComfyUI/models/loras/`
   * Ensure `KSampler` steps = 8
4. For 4-step workflow:
   * Load `workflows/qwen-image-4steps.json`
   * Put `Qwen-Image-Lightning-4steps-V1.0.safetensors` into `ComfyUI/models/loras/`
   * Ensure `KSampler` steps = 4
5. Run the workflow to generate images

## License Agreement

The models in this repository are licensed under the Apache 2.0 License. We claim no rights over your generated contents, granting you the freedom to use them while ensuring that your usage complies with the provisions of this license. You are fully accountable for your use of the models, which must not involve sharing any content that violates applicable laws, causes harm to individuals or groups, disseminates personal information intended for harm, spreads misinformation, or targets vulnerable populations. For a complete list of restrictions and details regarding your rights, please refer to the full text of the [license](LICENSE.txt).

## Acknowledgements

We built upon and reused code from the following projects: [Qwen-Image](https://github.com/QwenLM/Qwen-Image), licensed under the Apache License 2.0.

The evaluation text prompts are from [Qwen-Image](https://github.com/QwenLM/Qwen-Image), [Qwen-Image Blog](https://qwenlm.github.io/blog/qwen-image/) and [Qwen-Image-Service](https://huggingface.co/spaces/Qwen/Qwen-Image).

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ModelTC/Qwen-Image-Lightning&type=Timeline)](https://www.star-history.com/#ModelTC/Qwen-Image-Lightning&Timeline)
