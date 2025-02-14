# Model 

## 模型量化

### GPT-175B

- 拥有 1750 亿参数
- 至少需要 320GB 的半精度（FP16）格式存储空间
- 推理时间至少需要 5 个 A100 GPU，每个 GPU 配置 80GB 内存

## 模型压缩

### 模型蒸馏（Model Distillation）

`
将一个大型、性能较好的 "教师模型" 的知识迁移到一个小型、更高效的 "学生模型" 中，通过这种方式，学生模型可以在保持较高准确性和泛化能力的同时，减少参数数量和计算复杂度
`

#### 步骤

- 训练教师模型：首先训练一个大型的、性能较好的模型作为教师模型
- 生成软标签：利用教师模型的输出（通常是概率分布）作为软标签，而不是直接使用硬标签（真正输出的结果）
- 训练学生模型：使用这些软标签来训练学生模型，使其能够模仿教师模型的行为
- 优化损失函数：在训练过程中，通常会结合学生模型自身的损失和蒸馏损失，以确保学生模型不仅学习到输入数据的特征，还能捕捉到教师模型的 "隐含知识"

#### 优势

- 能够在不显著损失性能的情况下，显著减少模型大小和计算需求，特别适用于资源受限的设备

### 模型量化（Model Quantization）

`
通过减少模型参数和计算表示精度来压缩模型的技术，其主要目的是将浮点数参数转换为低精度整数，从而减少存储需求和计算成本
`

#### 种类

**训练后量化（PTQ）**

- 在模型训练完成后进行量化，通过统计分析确定最佳的量化比特数，并对全中和激活值进行量化
- 简单高效，不需要对训练过程进行修改
- 可能会导致一定的精度损失，因为量化过程没有考虑到训练过程中的动态变化

**量化感知训练（QAT）**

- 在训练的过程中加入量化操作，使模型在训练时就适应低精度的表示形式
- 在训练过程中动态调整量化参数，从而减少精度损失
- 更好的平衡压缩效果和模型性能，但训练过程更加复杂，需要更多的资源

**量化感知微调（QAF）**

- 在预训练模型的基础上进行微调，同时引入量化操作
- 可以快速适应特定任务的需求，同时减少模型的存储和计算开销，但性能不如 QAT 模型

#### 优势

- 能够在保持较高精度的同时显著减少模型的存储和计算需求

### 剪枝

`
通过移除神经网络中不重要的连接或神经元来减少模型复杂度
`

#### 分类

**非结构化剪枝**

- 随机地移出神经网络中的单个权重或连接
- 产生的稀疏结构在硬件上难以高效实现（硬件通常对规则的矩阵更友好）

**结构化剪枝**

- 按照一定规则移出整个神经元、滤波器或层
- 产生的稀疏结构更适合硬件加速，可以减少整个计算单元的负担

#### 局限

- 精度损失
- 训练复杂性：一些剪枝方法需要对训练过程进行修改，增加了训练的复杂性和计算资源
- 硬件依赖性：不同的平台对剪枝后的模型支持程度不同
- 模型依赖性：不同的模型对剪枝的敏感度不同


### 二值化

`
极端的量化技术，将神经网络中的权重和激活值限制在两个值（通常是 +1 和 -1）上
`

- 一个 32 位浮点数权重在二值化后只需要 1 位存储空间，这样存储空间减少了 32 倍






**Refeference**

- [DeepSeek R1 Distill models](https://x.com/jandotai/status/1884552022772662781?s=46&t=ulYQEDJ7GQSP3RJjsg3CJw)
- [DeepSeel 发布 R1 模型，好好恶补文章中提到的 "蒸馏" 技术](https://mp.weixin.qq.com/s/x5wWXdw65joiiHQkrgfi8w)
- [4000 字，深度解析 DeepSeek 的蒸馏技术](https://mp.weixin.qq.com/s/BDQ75O3MNePGmkFd5iscjw)
- [一文详解！模型压缩四剑客：量化、剪枝、蒸馏、二值化](https://mp.weixin.qq.com/s?__biz=MzkxMTEzNzQ3NA==&mid=2247487539&idx=1&sn=458b83e59c89962bf98d512dd027f43e&chksm=c1219f9ef65616884543512754e12a0815279d63673dafcb1c26e0ed0efacf180a0cff5b2d71&cur_album_id=3308295942525337604&scene=190#rd)
- [一文详解！模型压缩四剑客：量化、剪枝、蒸馏、二值化](https://mp.weixin.qq.com/s?__biz=MzkxMTEzNzQ3NA==&mid=2247487539&idx=1&sn=458b83e59c89962bf98d512dd027f43e&chksm=c1219f9ef65616884543512754e12a0815279d63673dafcb1c26e0ed0efacf180a0cff5b2d71&cur_album_id=3308295942525337604&scene=190#rd)
