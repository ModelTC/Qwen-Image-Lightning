# Qwen-Image-Lightning

We are excited to release the distilled version of [Qwen-Image](https://github.com/QwenLM/Qwen-Image). It preserves the capability of complex text rendering.

## 🔥 Latest News
* Jan 01, 2026: 👋 Release [Qwen-Image-2512-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/blob/main/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors) and its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-2512-Lightning/blob/main/Qwen-Image-2512-Lightning-4steps-V1.0-bf16.safetensors).
* Dec 22, 2025: 👋 Release [Qwen-Image-Edit-2511-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/blob/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-fp32.safetensors), its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/blob/main/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-bf16.safetensors), and [a fused fp8 model combining the bf16 base and fp32 LoRA](https://huggingface.co/lightx2v/Qwen-Image-Edit-2511-Lightning/blob/main/qwen_image_edit_2511_fp8_e4m3fn_scaled_lightning.safetensors).
* Oct 14, 2025: 👋 [Compatibility issues](https://github.com/ModelTC/Qwen-Image-Lightning/issues/32) associated with using the Lightning LoRA alongside the [Qwen-Image FP8 base model](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) have been resolved. To resolve this issue, we provide two alternative approaches. Please consult [the section below](#-using-lightning-loras-with-fp8-models) for guidance on which model to download based on your specific technical constraints and performance needs.
* Oct 09, 2025: 👋 Release [Qwen-Image-Edit-2509-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-fp32.safetensors) and its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-bf16.safetensors), [Qwen-Image-Edit-2509-Lightning-8steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-fp32.safetensors) and its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-bf16.safetensors).
* Sep 12, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V2.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V2.0.safetensors).
* Sep 10, 2025: 👋 Release [Qwen-Image-Lightning-4steps-V2.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors). Please see [the comparison between V1.x and V2.x](#-comparison-between-v1x-and-v2x).
* Aug 28, 2025: 👋 Release workflows for `Qwen-Image-Edit-Lightning`.
* Aug 24, 2025: 👋 Release [Qwen-Image-Edit-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-Lightning-4steps-V1.0.safetensors) and its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-Lightning-4steps-V1.0-bf16.safetensors).
* Aug 23, 2025: 👋 Release [Qwen-Image-Edit-Lightning-8steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-Lightning-8steps-V1.0.safetensors) and its [bf16 version](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Edit-Lightning-8steps-V1.0-bf16.safetensors).
* Aug 12, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V1.1](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.1.safetensors).
* Aug 12, 2025: 👋 Upload the bf16 version of the 8-step model [Qwen-Image-Lightning-8steps-V1.1-bf16](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.1-bf16.safetensors) and 4-step model [Qwen-Image-Lightning-4steps-V1.0-bf16](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0-bf16.safetensors).
* Aug 11, 2025: 👋 Release [Qwen-Image-Lightning-4steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V1.0.safetensors).
* Aug 08, 2025: 👋 Release [Qwen-Image-Lightning-8steps-V1.0](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-8steps-V1.0.safetensors).

## 📑 Community Support

