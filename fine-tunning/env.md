


```
micromamba create --name unsloth_env \
    python=3.11 \
    pytorch-cuda=12.1 \
    pytorch cudatoolkit xformers -c pytorch -c nvidia -c xformers \
    -y

micromamba activate unsloth_env

micromamba install "unsloth[colab-new] @ git+https://github.com/unslothai/unsloth.git"
micromamba install --no-deps trl peft accelerate bitsandbytes
```