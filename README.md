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

To assess the distilled models' performance characteristics, including their **strengths and limitations**, we compare the performance of the three models, i.e., `Qwen-Image`, `Qwen-Image-Lightning-8steps-V1.1`, and `Qwen-Image-Lightning-4steps-V1.0`, in different scenarios. The results can be reproduced following [the section below](#-run-evaluation-and-test).

### - **Quality and Speed**

Compared to the base model, the distilled models (8-step and 4-step) deliver a 12–25× speed improvement with no significant loss in performance in most cases.

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| 一个会议室，墙上写着"3.14159265-358979-32384626-4338327950"，一个小陀螺在桌上转动。 | ![111](https://github.com/user-attachments/assets/096885dd-09be-4259-8989-5120c442b136) | ![112](https://github.com/user-attachments/assets/d25b7437-d494-4eaa-8cb2-767587074301) | ![113](https://github.com/user-attachments/assets/7bd4c64c-8a79-4601-ba27-6c26a8be879b) |
| 宫崎骏的动漫风格。平视角拍摄，阳光下的古街热闹非凡。一个穿着青衫、手里拿着写着“阿里云”卡片的逍遥派弟子站在中间。旁边两个小孩惊讶的看着他。左边有一家店铺挂着“云存储”的牌子，里面摆放着发光的服务器机箱，门口两个侍卫守护者。右边有两家店铺，其中一家挂着“云计算”的牌子，一个穿着旗袍的美丽女子正看着里面闪闪发光的电脑屏幕；另一家店铺挂着“云模型”的牌子，门口放着一个大酒缸，上面写着“千问”，一位老板娘正在往里面倒发光的代码溶液。 | ![121](https://github.com/user-attachments/assets/f13d8e40-653d-4d46-9f6d-029fd85e03e7) | ![122](https://github.com/user-attachments/assets/fbe24265-106a-4a86-84a2-dda4fe8bb15d) | ![123](https://github.com/user-attachments/assets/3864a8de-7798-41f1-88b9-f6a2fe08ee7e) |
| 一副典雅庄重的对联悬挂于厅堂之中，房间是个安静古典的中式布置，桌子上放着一些青花瓷，对联上左书“义本生知人机同道善思新”，右书“通云赋智乾坤启数高志远”， 横批“智启通义”，字体飘逸，中间挂在一着一副中国风的画作，内容是岳阳楼。 | ![131](https://github.com/user-attachments/assets/6207e422-8611-42f7-90b7-c5271964e501) | ![132](https://github.com/user-attachments/assets/7859aa72-6b93-44d7-a6fa-c7ed3f1b6a03) | ![133](https://github.com/user-attachments/assets/66b699b6-09ec-45b0-903b-4be6d2aa55f5) |
| A movie poster. The first row is the movie title, which reads “Imagination Unleashed”. The second row is the movie subtitle, which reads “Enter a world beyond your imagination”. The third row reads “Cast: Qwen-Image”. The fourth row reads “Director: The Collective Imagination of Humanity”. The central visual features a sleek, futuristic computer from which radiant colors, whimsical creatures, and dynamic, swirling patterns explosively emerge, filling the composition with energy, motion, and surreal creativity. The background transitions from dark, cosmic tones into a luminous, dreamlike expanse, evoking a digital fantasy realm. At the bottom edge, the text “Launching in the Cloud, August 2025” appears in bold, modern sans-serif font with a glowing, slightly transparent effect, evoking a high-tech, cinematic aesthetic. The overall style blends sci-fi surrealism with graphic design flair—sharp contrasts, vivid color grading, and layered visual depth—reminiscent of visionary concept art and digital matte painting, 32K resolution, ultra-detailed. | ![141](https://github.com/user-attachments/assets/1c2749ed-9b68-4f84-ad7a-196a64e9d2d6) | ![142](https://github.com/user-attachments/assets/d4f66d85-3ed5-442e-9ad9-8eca144cac10) | ![143](https://github.com/user-attachments/assets/5edb6340-03fa-4f1e-8131-b9c699f2818e) |
| 一张企业级高质量PPT页面图像，整体采用科技感十足的星空蓝为主色调，背景融合流动的发光科技线条与微光粒子特效，营造出专业、现代且富有信任感的品牌氛围；页面顶部左侧清晰展示橘红色Alibaba标志，色彩鲜明、辨识度高。主标题位于画面中央偏上位置，使用大号加粗白色或浅蓝色字体写着“通义千问视觉基础模型”，字体现代简洁，突出技术感；主标题下方紧接一行楷体中文文字：“原生中文·复杂场景·自动布局”，字体柔和优雅，形成科技与人文的融合。下方居中排布展示了四张与图片，分别是：一幅写实与水墨风格结合的梅花特写，枝干苍劲、花瓣清雅，背景融入淡墨晕染与飘雪效果，体现坚韧不拔的精神气质；上方写着黑色的楷体"梅傲"。一株生长于山涧石缝中的兰花，叶片修长、花朵素净，搭配晨雾缭绕的自然环境，展现清逸脱俗的文人风骨；上方写着黑色的楷体"兰幽"。一组迎风而立的翠竹，竹叶随风摇曳，光影交错，背景为青灰色山岩与流水，呈现刚柔并济、虚怀若谷的文化意象；上方写着黑色的楷体"竹清"。一片盛开于秋日庭院的菊花丛，花色丰富、层次分明，配以落叶与古亭剪影，传递恬然自适的生活哲学；上方写着黑色的楷体"菊淡"。所有图片采用统一尺寸与边框样式，呈横向排列。页面底部中央用楷体小字写明“2025年8月，敬请期待”，排版工整、结构清晰，整体风格统一且细节丰富，极具视觉冲击力与品牌调性。 | ![151](https://github.com/user-attachments/assets/a5edca6d-99c2-46de-a94a-2ab156773ecf) | ![152](https://github.com/user-attachments/assets/b417d3df-61c2-4450-b5d5-56e80611974c) | ![153](https://github.com/user-attachments/assets/11cb221c-9b68-4c40-b874-410c1d793a97) |

---

### - **Dense or Small Text Rendering**

In scenarios involving dense or small text, the base model is more likely to produce better results.

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| 一个穿着"QWEN"标志的T恤的中国美女正拿着黑色的马克笔面相镜头微笑。她身后的玻璃板上手写体写着 “一、Qwen-Image的技术路线： 探索视觉生成基础模型的极限，开创理解与生成一体化的未来。二、Qwen-Image的模型特色：1、复杂文字渲染。支持中英渲染、自动布局； 2、精准图像编辑。支持文字编辑、物体增减、风格变换。三、Qwen-Image的未来愿景：赋能专业内容创作、助力生成式AI发展。” | ![211](https://github.com/user-attachments/assets/fa47db9d-640e-4795-ba0d-1ded2fe2b0a0) | ![212](https://github.com/user-attachments/assets/3492b14c-00cb-42a5-8e0f-0f008cc76401) | ![213](https://github.com/user-attachments/assets/92afeb4b-4f5b-42ec-86df-79634ebc98d9) |


---

### - **Hair-like Details**

In scenes containing hair-like details, the base model demonstrates superior rendering fidelity, whereas the distilled models may yield outputs that appear either noticeably blurred or excessively sharpened.

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| A capybara wearing a suit holding a sign that reads Hello World. | ![311](https://github.com/user-attachments/assets/a252369b-9c48-424a-a559-368b412d70cb) | ![312](https://github.com/user-attachments/assets/e0675f8d-d0c8-4d1e-8875-eb04827ac1db) | ![313](https://github.com/user-attachments/assets/a80d8595-20cb-47ed-b322-8ae3a7626808) |


---

### - **Highly Complex Scenes**

In highly complex scenes, all three models may fail to produce satisfactory results.

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| "A vibrant, warm neon-lit street scene in Hong Kong at the afternoon, with a mix of colorful Chinese and English signs glowing brightly. The atmosphere is lively, cinematic, and rain-washed with reflections on the pavement. The colors are vivid, full of pink, blue, red, and green hues. Crowded buildings with overlapping neon signs. 1980s Hong Kong style. Signs include: "龍鳳冰室" "金華燒臘" "HAPPY HAIR" "鴻運茶餐廳" "EASY BAR" "永發魚蛋粉" "添記粥麵" "SUNSHINE MOTEL" "美都餐室" "富記糖水" "太平館" "雅芳髮型屋" "STAR KTV" "銀河娛樂城" "百樂門舞廳" "BUBBLE CAFE" "萬豪麻雀館" "CITY LIGHTS BAR" "瑞祥香燭莊" "文記文具" "GOLDEN JADE HOTEL" "LOVELY BEAUTY" "合興百貨" "興旺電器" And the background is warm yellow street and with all stores' lights on. | ![411](https://github.com/user-attachments/assets/680863bb-b6cd-49a3-96a7-27e9d706c309) | ![412](https://github.com/user-attachments/assets/e5d72387-01e2-456a-95a4-b0cf93e2e59a) | ![413](https://github.com/user-attachments/assets/82aad254-d39b-49e2-8a84-27230a73de65) |


---


### - **Inconsistencies in Model Rankings Across Test Cases**

Test results may vary across different cases. In certain test instances, the base model may perform better, whereas in others, the distilled models may achieve superior results. Even for the same prompt at different resolutions, the relative performance ranking of the models may differ substantially.


| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| A young girl wearing school uniform stands in a classroom, writing on a chalkboard. The text "Introducing Qwen-Image, a foundational image generation model that excels in complex text rendering and precise image editing" appears in neat white chalk at the center of the blackboard. Soft natural light filters through windows, casting gentle shadows. The scene is rendered in a realistic photography style with fine details, shallow depth of field, and warm tones. The girl's focused expression and chalk dust in the air add dynamism. Background elements include desks and educational posters, subtly blurred to emphasize the central action. Ultra-detailed 32K resolution, DSLR-quality, soft bokeh effect, documentary-style composition. | ![511](https://github.com/user-attachments/assets/23c69637-918a-42a6-8f92-e36da14ced39) | ![512](https://github.com/user-attachments/assets/b9f17e0a-38ee-4404-a7d2-8c9eea385123) | ![513](https://github.com/user-attachments/assets/5d566b6e-2751-4e17-ac04-5517f24a868d) |
| | ❌ | ✅ | ✅ |
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197". | ![611](https://github.com/user-attachments/assets/24f0c053-5c91-4607-a1de-c2a717f2d321) | ![612](https://github.com/user-attachments/assets/0480f979-99e6-4762-8b7a-41eba2d72660) | ![613](https://github.com/user-attachments/assets/b50266bc-96b1-4820-af95-9bd19dd8a186) |
| | ❌ | ✅ | ✅ |
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197". | ![621](https://github.com/user-attachments/assets/a58c62a1-e079-42d3-a418-9e4ff6e738fb) | ![622](https://github.com/user-attachments/assets/ed36ebea-0535-43b4-82db-b55b1fc0f22e) | ![623](https://github.com/user-attachments/assets/f411310f-19a0-4477-8af0-ed536835f0a2) |
| | ✅ | ✅ | ❌ |



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