* [Diffusers](https://github.com/huggingface/diffusers) now supports loading Qwen-Image-Lightning within the Qwen-Image pipeline. Please check [their documentation](https://huggingface.co/docs/diffusers/main/api/pipelines/qwenimage) for details.
* [ComfyUI](https://github.com/comfyanonymous/ComfyUI) provides native workflows for [Qwen-Image](https://docs.comfy.org/tutorials/image/qwen/qwen-image) and [Qwen-Image-Edit](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit), including Lightning LoRA weights.
* [Nunchaku](https://github.com/nunchaku-tech/nunchaku) has released 4-bit [Qwen-Image lightning](https://huggingface.co/nunchaku-tech/nunchaku-qwen-image). Try their [example script](https://github.com/nunchaku-tech/nunchaku/blob/main/examples/v1/qwen-image-lightning.py) to reduce inference GPU memory usage.
* [Cache-dit](https://github.com/vipshop/cache-dit) now supports **3.5** steps inference for [Qwen-Image-Lightning](https://github.com/vipshop/cache-dit/blob/main/examples/pipeline/run_qwen_image_lightning.py) with cache acceleration.

## 📑 Todo List

* [x] Qwen-Image-Lightning-4/8steps-V1.x
* [x] ComfyUI Workflow
* [x] Qwen-Image-Edit-Lightning-4/8steps-V1.0
* [x] Qwen Edit ComfyUI Workflow
* [x] Qwen-Image-Lightning-4/8steps-V2.0
* [ ] Qwen-Image-Edit-Lightning-4/8steps-V2.0
* [x] Qwen-Image-Edit-2509-Lightning-4/8steps-V1.0
* [x] Qwen Edit 2509 ComfyUI Workflow
* [x] Qwen-Image-Edit-2511-Lightning-4steps-V1.0
* [ ] Qwen Edit 2511 ComfyUI Workflow
* [x] Qwen-Image-2512-Lightning-4steps-V1.0

## 📑 Comparison between V1.x and V2.x
Compared to V1.0, V2.0  produces images with reduced over-saturation, resulting in improved skin texture and more natural-looking visuals. 
### Qwen-Image-Lightning
| 4steps-V1.0 NFE=4 | 4steps-V2.0 NFE=4 | 8steps-V1.1 NFE=8 | 8steps-V2.0 NFE=8 |
|---|---|---|---|
| ![111](https://github.com/user-attachments/assets/03cc4358-2357-45a7-87f1-94a1c776e845) | ![112](https://github.com/user-attachments/assets/99b5a739-6452-4a8b-9e5b-d44d9a2ff080) | ![113](https://github.com/user-attachments/assets/f5da20ed-6b24-436e-969d-bc00a15a1ae2) | ![114](https://github.com/user-attachments/assets/d70298f8-2ce7-4ddc-816b-acf72fc26692) |
| ![111](https://github.com/user-attachments/assets/deb73eeb-05fe-4fb5-bde5-4e038b4d5118) | ![112](https://github.com/user-attachments/assets/158890c4-8dc5-4009-847c-1c9abb5a82ae) | ![113](https://github.com/user-attachments/assets/f6d0f497-0a69-4a49-b2c4-1c3107b03f94) | ![114](https://github.com/user-attachments/assets/16ee403a-f316-479b-a7fb-11010bf12ca1) |

## 📑 Using Lightning LoRAs with FP8 Models
The utilization of existing LoRA weights with the [qwen_image_fp8_e4m3fn.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) base model results in the grid artifacts reported in [Issue #32](https://github.com/ModelTC/Qwen-Image-Lightning/issues/32), wherein generated images exhibit a grid-like pattern. This artifact stems from the fact that the qwen_image_fp8_e4m3fn.safetensors model was produced by directly downcasting the [original bf16 weights](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_bf16.safetensors), rather than employing a calibrated conversion process with appropriate scaling.

In response to the prevalent use of this model, we have released a new set of Lightning LoRA weights specifically optimized for this base. These weights were generated by distilling the qwen_image_fp8_e4m3fn.safetensors model using bf16 guidance, thereby mitigating the artifact issue.

An alternative solution we provide is [a newly released FP8 base weight](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image/qwen_image_fp8_e4m3fn_scaled.safetensors), converted with scaling to ensure better compatibility with the existing suite of LoRA weights trained on BF16 bases. A comparative analysis is provided below. 


| Base + LoRA | [bf16 base](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_bf16.safetensors) + [LoRA trained on bf16 base](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors)  | [fp8 base](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) + [LoRA trained on bf16 base](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors)  | [fp8 base](https://huggingface.co/Comfy-Org/Qwen-Image_ComfyUI/blob/main/split_files/diffusion_models/qwen_image_fp8_e4m3fn.safetensors) + [LoRA trained on fp8 base](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-fp8-e4m3fn-Lightning-4steps-V1.0-fp32.safetensors) | [scaled fp8 base](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image/qwen_image_fp8_e4m3fn_scaled.safetensors) + [LoRA trained on bf16 base](https://huggingface.co/lightx2v/Qwen-Image-Lightning/blob/main/Qwen-Image-Lightning-4steps-V2.0.safetensors) |
|:---:|:---:|:---:|:---:|:---:|
|Correctness|✅|❌|✅|✅|
|Comparison| ![111](https://github.com/user-attachments/assets/4a25b268-4006-462a-bc1c-f8be059dc019) | ![112](https://github.com/user-attachments/assets/38267c06-597f-4c69-9678-5d82e5c17ed2) | ![113](https://github.com/user-attachments/assets/21ebc752-e304-4ea3-bf65-ac3f50c9aa9c) | ![114](https://github.com/user-attachments/assets/5e0c022f-b64f-47ec-b888-b58ab8b99570) |
|Workflow|[base-bf16-lora-on-bf16.json](./workflows/fp8-comparison/base-bf16-lora-on-bf16.json)|[base-fp8-lora-on-bf16.json](./workflows/fp8-comparison/base-fp8-lora-on-bf16.json)|[base-fp8-lora-on-fp8.json](./workflows/fp8-comparison/base-fp8-lora-on-fp8.json)|[base-scaled-fp8-lora-on-bf16.json](./workflows/fp8-comparison/base-scaled-fp8-lora-on-bf16.json)|


## 📑 T2I Performance Report

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


## 📑 Editing Performance Report

We compare the performance of the three models, i.e., `Qwen-Image-Edit-Diffusers`, `Qwen-Image-Edit-Lightning-8steps-V1.0`, and `Qwen-Image-Edit-Lightning-4steps-V1.0`, in different scenarios. The results can be reproduced following [the section below](#-run-evaluation-and-test).


| Input Image | Prompt | Base Edit NFE=100 | 8steps-V1.0 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|---|
| ![111](https://github.com/user-attachments/assets/94079f67-835c-441c-bd9e-ec36ce4fa251)  | Replace the words 'HEALTH INSURANCE' on the letter blocks with 'Tomorrow will be better'. | ![112](https://github.com/user-attachments/assets/01a8a7ca-ca6c-440b-8732-f8ffbb66ffc6) | ![113](https://github.com/user-attachments/assets/430702c6-c54d-4788-80ab-aae2e457a086) | ![114](https://github.com/user-attachments/assets/e42c07b7-5d1c-4c57-bb1e-912b59b870a7) |
|   |  | Bad case: the first "m" appears as "mn" due to an extra stroke.  | | Bad case: the letter "o" is missing.|
| ![121](https://github.com/user-attachments/assets/5c7a29a7-b590-44b5-82fb-23cf90396ef2)  | Replace the words 'HEALTH INSURANCE' on the letter blocks with '明天会更好'. | ![122](https://github.com/user-attachments/assets/d9bb1218-849a-465b-a521-6e653bd87667) | ![123](https://github.com/user-attachments/assets/fb7192bc-7b5d-4743-9257-2c4206358e7c) | ![124](https://github.com/user-attachments/assets/046b5f79-3075-4f78-b22f-27c189ab15ab) |
|   |  |  | Bad case: an extra "更" is generated.| |
| ![131](https://github.com/user-attachments/assets/a8e8916f-a4c8-47d0-a938-3fe07716da5b)  | Replace the polka-dot shirt with a light blue shirt. | ![132](https://github.com/user-attachments/assets/da738b8a-220e-4a7c-b5d7-dc02f2adabc9) | ![133](https://github.com/user-attachments/assets/2cce11ab-9a0a-4893-a9ce-50022d5cfcd3) | ![134](https://github.com/user-attachments/assets/f66d3ec3-f957-4896-9859-0b486f1f30f6) |
| ![141](https://github.com/user-attachments/assets/00ab0b9e-773e-497d-841e-957c4507a710)  | Remove the hair from the plate. | ![142](https://github.com/user-attachments/assets/68d98b71-a11d-4dff-b9b8-eaa063a3e115) | ![143](https://github.com/user-attachments/assets/78aab90c-6ba6-464f-a478-a5eb54038813) | ![144](https://github.com/user-attachments/assets/90264ad7-49db-434f-bda8-c7aa9c3887be) |
| ![151](https://github.com/user-attachments/assets/e9523145-5be7-4204-9cb9-35bf3e373084)  | Generate a cartoon profile picture of the person. | ![152](https://github.com/user-attachments/assets/1c3bd38e-fe4f-4ecb-8e3c-d342c80bbbfb) | ![153](https://github.com/user-attachments/assets/6b0ee9de-59fa-465c-a4b9-04f271cdeacb) | ![154](https://github.com/user-attachments/assets/4c3dc692-5f67-4b0f-8873-a382d9873598) |
| ![161](https://github.com/user-attachments/assets/025a73ba-5bcf-4bf3-9876-b146db679da6)  | Transform the character in the image into an anime style, and add the text: "Accelerate image generation and editing with Lightx2V Qwen-Image-Lightning". | ![162](https://github.com/user-attachments/assets/2158e2f6-ccbf-41d1-9678-039058452dca) | ![163](https://github.com/user-attachments/assets/8a06b026-6818-4f33-ba20-1ce69766347f) | ![164](https://github.com/user-attachments/assets/d27f9a68-6916-4931-a7fd-77ace7ca0e2b) |
|   |  | Bad case: incorrect spelling "Lightx2V". | Bad case: incorrect spelling "editing with". | Failure case. |
| ![171](https://github.com/user-attachments/assets/9c8a5f27-d23c-431c-a57e-9d2aa3ba83e0)  | 将图中的人物改为日漫风格，并给图片添加文字“使用Lightx2V Qwen-Image-Lightning 加速图像生成和图片编辑”。 | ![172](https://github.com/user-attachments/assets/f256e198-40f6-4f38-a0e9-e57a4cb6b3d5) | ![173](https://github.com/user-attachments/assets/10623274-4b69-4bd8-87e3-7f72a818d676) | ![174](https://github.com/user-attachments/assets/43dbce1e-7726-42e0-8125-bf0d77debb58) |
| ![181](https://github.com/user-attachments/assets/ee2cc286-445c-49f5-8910-8656ca478a13)  | 将图中红色框中的文字改为"殇",只改变框内的画面，框外的画面维持不变。 | ![182](https://github.com/user-attachments/assets/9267dda5-c788-4cd4-9811-448b06a4e2e9) | ![183](https://github.com/user-attachments/assets/4b7df2b5-c867-4d27-8aab-49b15b71c82d) | ![184](https://github.com/user-attachments/assets/948841a5-4653-4ce0-b246-94b305c04ab5) |


## 🚀 Run Evaluation and Test with LightX2V

### Installation

```sh
git clone https://github.com/ModelTC/LightX2V.git
cd LightX2V
pip install -v -e .
```

### Run 4-step Edit-2511 Model

```sh
python examples/qwen_image/qwen_2511_with_distill_lora.py
```

### Run Base Edit-2511 Model

``` sh
python examples/qwen_image/qwen_2511_fp8.py
```

### Run Qwen-Image-2512 Model

- Please follow the instructions in [LightX2V](https://github.com/ModelTC/LightX2V/tree/main/examples/qwen_image#usage-method-1-using-bash-scripts-highly-recommended) to run inference on Qwen-Image-2512 model and its lightning lora with LightX2V.

## 🚀 Run Evaluation and Test with Diffusers

### Installation

- Please follow [Qwen-Image](https://github.com/QwenLM/Qwen-Image) to install the **Python Environment**, e.g., diffusers v0.35.1, and download the **Base Model**.
- For the Qwen-Image-Edit-2509, Qwen-Image-Edit-2511 and Qwen-Image-2512, please install the latest diffusers from their main branch by
```sh
pip install git+https://github.com/huggingface/diffusers
```

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

### Run 8-step Edit Model

``` sh
# 8 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_prompt_list.txt \
--image_path_list_file examples/image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit \
--out_dir test_lora_8_step_edit_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Edit-Lightning-8steps-V1.0.safetensors \
--base_seed 42 --steps 8 --cfg 1.0
```

### Run 4-step Edit Model

``` sh
# 4 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_prompt_list.txt \
--image_path_list_file examples/image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit \
--out_dir test_lora_4_step_edit_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Edit-Lightning-4steps-V1.0.safetensors \
--base_seed 42 --steps 4 --cfg 1.0
```

### Run Base Edit Model

``` sh
# 50 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_prompt_list.txt \
--image_path_list_file examples/image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit \
--out_dir test_base_edit_results \
--base_seed 42 --steps 50 --cfg 4.0
```

### Run 8-step Edit-2509 Model

``` sh
# 8 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_plus_prompt_list.txt \
--image_path_list_file examples/edit_plus_image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit-2509 \
--out_dir test_lora_8_step_edit_2509_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-fp32.safetensors \
--base_seed 42 --steps 8 --cfg 1.0
```

### Run 4-step Edit-2509 Model

``` sh
# 4 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_plus_prompt_list.txt \
--image_path_list_file examples/edit_plus_image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit-2509 \
--out_dir test_lora_4_step_edit_2509_results \
--lora_path Qwen-Image-Lightning/Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-fp32.safetensors \
--base_seed 42 --steps 4 --cfg 1.0
```

### Run Base Edit-2509 Model

``` sh
# 40 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_plus_prompt_list.txt \
--image_path_list_file examples/edit_plus_image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit-2509 \
--out_dir test_base_40_step_edit_2509_results \
--base_seed 42 --steps 40 --cfg 4.0
```

### Run 4-step Edit-2511 Model

``` sh
# 4 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_plus_prompt_list.txt \
--image_path_list_file examples/edit_plus_image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit-2511 \
--out_dir test_lora_4_step_edit_2511_results \
--lora_path Qwen-Image-Edit-2511-Lightning/Qwen-Image-Edit-2511-Lightning-4steps-V1.0-fp32.safetensors \
--base_seed 42 --steps 4 --cfg 1.0
```

### Run Base Edit-2511 Model

``` sh
# 40 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/edit_plus_prompt_list.txt \
--image_path_list_file examples/edit_plus_image_path_list.txt \
--model_name Qwen/Qwen-Image-Edit-2511 \
--out_dir test_base_40_step_edit_2511_results \
--base_seed 42 --steps 40 --cfg 4.0
```

### Run 4-step Qwen-Image-2512 Model

``` sh
# 4 steps, cfg 1.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--model_name Qwen/Qwen-Image-2512 \
--out_dir test_lora_4_step_qwen_image_2512_results \
--lora_path Qwen-Image-2512-Lightning/Qwen-Image-2512-Lightning-4steps-V1.0-fp32.safetensors \
--base_seed 42 --steps 4 --cfg 1.0
```

### Run base Qwen-Image-2512 Model

``` sh
# 50 steps, cfg 4.0
python generate_with_diffusers.py \
--prompt_list_file examples/prompt_list.txt \
--model_name Qwen/Qwen-Image-2512 \
--out_dir test_base_50_step_qwen_image_2512_results \
--base_seed 42 --steps 50 --cfg 4.0
```

## 🎨 ComfyUI Workflow

ComfyUI workflow is available in the `workflows/` directory. 

- The Qwen-Image workflow is based on the [Qwen-Image ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image) and has been verified with ComfyUI repository at commit ID `37d620a6b85f61b824363ed8170db373726ca45a`. 

- The Qwen-Image-Edit workflow is based on the [Qwen-Image-Edit ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit). We noticed a gap in performance compared to diffusers inference, which may stem from differences in how ComfyUI and diffusers handle the processing.


### Workflow Files

* `workflows/qwen-image-8steps.json` - 8-step lightning workflow for Qwen-Image
* `workflows/qwen-image-4steps.json` - 4-step lightning workflow for Qwen-Image
* `workflows/qwen-image-edit-8steps.json` - 8-step lightning workflow for Qwen-Image-Edit
* `workflows/qwen-image-edit-4steps.json` - 4-step lightning workflow for Qwen-Image-Edit
* `workflows/qwen-image-edit-2509-8steps.json` - 8-step lightning workflow for Qwen-Image-Edit-2509
* `workflows/qwen-image-edit-2509-4steps.json` - 4-step lightning workflow for Qwen-Image-Edit-2509

### Usage

1. Install ComfyUI following the [official instructions](https://github.com/comfyanonymous/ComfyUI)
2. Download and place the Qwen-Image or Qwen-Image-Edit base model following the [Qwen-Image ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image), [Qwen-Image-Edit ComfyUI tutorial](https://docs.comfy.org/tutorials/image/qwen/qwen-image-edit) (include UNet/CLIP/VAE files into proper ComfyUI folders)
3. For **Qwen Image** workflows:
   - **8-step**: Load `workflows/qwen-image-8steps.json`, put `Qwen-Image-Lightning-8steps-V1.0.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 8
   - **4-step**: Load `workflows/qwen-image-4steps.json`, put `Qwen-Image-Lightning-4steps-V1.0.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 4
4. For **Qwen Image Edit** workflows:
   - **8-step**: Load `workflows/qwen-image-edit-8steps.json`, put `Qwen-Image-Edit-Lightning-8steps-V1.0.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 8
   - **4-step**: Load `workflows/qwen-image-edit-4steps.json`, put `Qwen-Image-Edit-Lightning-4steps-V1.0.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 4
5. For **Qwen Image Edit 2509** workflows:
   - **8-step**: Load `workflows/qwen-image-edit-2509-8steps.json`, put `Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-8steps-V1.0-fp32.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 8
   - **4-step**: Load `workflows/qwen-image-edit-2509-4steps.json`, put `Qwen-Image-Edit-2509/Qwen-Image-Edit-2509-Lightning-4steps-V1.0-fp32.safetensors` into `ComfyUI/models/loras/`, and set `KSampler` steps to 4
6. Run the workflow to generate images

## License Agreement

The models in this repository are licensed under the Apache 2.0 License. We claim no rights over your generated contents, granting you the freedom to use them while ensuring that your usage complies with the provisions of this license. You are fully accountable for your use of the models, which must not involve sharing any content that violates applicable laws, causes harm to individuals or groups, disseminates personal information intended for harm, spreads misinformation, or targets vulnerable populations. For a complete list of restrictions and details regarding your rights, please refer to the full text of the [license](LICENSE.txt).

## Acknowledgements

We built upon and reused code from the following projects: [Qwen-Image](https://github.com/QwenLM/Qwen-Image), licensed under the Apache License 2.0.

The evaluation text prompts are from [Qwen-Image](https://github.com/QwenLM/Qwen-Image), [Qwen-Image Blog](https://qwenlm.github.io/blog/qwen-image/) and [Qwen-Image-Service](https://huggingface.co/spaces/Qwen/Qwen-Image).

The test cases for Image Editing are from [Qwen-Image-Edit-api](https://www.alibabacloud.com/help/en/model-studio/qwen-image-edit-api), [reddit](https://www.reddit.com/r/comfyui/comments/1mue7k0/testing_the_new_qwen_image_editing_q4_gguf_and_4/) and [Chat-Qwen-AI](https://chat.qwen.ai/)

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=ModelTC/Qwen-Image-Lightning&type=Timeline)](https://www.star-history.com/#ModelTC/Qwen-Image-Lightning&Timeline)


## Citation

```bibtex
@misc{Qwen-Image-Lightning,
  title = {Qwen-Image-Lightning},
  author = {Xiangyu Fan and Zesong Qiu and Fanzhou Wang and Peng Gao and Lei Yang},
  year = {2025},
  url = {https://github.com/ModelTC/LightX2V-Qwen-Image-Lightning},
}
```