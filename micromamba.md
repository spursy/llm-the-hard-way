# Micromamba

`
一款快速、轻量级的包管理工具，可以用来轻松构建和管理软件环境
`

## 基本使用

- 查看版本

`
micromamba --version
`

- 添加软件源

`
// bioconda 是一个专门用于管理生物信息学相关软件的 Conda 频道，被看做是生物信息软件的 AppStore

conda config --add channels bioconda

// Conda-forge 是一个由社区驱动的 Conda 频道，提供大量开源软件包。被看作是一个用于各种软件提供 conda 包的社区项目和组织

conda config --add channels conda-forge

// 添加为最高优先级的通道

conda config --set channel_priority strict
`

- 创建环境

`
micromamba create -n myenv
`

- 激活环境

`
micromamba activate myenv
`

- 安装软件包

`
micromamba install fastp
`

- 退出环境

`
micromamba deactivate
`

## 使用文件配置

```
// 文件名是 env.yml

name: myenv
channels:
  - bioconda
  - conda-forge
dependencies:
  - qualimap=2.2
  - multiqc=1.12
```

```
micromamba create -y -n myenv -f env.yml
```

## 常见命令

```
alias ma="micromamba activate"
alias mda="micromamba deactivate"

function mmc { micromamba create -n $Args $Args}   # 创建环境
function mma { micromamba activate $Args }          # 激活环境
function mms { micromamba search $Args}           # 查找包
function mmi { micromamba install $Args}          # 安装包
function mmu { micromamba update $Args}           # 更新包
function mmr { micromamba remove $Args}           # 移除包
function mml { micromamba list}                # 查看安装包
function mmda { micromamba deactivate }            # 退出环境

```


