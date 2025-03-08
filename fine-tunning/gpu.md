# GPU

## 主流卡

- A 架构（Ampere）：NVIDIA A100 / A800 / A40 / A30 / A16 / A10 / A2
- L 架构（Ada Lovelace）：NVIDIA L40S、GeForce RTX 4090
- H 架构（Hopper）：NVIDIA H100 / H800
- 最新的 B 架构（Blakwell）


## 英伟达卡的性能对比

| 型号 | 架构 | CUDA 核心数 | Tensor 核心数 | 显存 | 带宽 | NVLink | 用途 | 发布时间 |
| ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | ----- | 
| A100 | Ampere | 6912 | 432 | 40G/80G | 1.6TB/s | 支持 | AI 训练与推理，数据中心，科学研究 | 2022 年 |
| A800 | Ampere | 6912 | 432 | 40G/80G | 受限 | 受限 | 中国市场 AI 计算 | 2022 年 |
| H100 | Hopper | 16896 | 528 | 80G | 3.35TB/s | 支持 | AI 训练与推理，超大规模模型训练 | 2022 年 |
| H800 | Hopper | 16896 | 528 | 80G | 受限 | 受限 | 中国市场 AI 计算 | 2023 年 |
| H20 | Hopper | 未知 | 未知 | 96G | 4.0TB/s | 支持 | AI 推理，边缘计算、视频处理 | 2023 年 |

## 如何选择合适的显卡

- AI 训练：大规模深度学习训练（如 GPT、Transformer）推荐 H100 或 H800
- AI 推理：推荐 A100、A800，推理对带宽要求较低
- 科学计算 & HPC：H100 最优，A100 次之
- 中小规模计算：可以考虑 A800、H800 或 H20





**Reference**
- [一文带你看懂英伟达 A100、A800、H100、H20：谁是 AI 算力之王](https://mp.weixin.qq.com/s/IIuoIKX_N-9E2DaBawezfg)