import numpy as np
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
import seaborn as sns
from torch.utils.data import DataLoader, TensorDataset

# 生成随机数据集
np.random.seed(42)
X_train = np.random.rand(500, 10)  # 500 个样本，每个样本 10 维
y_train = np.random.randint(0, 2, 500)  # 二分类标签

# 转换为 PyTorch Tensor
X_train_tensor = torch.tensor(X_train, dtype=torch.float32)
y_train_tensor = torch.tensor(y_train, dtype=torch.long)

# 构建 DataLoader
train_dataset = TensorDataset(X_train_tensor, y_train_tensor)
train_loader = DataLoader(train_dataset, batch_size=32, shuffle=True)

class TransformerEncoder(nn.Module):
    def __init__(self, input_dim, embed_dim, num_heads, ff_dim):
        super().__init__()
        self.self_attn = nn.MultiheadAttention(embed_dim, num_heads)
        self.ffn = nn.Sequential(
            nn.Linear(embed_dim, ff_dim),
            nn.ReLU(),
            nn.Linear(ff_dim, embed_dim)
        )
        self.norm1 = nn.LayerNorm(embed_dim)
        self.norm2 = nn.LayerNorm(embed_dim)

    def forward(self, x):
        attn_output, _ = self.self_attn(x, x, x)
        x = self.norm1(x + attn_output)
        ffn_output = self.ffn(x)
        x = self.norm2(x + ffn_output)
        return x
    
# 定义模型
model = TransformerEncoder(input_dim=10, embed_dim=10, num_heads=2, ff_dim=20)
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)
loss_fn = nn.CrossEntropyLoss()

# 训练循环
for epoch in range(10):
    for X_batch, y_batch in train_loader:
        optimizer.zero_grad()
        X_batch = X_batch.unsqueeze(1)  # 增加序列维度
        output = model(X_batch)
        loss = loss_fn(output.mean(dim=1), y_batch)
        loss.backward()
        optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.4f}")
    
# 生成随机注意力权重
attention_weights = np.random.rand(10, 10)
plt.figure(figsize=(6, 5))
sns.heatmap(attention_weights, cmap="coolwarm", annot=True)
plt.title("Self-Attention Heatmap")
plt.show()


