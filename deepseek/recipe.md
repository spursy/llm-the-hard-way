# DeepSeek

## DeepSeek-R1 Illustration

### How LLMs are trained

#### The gerneral recipe of creating a high-quality LLM over three steps?

![llm-flow](../pics/llm-flow.png)

- The language modeling step where we train the model to predict the next word using a massive amount of web data. This step results in a base model
- a supervised fine-tuning step that makes the model more useful in following instructions and answering questions
- a preference tuning step which further polishes its behavior and aligns to human preferences


#### DeepSeek-R1 Recap

![deepseek-qa](../pics/deepseek-qa.png)

`
DeepSeek-R1 generates one token at a time, except it excels at solving math and reasoning problems because it is able to spend more time  processing a problem through the process of generating thinking tokens that explain its chain of thought
`

### DeepSeek-R1 Traning Recipe

![deepseek-recipe](../pics/deepseek.png)

#### 1. Long chains of reasoning SFT data

`
This is a large number of long chain-of-thought examples (600,000 of them). These are very hard to come by and very expensive to label with humans at this scale.
`

#### 2. An interim high-quality reasoning LLM

`
It is significant not because it's a great LLM to use, but because it required so little labeled data alongside large-scale reinforcement learning resulting in a model that exels at solving reasoning problems.
`

`
The outputs of unnnamed speciallist reasining model can be used to train a model general model that can also do other, non-reasoning tasks, to the level users expect from a LLM.
`

#### 3. Creating reasoning models with large-scale refinforcement learning (RL)













**Reference**

-[图解 DeepSeek-R1](https://zhuanlan.zhihu.com/p/21175143007)