# Qwen-Image-Lightning Performance Report


This report presents a comparative analysis of inference performance across three Qwen-Image model variants under controlled experimental conditions. We evaluated the original `Qwen-Image`, `Qwen-Image-Lightning-8step-V1.1`, and `Qwen-Image-Lightning-4step-V1.0` using standardized parameters to assess their respective computational efficiency and output quality.


## Key Findings Summary

- **Speed vs Quality Trade-off**: Distilled models offer 12–25× faster inference with minimal quality loss on standard tasks.
- **Complex Text Rendering Hierarchy**: Accuracy in complex text generation follows the hierarchy: Base model (NFE100) > 8-step (NFE8) ≥ 4-step (NFE4).
- **Fine Detail Hair Preservation**: Base model outperforms distilled models in rendering fine hair textures, maintaining superior detail retention.
- **Multi-Element Scene Complexity**: All models face challenges in generating highly complex, multi-element scenes.
- **Variability in Performance**: Distilled models can outperform the base model in some scenarios; performance is also influenced by output resolution for both base and distilled models.

## Experiment Setup

The experimental setup employed identical resolution settings and input conditions across all model variants to ensure fair comparison. A fixed random seed (seed=42) was implemented to maintain reproducibility and eliminate stochastic variations. Three distinct inference configurations were tested: 

- `Qwen-Image`, the base model with 50 inference steps at CFG=4 (NFE100), 
- `Qwen-Image-Lightning-8step-V1.1` with 8 steps at CFG=1 (NFE8), 
- `Qwen-Image-Lightning-4step-V1.0` with 4 steps at CFG=1 (NFE4). 


## Results and Analysis

### 1. Standard Generation Tasks
All three models perform equally well for basic image generation on `Long number`, `Anime scene with signs`, `Classical Chinese couplets`, `Movie poster` and `PPT design` tests.

**Table 1** demonstrates that the `Qwen-Image` (NFE100) achieves satisfactory inference, while the distilled variants `Qwen-Image-Lightning-8step-V1.1` (NFE8) and `Qwen-Image-Lightning-4step-V1.0` (NFE4) maintain comparable performance. Comprehensive assessment across diverse test scenarios indicates that all three model configurations deliver acceptable generation quality within their designated operational parameters.

