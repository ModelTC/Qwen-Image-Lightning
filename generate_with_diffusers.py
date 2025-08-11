import argparse
import math
import os

from diffusers import DiffusionPipeline, FlowMatchEulerDiscreteScheduler
from diffusers.models import QwenImageTransformer2DModel
import torch
import torch.nn as nn
from safetensors.torch import safe_open


def build_lora_names(key, lora_down_key, lora_up_key, is_native_weight):
    base = "diffusion_model." if is_native_weight else ""
    lora_down = base + key.replace(".weight", lora_down_key)
    lora_up = base + key.replace(".weight", lora_up_key)
    lora_alpha = base + key.replace(".weight", ".alpha")
    return lora_down, lora_up, lora_alpha


def load_and_merge_lora_weight(
    model: nn.Module,
    lora_state_dict: dict,
    lora_down_key: str = ".lora_down.weight",
    lora_up_key: str = ".lora_up.weight",
):
    is_native_weight = any("diffusion_model." in key for key in lora_state_dict)
    for key, value in model.named_parameters():
        lora_down_name, lora_up_name, lora_alpha_name = build_lora_names(
            key, lora_down_key, lora_up_key, is_native_weight
        )
        if lora_down_name in lora_state_dict:
            lora_down = lora_state_dict[lora_down_name]
            lora_up = lora_state_dict[lora_up_name]
            lora_alpha = float(lora_state_dict[lora_alpha_name])
            rank = lora_down.shape[0]
            scaling_factor = lora_alpha / rank
            assert lora_up.dtype == torch.float32
            assert lora_down.dtype == torch.float32
            delta_W = scaling_factor * torch.matmul(lora_up, lora_down)
            value.data = (value.data + delta_W).type_as(value.data)
    return model


def load_and_merge_lora_weight_from_safetensors(
    model: nn.Module,
    lora_weight_path: str,
    lora_down_key: str = ".lora_down.weight",
    lora_up_key: str = ".lora_up.weight",
):
    lora_state_dict = {}
    with safe_open(lora_weight_path, framework="pt", device="cpu") as f:
        for key in f.keys():
            lora_state_dict[key] = f.get_tensor(key)
    model = load_and_merge_lora_weight(
        model, lora_state_dict, lora_down_key, lora_up_key
    )
    return model


def main(
    model_name,
    prompt_list_file: str,
    lora_path: str | None,
    out_dir: str,
    base_seed: int,
    num_inference_steps: int = 8,
    true_cfg_scale: float = 1.0,
):
    if torch.cuda.is_available():
        torch_dtype = torch.bfloat16
        device = "cuda"
    else:
        torch_dtype = torch.float32
        device = "cpu"

    if lora_path is not None:
        model = QwenImageTransformer2DModel.from_pretrained(
            model_name, subfolder="transformer", torch_dtype=torch_dtype
        )
        assert os.path.exists(lora_path), f"Lora path {lora_path} does not exist"
        model = load_and_merge_lora_weight_from_safetensors(model, lora_path)
        scheduler_config = {
            "base_image_seq_len": 256,
            "base_shift": math.log(3),  # We use shift=3 in distillation
            "invert_sigmas": False,
            "max_image_seq_len": 8192,
            "max_shift": math.log(3),  # We use shift=3 in distillation
            "num_train_timesteps": 1000,
            "shift": 1.0,
            "shift_terminal": None,  # set shift_terminal to None
            "stochastic_sampling": False,
            "time_shift_type": "exponential",
            "use_beta_sigmas": False,
            "use_dynamic_shifting": True,
            "use_exponential_sigmas": False,
            "use_karras_sigmas": False,
        }
        scheduler = FlowMatchEulerDiscreteScheduler.from_config(scheduler_config)
        pipe = DiffusionPipeline.from_pretrained(
            model_name, transformer=model, scheduler=scheduler, torch_dtype=torch_dtype
        )
    else:
        pipe = DiffusionPipeline.from_pretrained(model_name, torch_dtype=torch_dtype)

    pipe = pipe.to(device)

    positive_magic = {
        "en": "Ultra HD, 4K, cinematic composition.",  # for english prompt
        "zh": "超清，4K，电影级构图",  # for chinese prompt
    }

    negative_prompt = " "  # Recommended if you don't use a negative prompt.

    # Generate with different aspect ratios
    aspect_ratios = {
        "1:1": (1328, 1328),
        "16:9": (1664, 928),
        "9:16": (928, 1664),
        "4:3": (1472, 1104),
        "3:4": (1104, 1472),
        "3:2": (1584, 1056),
        "2:3": (1056, 1584),
    }

    with open(prompt_list_file, "r") as f:
        prompt_list = f.read().splitlines()
    os.makedirs(out_dir, exist_ok=True)

    for _, (width, height) in aspect_ratios.items():
        for i, prompt in enumerate(prompt_list):
            image = pipe(
                prompt=prompt + positive_magic["en"],
                negative_prompt=negative_prompt,
                width=width,
                height=height,
                num_inference_steps=num_inference_steps,
                true_cfg_scale=true_cfg_scale,
                generator=torch.Generator(device="cuda").manual_seed(base_seed),
            ).images[0]

            image.save(
                f"{out_dir}/{i:02d}_{width}x{height}_{num_inference_steps}steps_cfg{true_cfg_scale}_example.png"
            )


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--prompt_list_file", type=str, default="examples/prompt_list.txt"
    )
    parser.add_argument("--out_dir", type=str, default="results")
    parser.add_argument("--lora_path", type=str, default=None)
    parser.add_argument("--base_seed", type=int, default=42)
    parser.add_argument("--model_name", type=str, default="Qwen/Qwen-Image")
    parser.add_argument("--steps", type=int, default=None)
    parser.add_argument("--cfg", type=float, default=None)
    args = parser.parse_args()
    if args.steps is None:
        num_inference_steps = 50 if args.lora_path is None else 8
    else:
        num_inference_steps = args.steps
    if args.cfg is None:
        true_cfg_scale = 4.0 if args.lora_path is None else 1.0
    else:
        true_cfg_scale = args.cfg
    if args.lora_path is not None:
        assert os.path.exists(args.lora_path), (
            f"Lora path {args.lora_path} does not exist"
        )

    main(
        model_name=args.model_name,
        prompt_list_file=args.prompt_list_file,
        lora_path=args.lora_path,
        out_dir=args.out_dir,
        base_seed=args.base_seed,
        num_inference_steps=num_inference_steps,
        true_cfg_scale=true_cfg_scale,
    )
