# Day3_DeepGEMM

## 矩阵乘法

- 大模型的每一层神经网络本质都是矩阵变换，不管是输入的是文本还是图像，都是通过权重矩阵变换来实现特征提取，比如大家熟知的 Transformer，自注意力机制就是通过 Query,Key, Value 三个矩阵的乘法完成语义关联计算
- 矩阵乘法占了运行时长的 45% - 60%

`
直白的说，千亿参数规模的模型，90% 以上的计算量来自矩阵乘法。所以矩阵乘法的效率直接决定了模型推理和训练速度。
`

### 面临问题

- 模型结构各异导致矩阵大小差异性非常大，不同的长度序列具有不同的 shape、不同的 batch size，实际矩阵乘法有数百个形状
- 矩阵太大，没办法一次性饭放入到寄存器或内存缓存

`
GPU/TPU 的架构设计，都是高度针对矩阵乘法去优化的，以 NVDIA GPU 为例，其张量核心（Tensor Core）就是专门加速矩阵累加运算的，还有专门的 GPU 加速库 cuBLAS。
`

## DeepGEMM

### 简介

`
DeepGEMM 是一个支持 FP8 精度的高性能 GEMM（通用矩阵乘法）库，适用于矩阵和 MoE（Mixture of Experts，专用混合专家模型）计算。DeepGEMM 具有细粒度缩放功能，采用 CUDA 编写，使用轻量级即时（JIT）模块在运行时编译所有内核
`

### 特点

- 核心代码只有 300 行左右，最高可达 1358 TFLOPS
- 仅支持英伟达最新的 Hopper 架构的显卡 H800，不兼容老型号
- JIT（Just-In-Time）编译，在运行时会自动生成需要的代码，不需要配置环境，能快速部署

### 两级累加

`
存在的问题：大模型一般用 FP8 量化瘦身，目的是提速，虽然提取速度快，存储空间小，但是低精度带来误差累积，大模型中的矩阵乘法可能涉及数百万词乘法，误差会被指数级放大。
`

- 先做高精度乘法和累加，当高精度累加结果超过 FP8 范围时，再转回 FP8 存储，实现在速度和精度之间的平衡
- 不仅支持普通精度乘法，还支持混合专家模型 MoE

`
简单地说，普通的 AI 通常是稠密矩阵，MoE 因为不是全部激活，所以还会有稀疏矩阵，一般会分组计算，因此 MoE 中的矩阵乘法更加复杂
`

### 三种 GEMM 类型支持

- 常规稠密 GEMM：通过函数 deep_gemm.gemm_fp8_fp8_bf16_nt 调用，适用于常规矩阵乘法
- 分组 GEMM（连续布局，contiguous Layout）：针对 MoE 模型优化，仅对 M 轴分组，N 和 K 保持固定。这种设计适用于 MoE 专家共享相同形状的情况，将多个专家的 token 拼接成单一连续张量，适用于训练前向或推理预填充阶段。每个专家需对齐到 M 块大小。
- 分组 GEMM（掩码分组，Masked Grouped GEMM）：支持推理解码阶段，结合 CUDA Graph 适应动态 token 分配。

### 调度优化

`
DeepGEMM 遵循 CUTLASS 设计，其内核为 warp 专用，支持重叠式的数据移动，张量核心 MMA 指令和 CUDA 核心优化
`

- TMA（Tensor Memory Acceleration）：Hopper 架构的硬件特性，用于异步数据加载或移动（如 LHS 矩阵，缩放因子等），减少内存访问延迟
- 指令重叠：内核采用 warp-specialized 设计，允许数据移动、张量核心 MMA（矩阵乘法）指令和 CUDA 核心累加操作重叠
- FP8 微调：通过修改变以后二进制的 FFMA（融合乘加）指令，调整 yield 和 reuse 位，进一步提升性能
- 区块调度器：通过统一的调度器调度所有非分组和分组内核，栅格化（Rasterization）以增强 L2 缓存的复用/重用

这些优化使得 DeepGEMM 在大多数矩阵大小上由于专家调优的内核，同时保持代码简洁

### 与其它库对比

- CUTLASS: 功能强大但代码复杂，依赖大量模板和预编译，适合通用场景
- CuTe: 专注于张量操作抽象，灵活但需要较深理解
- DeepGEMM: 专注于 FP8 和 Hopper，代码简洁，易于学习和修改，适合特定需求（如 DeepSeek-V3 的 MoE 训练）

### MoE 中的 GEMM 场景

**Contiguous Layout**

- 适合训练或推理时把不同的 Expert 的 Token 数据按行连续拼接，有利于用 DeepGeMM 的分组功能一次性进行多组运算

**Masked Layout**

- 适合推理阶段，当 Export 间的 Token 数大多并不均匀或实时变化时，可通过一个 mask 来只计算有效行，从而减少无用的算力浪费

**Reference**

- [300 行代码的矩阵乘法把 H800 榨到冒青烟，一文告诉你 DeepGEMM 到底牛在哪儿](https://mp.weixin.qq.com/s/C-sMu9Yo5xpzuRyEo1TVlA)
- [GitHub DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)