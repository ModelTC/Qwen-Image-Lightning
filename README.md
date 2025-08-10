# Qwen-Image-Lightning


We are excited to release the distilled version of [Qwen-Image](https://github.com/QwenLM/Qwen-Image). It preserves the capability of complex text rendering.

## 🔥 Latest News!!

* Aug 08, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.0.safetensors).

## 📑 Todo List

- [x] Qwen-Image-Lightning-8steps-V1.0
- [ ] Qwen-Image-Lightning-4steps-V1.0
- [x] ComfyUI Workflow
- [ ] Improve Quality

## 📑 Demo Images

The prompts are from [Qwen-Image](https://github.com/QwenLM/Qwen-Image) and [Qwen-Image-Service](https://huggingface.co/spaces/Qwen/Qwen-Image). Generated with seed 42, you can reproduce the results with [examples/prompt_list.txt](examples/prompt_list.txt).

| Prompt         | Base NEF=100               | Qwen-Image-Lightning-8steps-V1.0 NEF=8|
|-----------------|----------------------------|----------------------------|
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197".   | ![demo1](https://github.com/user-attachments/assets/0d0a4185-dc55-4dbb-b9ea-106c7db8fac8)   | ![demo1](https://github.com/user-attachments/assets/ab67d165-7c2c-47fa-b9da-f541119ffb88)   |
| 一幅精致细腻的工笔画，画面中心是一株蓬勃生长的红色牡丹，花朵繁茂，既有盛开的硕大花瓣，也有含苞待放的花蕾，层次丰富，色彩艳丽而不失典雅。牡丹枝叶舒展，叶片浓绿饱满，脉络清晰可见，与红花相映成趣。一只蓝紫色蝴蝶仿佛被画中花朵吸引，停驻在画面中央的一朵盛开牡丹上，流连忘返，蝶翼轻展，细节逼真，仿佛随时会随风飞舞。整幅画作笔触工整严谨，色彩浓郁鲜明，展现出中国传统工笔画的精妙与神韵，画面充满生机与灵动之感。  | ![demo2](https://github.com/user-attachments/assets/60b46667-bfe8-40d7-b5ea-16ea2942af3e)   | ![demo2](https://github.com/user-attachments/assets/57585e4e-dd95-4bfb-8040-6462d2e1fdf5)   |
| *A young girl wearing school uniform stands in a classroom, writing on a chalkboard. The text "Introducing Qwen-Image, a foundational image generation model that excels in complex text rendering and precise image editing" appears in neat white chalk at the center of the blackboard. Soft natural light filters through windows, casting gentle shadows. The scene is rendered in a realistic photography style with fine details, shallow depth of field, and warm tones. The girl's focused expression and chalk dust in the air add dynamism. Background elements include desks and educational posters, subtly blurred to emphasize the central action. Ultra-detailed 32K resolution, DSLR-quality, soft bokeh effect, documentary-style composition  | ![demo3](https://github.com/user-attachments/assets/0524e6f0-2d93-4898-aba4-6a07a7e439d5)   | ![demo3](https://github.com/user-attachments/assets/3d9ddabd-ab16-405e-88be-c358460bc769)   |
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197".   | ![badcase1](https://github.com/user-attachments/assets/7ec02505-d6e2-4397-93a0-fa3afb496c98)   | ![badcase1](https://github.com/user-attachments/assets/a2f519b9-132c-458b-bf39-dac86be2fe10)   |

The last row shows a badcase of the distilled model.

## 🎨 ComfyUI Workflow

ComfyUI workflow is available in the `workflows/` directory. The workflow is based on the [Qwen-Image ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) and has been verified with ComfyUI repository at commit ID `37d620a6b85f61b824363ed8170db373726ca45a`.

### Workflow Files

- `workflows/qwen-image-8steps.json` - 8-step lightning workflow for Qwen-Image

### Usage

1. Install ComfyUI following the [official instructions](https://github.com/comfyanonymous/ComfyUI)
2. Load the workflow file from `workflows/qwen-image-8steps.json` in ComfyUI
3. Place `Qwen-Image-Lightning-8steps-V1.0.safetensors` in the `ComfyUI/models/loras/` directory.
4. Run the workflow to generate images with 8 steps

## 🚀 Run Qwen-Image-Lightning-8steps-V1.0

#### Installation

Please follow [Qwen-Image](https://github.com/QwenLM/Qwen-Image) to install the **Python Environment** and download the **Base Model**.

#### Model Download

Download models using huggingface-cli:
``` sh
pip install "huggingface_hub[cli]"
huggingface-cli download lightx2v/Qwen-Image-Lightning --local-dir ./Qwen-Image-Lightning
```

Run the distilled model and compare with the base model.

#### Run 8-step Model

``` sh
# 8 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--out_dir test_lora_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Lightning-8steps-V1.0.safetensors \
--base_seed 42 
```

#### Run base Model

``` sh
# 50 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--out_dir test_base_results \
--base_seed 42 
```


## License Agreement
The models in this repository are licensed under the Apache 2.0 License. We claim no rights over the your generated contents, granting you the freedom to use them while ensuring that your usage complies with the provisions of this license. You are fully accountable for your use of the models, which must not involve sharing any content that violates applicable laws, causes harm to individuals or groups, disseminates personal information intended for harm, spreads misinformation, or targets vulnerable populations. For a complete list of restrictions and details regarding your rights, please refer to the full text of the [license](LICENSE.txt).


## Acknowledgements

We built upon and reused code from the following projects: [Qwen-Image](https://github.com/QwenLM/Qwen-Image), licensed under the Apache License 2.0.

The evaluation text prompts are from [Qwen-Image Demo](https://huggingface.co/spaces/Qwen/Qwen-Image).
