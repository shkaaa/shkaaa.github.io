---
layout:     post
title:    Agentic RAG项目
subtitle:   LLM
date:       2025-05-14
author:     SHK
header-img: img/post-bg-debug.png
catalog: true
tags: 
    - NLP
---

# Agentic RAG

### 功能概述

利用同时具有推理和Function Call能力的LLM（Qwen3），实现对本地知识库的问答功能。支持对复杂问题的多部搜索。

### 基本架构

![Architecure](https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-19-at-15.49.18.5tr940ta6s.webp)

## Milvus 向量数据库

![Collection Explained](https://milvus.io/docs/v2.5.x/assets/collection-explained.png)

### 字段

一个DB有不同的Collection

Collectoin包含Entities和Fields

```python
schema.add_field("id", DataType.INT64, is_primary=True)
schema.add_field("embedding", DataType.FLOAT_VECTOR, dim=dim)
```

### 索引

密集向量，用欧氏距离L2或者内积IP

```
index_params = self.client.prepare_index_params()

index_params.add_index(field_name="embedding", metric_type=metric_type)
```



### 混合搜索

配置analyzer_params,配置分词器

```
schema.add_field(
                    "text",                    # 字段名：text
                    DataType.VARCHAR,          # 数据类型：变长字符串
                    max_length=text_max_length,# 最大长度：65535字符
                    analyzer_params=analyzer_params,  # 分析器参数配置
                    enable_match=True,         # 启用文本匹配功能
                    enable_analyzer=True       # 启用文本分析器
                )
```

稀疏向量 -- 存储文本的BM25特征，支持文本匹配搜索

```
schema.add_field("sparse_vector", DataType.SPARSE_FLOAT_VECTOR)
```

```
# 创建BM25函数
# BM25是一种基于概率的文本相似度算法，常用于信息检索
# 特点：
# 1. 考虑词频（TF）和逆文档频率（IDF）
# 2. 对长文本和短文本都有良好的处理能力
# 3. 支持关键词权重计算
bm25_function = Function(
         	name="bm25",                    # 函数名称
          function_type=FunctionType.BM25,# 函数类型：BM25算法
          input_field_names=["text"],     # 输入字段：文本字段
          output_field_names="sparse_vector" # 输出字段：稀疏向量
          )
# 将BM25函数添加到schema中
schema.add_function(bm25_function)
# 稀疏向量索引
index_params.add_index(
		field_name="sparse_vector",     # 字段名：稀疏向量
		index_type="SPARSE_INVERTED_INDEX", # 索引类型：稀疏倒排索引
		metric_type="BM25"             # 度量类型：BM25算法
)
```

### 创建集合

```python
self.client.create_collection(
 collection,                # 集合名称
 schema=schema,            # 数据模式，包含字段定义和函数配置
 index_params=index_params,# 索引参数，包含向量和文本的索引配置
 consistency_level="Strong",# 一致性级别：Strong表示强一致性，确保数据写入后立即可见
)
```

### 搜索

```python
# 执行混合搜索
# 使用RRF（Reciprocal Rank Fusion）排序器合并搜索结果
# RRF是一种用于合并多个排序结果的算法，特别适合混合搜索场景
# 工作原理：
# 1. 对每个排序结果中的文档赋予一个基于排名的分数
# 2. 分数计算公式：score = 1/(k + r)，其中：
#    - k是一个常数（通常为60）
#    - r是文档在排序中的位置
# 3. 将同一文档在不同排序中的分数相加
# 4. 根据最终分数重新排序
# 优点：
# 1. 能够有效平衡不同排序方法的结果
# 2. 对异常值不敏感
# 3. 不需要对原始分数进行归一化
# 4. 适合处理不同来源的排序结果
search_results = self.client.hybrid_search(
        collection_name=collection,
        reqs=[sparse_request, dense_request],
        ranker=RRFRanker(),  # 使用RRF排序器合并向量搜索和文本搜索的结果
        limit=top_k,
        output_fields=["embedding", "text", "reference", "metadata"],
        timeout=10,
        )
```

```python
# 混合搜索中的结果组
search_results = self.client.hybrid_search(
    collection_name=collection,
    reqs=[sparse_request, dense_request],  # 包含向量搜索和文本搜索请求
    ranker=RRFRanker(),
    limit=top_k
)
# 返回结果：
# - 第一个结果组：向量搜索的结果
# - 第二个结果组：文本搜索的结果
```

不是混合搜索，也可以使用批量搜索，得到的答案是结果组

## 改进点

### Agent Router -> Agent Planner

单Agent改进为Agentic Workflow

#### Q1: 查询一部小说中有多少人物



#### Q2: 
