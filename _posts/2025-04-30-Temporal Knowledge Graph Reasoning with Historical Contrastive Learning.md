---
layout:     post
title:     4.30 Paper Reading
subtitle:   TKG paper
date:       2025-04-30
author:     SHK
header-img: img/post-bg-debug.png
catalog: true
tags: 
    - TKG
---



# Temporal Knowledge Graph Reasoning with Historical Contrastive Learning 4-30

- Unsqueezed ->加入一个维度

例如，在预测 “美国在*t*+1时刻与哪个国家进行谈判” 时，如果在*t*时刻之前，美国从未与俄罗斯进行过谈判，那么（美国，谈判，俄罗斯，*t*+1）这个事件对于当前查询（美国，谈判，？，*t*+1）来说，就涉及到非历史实体俄罗斯，在之前时间里美国和俄罗斯谈判相关的事件不存在，即属于非历史事件。

粗体**s**、**p**、**o**分别表示*s*、*p*、*o*的嵌入向量，其维度为*d* 。$\mathbf{E}\in\mathbb{R}^{|\mathcal{E}|\times d}$是所有实体的嵌入矩阵，其行表示各个实体*s*的嵌入向量。类似地，$\mathbf{P}\in\mathbb{R}^{|\mathcal{R}|\times d}$是所有关系类型的嵌入矩阵。<img src="./Screenshot 2025-04-30 at 16.39.47.png" alt="Screenshot 2025-04-30 at 16.39.47" style="zoom:67%;" />

### 历史事件集合

给定一个查询$q=(s,p,?,t)$，定义历史事件集合$\mathcal{D}_t^{s,p}$，相关的历史实体集合$\mathcal{H}_t^{s,p}$。
$$
\mathcal{D}_t^{s,p}=\bigcup_{k<t}\left\{ (s,p,o,k) \in \mathcal{G}_k \right\}
$$

$$
\mathcal{H}_{t}^{s, p}=\left\{o |(s, p, o, k) \in \mathcal{D}_{t}^{s, p}\right\}
$$

非历史实体 non-historical entities：
$$
\{(s, p, o', k) | o' \notin H_{t}^{s, p}, k<t\}
$$
给定查询*q*=(*s*,*p*,?,*t*)中历史实体的出现频率。
$$
\mathbf{F}_t^{s,p}(o)=\sum_{k<t}|\{o|(s,p,o,k)\in\mathcal{G}_k\}|
$$
显然 $\mathbf{F}_t^{s,p}\in \mathbb{R}^{|\mathcal{E}|}$

由于无法计算非历史实体的频率（非历史实体，没有出现在D中），所以把F变化为Z。
$$
Z_{t}^{s, p}(o)=\lambda \cdot\left(\Phi_{F_{t}^{s, p}(o)>0}-\Phi_{F_{t}^{s, p}(o)=0}\right)
$$
当Z<0时，表示非历史事件，不存在于图G中.

### 历史事件关系

$$
\mathbf{H}_{his}^{s,p} = \underbrace{\tanh\left( \mathbf{W}_{his} (\mathbf{s} \oplus \mathbf{p}) + \mathbf{b}_{his} \right) \mathbf{E}^T}_{\text{similarity score between } q \text{ and } \mathcal{E}} + \mathbf{Z}_{t}^{s,p}, \tag{6}
$$

潜在上下文向量（latent context vector）H, 用于对不同宾语实体的历史依赖程度进行评分。W是d*2d的大小，tanh之后，生成一个d维的向量（看作行向量）与转置后的E相乘，从而得到q和每个实体之间的关系。

Z帮助两个潜在上下文向量聚焦于历史/非历史事件，且不参与模型更新。

![image-20250430165926054](/Users/hongkunsong/Library/Application Support/typora-user-images/image-20250430165926054.png)

左侧部分从历史依赖和非历史依赖两个方面学习实体的分布情况。右侧部分展示了历史对比学习的两个阶段，其目的是识别高度相关的实体，并且输出一个布尔掩码向量。中间部分是基于掩码的推理过程，它将从两种依赖关系中学习到的分布情况与掩码向量相结合，从而生成最终结果。

**先学到一个概率分布， 在去学一个掩码**

定义预测概率和损失

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 17.00.36.png" alt="Screenshot 2025-04-30 at 17.00.36" style="zoom: 50%;" />

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 17.01.08.png" alt="Screenshot 2025-04-30 at 17.01.08" style="zoom: 50%;" />

o_i是给定查询*q*的真实对象实体，模型训练时通过调整参数使L*ce*最小化，来提高对不同类型事件中实体的预测准确性。

### 对比学习stage 1

**计算查询嵌入向量**：给定查询*q*，其嵌入向量v_q通过公式

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 17.08.27.png" alt="Screenshot 2025-04-30 at 17.08.27" style="zoom:50%;" />

计算得出。其中，MLP对查询q的信息进行编码，将查询中的主体实体*s*、关系*p*以及历史实体频率信息进行整合，经过*M**L**P*处理后对嵌入进行归一化并投影到单位球面上，为后续的对比训练做准备。

**定义相似查询集合**：设*M*表示一个小批量样本，*Q*(*q*)表示在小批量*M*中除查询*q*之外，布尔标签与$I_q$相同的查询集合。这个集合用于确定与查询*q*属于同一类别的其他查询。

对比学习损失

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 17.18.59.png" alt="Screenshot 2025-04-30 at 17.18.59" style="zoom: 50%;" />

### 阶段二：训练二元分类器。

当第一阶段的训练完成后，CENET 会冻结第一阶段中包括实体嵌入矩阵*E*、关系嵌入矩阵*P*以及它们的编码器在内的相应参数的权重。

然后，根据真实标签Iq，将查询嵌入向量v_q输入到一个线性层，使用交叉熵损失来训练一个二元分类器，这一过程无需赘述。现在，该分类器能够识别查询*q*中缺失的对象实体是否存在于历史实体集合中。

在推理过程中，会生成一个布尔掩码向量,用于根据预测的$\hat{I}_q$是否为真来确认是哪一类实体。

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 18.05.16.png" alt="Screenshot 2025-04-30 at 18.05.16" style="zoom:67%;" />

<img src="/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 18.18.46.png" alt="Screenshot 2025-04-30 at 18.18.46" style="zoom:67%;" />

![Screenshot 2025-04-30 at 18.19.27](/Users/hongkunsong/Library/Application Support/typora-user-images/Screenshot 2025-04-30 at 18.19.27.png)

![案例分析](https://raw.githubusercontent.com/xyjigsaw/image/master/upload/cenet_case_study_2023_03_02_10.png)