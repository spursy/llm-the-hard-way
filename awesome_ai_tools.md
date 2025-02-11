# AWESOME AI TOOLS

## IDE (Extensions)

### Qodo

- [Qodo](https://app.qodo.ai/)

`Qodo Gen is your AI-powered coding assistant and mentor. Qodo helps you write, understand, test and review code with your team.

With tools for code generation, test workflowing, and AI chat, Qodo Gen helps developers write quality code that works as intended, with fewer bugs.
`

## Jan 

- [jan](https://jan.ai/)

`
Jan is an open source Chat-GPT-alternative that runs 100% offline
`

## unsloth

- [unsloth](https://unsloth.ai/)

`
一个开源的库，旨在加速大型语言模型（LLM）的微调，同时减少内存使用。通过优化反向传播和重写 PyTorch 模块来实现这一点。
`

### 优势

#### 提高训练速度

- 与传统方法相比，显著提高训练速，最多可讲训练时间缩短 5 倍
- 开启 Unsloth 后，Llama3-8B 的训练速度可提升 44.35%，训练时间可减少 30.72%

#### 减少内存占用

- 最大限度减少内存的占用，对于像 Llama-3 这样占用大量内存的模型尤其有利

#### 保证精度

- 采用精确计算方法，确保微调后的模型与经过训练的模型性能相当，精度损失为零

#### 易于使用

- 与 Hugging Face 生态兼容，可以很容易地与 transformers、perf、trl 等代码库结合使用，只需要修改模型的加载方式即可

## PEFT

**（Parameter-Efficient Fine-Tuning）一种参数高效微调技术，降低时间和计算资源的消耗**

- [peft](https://github.com/huggingface/peft)

### 目标

`
在不微调模型所有参数的情况下，使预训练语言模型适应各种下游应用程序。通过添加少量可训练的参数（如适配器或小模型模块）来适应新任务，而不是重新训练整个模块
`

## TRL

**（Transformer Refinforcement Learning）**

- [TRL](https://github.com/huggingface/trl)

### 作用

- 使用强化学习微调模型：使 RL 的步骤更容易和灵活，让每个人可以在自己的数据集和训练设置上用 RL 微调 LM（可使用此算法微调模型以生成正面电影评论、进行受控生成或江西的模型的毒性）
- 支持 PPO 算法
- 支持 PEFT 参数微调
- 全栈工具：可用于使用监督微调步骤（SFT）、奖励模型（RM）和近端策略优化（PPO） 以及直接偏好优化（DPO）等微调方法和对齐转换器语言和扩散模型
- 简化 LLM 微调：可以直接监督微调开放式 LLM，支持数据集格式，包括会话和指令格式，只对完成情况进行训练，忽略提示，打包数据集，提高训练效率

## XTuner

- [XTuner](https://github.com/InternLM/xtuner)

`
一款高效、灵活且功能齐全的工具包，用于微调大模型。旨在帮助企业快速调整这些模型以适应特定任务，同时应对资源密集性流程带来的挑战
`

### 特点

#### 高效性

- 支持在几乎所有 GPU 上进行 LLM 和 VLM 的预训练/微调
- 自动调整高性能算子，例如 FlashAttention 和 Triton 内核，以提高训练吞吐量

#### 功能齐全

- 支持连续训练、指令微调和 Agent 微调
- 支持使用预定义的模板与大型模型聊天

## FastLLM

- [FastLLM](https://github.com/ztxz16/fastllm)

### 特点

- 高性能：通过优化算法和底层实现，提升大模型的推理性能
- 跨平台：纯 c++ 实现，便于跨平台移植，比如在 android 上直接编译
- 多平台加速：ARM 平台支持 NEON 指令加速，X86平台支持 AVX 指令集加速，NVIDIA 平台支持 CUDA 加速
- 多种精度：支持浮点模型（FP32），半精度模型（FP16），量化模型（INT8， INT4）加速

## llama.cpp

- [llama.cpp](https://github.com/ggerganov/llama.cpp)

`
是 Facebook LLaMA 模型的 C/C++ 端口，用于在 CPU 机器上完成开源大模型的部署和使用。作为一个开源的 C/C++ 端口，允许用户在不使用 PyTorch 等深度学习框架的情况下，将 PyTorch 等训练产生的二进制文件进行转换，使其可在消费级 GPU/CPU 上运行大语言模型
`

- 推理性能优化：使用 C 语言编写的机器学习张量库 ggml，提高了推理过程中的性能
- 模型量化：将模型参数从 32 位浮点数转换为 16 位浮点数，甚至 8、4 位整数，以牺牲一定的模型精度来获取推理速度的提升






**Reference**
- [Run ai locally with jan](https://x.com/jandotai/status/1884870577359610312?s=46&t=ulYQEDJ7GQSP3RJjsg3CJw)