**Table 1: Basic Image Generation**
| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| 一个会议室，墙上写着"3.14159265-358979-32384626-4338327950"，一个小陀螺在桌上转动。 | ![111](https://github.com/user-attachments/assets/096885dd-09be-4259-8989-5120c442b136) | ![112](https://github.com/user-attachments/assets/d25b7437-d494-4eaa-8cb2-767587074301) | ![113](https://github.com/user-attachments/assets/7bd4c64c-8a79-4601-ba27-6c26a8be879b) |
|  | ✅"3.14159265-358979-32384626-4338327950" | ✅"3.14159265-358979-32384626-4338327950" | ✅"3.14159265-358979-32384626-4338327950" |
| 宫崎骏的动漫风格。平视角拍摄，阳光下的古街热闹非凡。一个穿着青衫、手里拿着写着“阿里云”卡片的逍遥派弟子站在中间。旁边两个小孩惊讶的看着他。左边有一家店铺挂着“云存储”的牌子，里面摆放着发光的服务器机箱，门口两个侍卫守护者。右边有两家店铺，其中一家挂着“云计算”的牌子，一个穿着旗袍的美丽女子正看着里面闪闪发光的电脑屏幕；另一家店铺挂着“云模型”的牌子，门口放着一个大酒缸，上面写着“千问”，一位老板娘正在往里面倒发光的代码溶液。 | ![121](https://github.com/user-attachments/assets/f13d8e40-653d-4d46-9f6d-029fd85e03e7) | ![122](https://github.com/user-attachments/assets/fbe24265-106a-4a86-84a2-dda4fe8bb15d) | ![123](https://github.com/user-attachments/assets/3864a8de-7798-41f1-88b9-f6a2fe08ee7e) |
| 一副典雅庄重的对联悬挂于厅堂之中，房间是个安静古典的中式布置，桌子上放着一些青花瓷，对联上左书“义本生知人机同道善思新”，右书“通云赋智乾坤启数高志远”， 横批“智启通义”，字体飘逸，中间挂在一着一副中国风的画作，内容是岳阳楼。 | ![131](https://github.com/user-attachments/assets/6207e422-8611-42f7-90b7-c5271964e501) | ![132](https://github.com/user-attachments/assets/7859aa72-6b93-44d7-a6fa-c7ed3f1b6a03) | ![133](https://github.com/user-attachments/assets/66b699b6-09ec-45b0-903b-4be6d2aa55f5) |
| A movie poster. The first row is the movie title, which reads “Imagination Unleashed”. The second row is the movie subtitle, which reads “Enter a world beyond your imagination”. The third row reads “Cast: Qwen-Image”. The fourth row reads “Director: The Collective Imagination of Humanity”. The central visual features a sleek, futuristic computer from which radiant colors, whimsical creatures, and dynamic, swirling patterns explosively emerge, filling the composition with energy, motion, and surreal creativity. The background transitions from dark, cosmic tones into a luminous, dreamlike expanse, evoking a digital fantasy realm. At the bottom edge, the text “Launching in the Cloud, August 2025” appears in bold, modern sans-serif font with a glowing, slightly transparent effect, evoking a high-tech, cinematic aesthetic. The overall style blends sci-fi surrealism with graphic design flair—sharp contrasts, vivid color grading, and layered visual depth—reminiscent of visionary concept art and digital matte painting, 32K resolution, ultra-detailed. | ![141](https://github.com/user-attachments/assets/1c2749ed-9b68-4f84-ad7a-196a64e9d2d6) | ![142](https://github.com/user-attachments/assets/d4f66d85-3ed5-442e-9ad9-8eca144cac10) | ![143](https://github.com/user-attachments/assets/5edb6340-03fa-4f1e-8131-b9c699f2818e) |
| 一张企业级高质量PPT页面图像，整体采用科技感十足的星空蓝为主色调，背景融合流动的发光科技线条与微光粒子特效，营造出专业、现代且富有信任感的品牌氛围；页面顶部左侧清晰展示橘红色Alibaba标志，色彩鲜明、辨识度高。主标题位于画面中央偏上位置，使用大号加粗白色或浅蓝色字体写着“通义千问视觉基础模型”，字体现代简洁，突出技术感；主标题下方紧接一行楷体中文文字：“原生中文·复杂场景·自动布局”，字体柔和优雅，形成科技与人文的融合。下方居中排布展示了四张与图片，分别是：一幅写实与水墨风格结合的梅花特写，枝干苍劲、花瓣清雅，背景融入淡墨晕染与飘雪效果，体现坚韧不拔的精神气质；上方写着黑色的楷体"梅傲"。一株生长于山涧石缝中的兰花，叶片修长、花朵素净，搭配晨雾缭绕的自然环境，展现清逸脱俗的文人风骨；上方写着黑色的楷体"兰幽"。一组迎风而立的翠竹，竹叶随风摇曳，光影交错，背景为青灰色山岩与流水，呈现刚柔并济、虚怀若谷的文化意象；上方写着黑色的楷体"竹清"。一片盛开于秋日庭院的菊花丛，花色丰富、层次分明，配以落叶与古亭剪影，传递恬然自适的生活哲学；上方写着黑色的楷体"菊淡"。所有图片采用统一尺寸与边框样式，呈横向排列。页面底部中央用楷体小字写明“2025年8月，敬请期待”，排版工整、结构清晰，整体风格统一且细节丰富，极具视觉冲击力与品牌调性。 | ![151](https://github.com/user-attachments/assets/a5edca6d-99c2-46de-a94a-2ab156773ecf) | ![152](https://github.com/user-attachments/assets/b417d3df-61c2-4450-b5d5-56e80611974c) | ![153](https://github.com/user-attachments/assets/11cb221c-9b68-4c40-b874-410c1d793a97) |




---

### 2. Text Rendering


Statistical analysis reveals performance differentiation primarily manifests in `challenging test cases`, particularly those involving dense small text rendering. The `NFE4` exhibits elevated failure rates compared to `NFE8` and `NFE100` when processing complex textual elements within generated images. 


**Table 2** presents a comparison of complex, dense text rendering among the three model. Results indicate that `NFE100` achieves the highest accuracy, whereas `NFE4` exhibits a greater frequency of typographical errors. In this example, NFE4 outputs the phrase "自动布局" twice and appends an extra "2".

#### **Table 2: Complex Text Rendering Performance**

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| 一个穿着"QWEN"标志的T恤的中国美女正拿着黑色的马克笔面相镜头微笑。她身后的玻璃板上手写体写着 “一、Qwen-Image的技术路线： 探索视觉生成基础模型的极限，开创理解与生成一体化的未来。二、Qwen-Image的模型特色：1、复杂文字渲染。支持中英渲染、自动布局； 2、精准图像编辑。支持文字编辑、物体增减、风格变换。三、Qwen-Image的未来愿景：赋能专业内容创作、助力生成式AI发展。” | ![211](https://github.com/user-attachments/assets/fa47db9d-640e-4795-ba0d-1ded2fe2b0a0) | ![212](https://github.com/user-attachments/assets/3492b14c-00cb-42a5-8e0f-0f008cc76401) | ![213](https://github.com/user-attachments/assets/92afeb4b-4f5b-42ec-86df-79634ebc98d9) |


---


### 3. Fine Detail Hair Preservation

This section evaluates the capability of the three models to preserve fine hair details, aiming to identify the performance gap between `NFE100` and its distilled variants. We use a prompt featuring a capybara with textual elements to assess both texture fidelity and detail retention.

**Table 3**  shows that `NFE100` consistently delivers superior fine hair detail preservation compared to its distilled counterparts (`NFE8` and `NFE4`), producing sharper and more natural hair textures while maintaining overall visual quality. 


#### **Table 3: Detail Hair Preservation Analysis**

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| A capybara wearing a suit holding a sign that reads Hello World. | ![311](https://github.com/user-attachments/assets/a252369b-9c48-424a-a559-368b412d70cb) | ![312](https://github.com/user-attachments/assets/e0675f8d-d0c8-4d1e-8875-eb04827ac1db) | ![313](https://github.com/user-attachments/assets/a80d8595-20cb-47ed-b322-8ae3a7626808) |


---

### 4. Multi-Element Scene Complexity


This section assesses the ability of the three models to handle highly complex scenes, using a neon-lit street scenario rich in visual and textual elements. The test includes numerous signs in both Chinese and English to evaluate performance in multi-element, detail-heavy environments.

**Table 4** illustrates that in highly complex scenarios, all three models may encounter generation challenges, indicating that complexity itself can be a limiting factor.

#### **Table 4: Multi-Element Scene Complexity**

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| "A vibrant, warm neon-lit street scene in Hong Kong at the afternoon, with a mix of colorful Chinese and English signs glowing brightly. The atmosphere is lively, cinematic, and rain-washed with reflections on the pavement. The colors are vivid, full of pink, blue, red, and green hues. Crowded buildings with overlapping neon signs. 1980s Hong Kong style. Signs include: "龍鳳冰室" "金華燒臘" "HAPPY HAIR" "鴻運茶餐廳" "EASY BAR" "永發魚蛋粉" "添記粥麵" "SUNSHINE MOTEL" "美都餐室" "富記糖水" "太平館" "雅芳髮型屋" "STAR KTV" "銀河娛樂城" "百樂門舞廳" "BUBBLE CAFE" "萬豪麻雀館" "CITY LIGHTS BAR" "瑞祥香燭莊" "文記文具" "GOLDEN JADE HOTEL" "LOVELY BEAUTY" "合興百貨" "興旺電器" And the background is warm yellow street and with all stores' lights on. | ![411](https://github.com/user-attachments/assets/680863bb-b6cd-49a3-96a7-27e9d706c309) | ![412](https://github.com/user-attachments/assets/e5d72387-01e2-456a-95a4-b0cf93e2e59a) | ![413](https://github.com/user-attachments/assets/82aad254-d39b-49e2-8a84-27230a73de65) |


---

### 5. Model Performance Variability

Analysis shows that while `NFE100` maintains the lowest overall bad case ratio, the distilled models (`NFE8` and `NFE4`) can outperform it in certain situations. For example, in the classroom prompt, `NFE100` produced a typo on the word "fundational," whereas both distilled models rendered the text correctly. This demonstrates that distillation does not uniformly reduce performance and may sometimes offer benefits in handling specific details. The results are presented in **Table 5**.


#### **Table 5: Model Performance Variability**


In certain test cases,  `NFE8` and `NFE4` performs better than `NFE100`.

| Prompt | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|
| A young girl wearing school uniform stands in a classroom, writing on a chalkboard. The text "Introducing Qwen-Image, a foundational image generation model that excels in complex text rendering and precise image editing" appears in neat white chalk at the center of the blackboard. Soft natural light filters through windows, casting gentle shadows. The scene is rendered in a realistic photography style with fine details, shallow depth of field, and warm tones. The girl's focused expression and chalk dust in the air add dynamism. Background elements include desks and educational posters, subtly blurred to emphasize the central action. Ultra-detailed 32K resolution, DSLR-quality, soft bokeh effect, documentary-style composition. | ![511](https://github.com/user-attachments/assets/23c69637-918a-42a6-8f92-e36da14ced39) | ![512](https://github.com/user-attachments/assets/b9f17e0a-38ee-4404-a7d2-8c9eea385123) | ![513](https://github.com/user-attachments/assets/5d566b6e-2751-4e17-ac04-5517f24a868d) |
| | "fundational" in image is wrong | ✅ | ✅ |


---

### 6. Resolution Impact

The results show that model performance can vary depending on resolution. In the `713×1280` case, `NFE100` struggles with accurately rendering a long numeric sequence, while both distilled models (`NFE8` and `NFE4`) handle it correctly. Conversely, at `1280×1280` resolution, `NFE100` and `NFE8` perform well, whereas `NFE4` fails to reproduce the sequence accurately. This demonstrates that resolution changes can improve or degrade performance depending on both base model and the distilled models. The visual results are demonstrated in **Table 6**.

#### **Table 6: Resolution Impact Analysis**

| Prompt | Resolution | Base NFE=100 | 8steps-V1.1 NFE=8 | 4steps-V1.0 NFE=4 |
|---|---|---|---|---|
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197". | 713 x 1280 | ![611](https://github.com/user-attachments/assets/24f0c053-5c91-4607-a1de-c2a717f2d321) | ![612](https://github.com/user-attachments/assets/0480f979-99e6-4762-8b7a-41eba2d72660) | ![613](https://github.com/user-attachments/assets/b50266bc-96b1-4820-af95-9bd19dd8a186) |
| | | ❌  "-238446264 -"> "-23846264" | ✅ | ✅ |
| A coffee shop entrance features a chalkboard sign reading "Qwen Coffee 😊 $2 per cup," with a neon light beside it displaying "通义千问". Next to it hangs a poster showing a beautiful Chinese woman, and beneath the poster is written "π≈3.1415926-53589793-23846264-33832795-02384197". | 1280 x 1280 | ![621](https://github.com/user-attachments/assets/a58c62a1-e079-42d3-a418-9e4ff6e738fb) | ![622](https://github.com/user-attachments/assets/ed36ebea-0535-43b4-82db-b55b1fc0f22e) | ![623](https://github.com/user-attachments/assets/f411310f-19a0-4477-8af0-ed536835f0a2) |
| | | ✅ | ✅ | ❌ |