---
layout:     post
title:     NLP-Class
subtitle:   NLP
date:       2025-05-13
author:     SHK
header-img: img/post-bg-debug.png
catalog: true
tags: 
    - NLP
---



## L1

- **International Organization for Standardization**
  - Approximately **6000** languages on earth
  - **200~400** have a writing system
- Codes for languages 
  - **ISO 639-1 to ISO 639-6**
  - **-1:Zh ko ja fr en**
  - **-2:zho kor jpn fra eng**
- **ISO for countries ISO 3166-1 alpha-3**
  - **JPN CHN KOR IND FRA**
- wrting systems - nlp tools
  - Chinese for Japanese, Vietnamese(<17 c.)
  - Latin for Italian, Spanish, French, English, German

- Classification of writing systems
  - **Logographic systems: Sumerian, Maya, Chinese, Hieroglyphs**, . . .
    • **Syllabic systems: kanas, Cree,** . . .
    • **Alphabetical systems**
    	– **Abjads (only consonants): Hebrew, Arabic, ...**
    	– **Abugidas (consonants+vowels as obligatory markers): all Bhramic writing systems**, i.e., **Devanagari, Thai, Lao, Tamil, ...**
    – **Alphabets proper (consonants and vowels on the**
    **same footing): Latin, Cyrillic, ...**
    • Featural system:Korean

Spell: Vietnamese

- Segments in writing systems
  - Syllables
  - Words
  - Hyperwords or chunks
  - Sentences or paragraphs

Language$\neq$country$\neq$ ethnicity

## L2

### ASCII

• Computers were invented in the US.∗ 

• Consequently, the first texts written on computers were in English. 

• a, b, c... z, A, B, C, ..., Z, 0, 1..., 9, !, ?, ., :, ..., ,\<space\> ,+, -, *, /, =, ... 

•all of the codes:  64 = 2^6 < 26 + 26 + 10 + 10 + 10 + x < 128 = 2^7

A file is a sequence of bits. It is easy to segment a sequence of bits in smaller sequences of the same number of bits, e.g., 7. 

Each sequence of 7 bits will correspond to one character: **American Standard Code for Information Interchange (ASCII)**.

### 8-bit coeds

Arabic, Greek could afford to be coded on 8 bits. This just required a different meaning for the same codes.

### Problems with codes

Solution by using one and only one universal encoding (desired visualization for the above same sequence of bytes)

Unicode is a consortium of 

​	• large companies, associations, governments, individuals 

**promoting proposals for a universal representation for all possible writing systems**

### ISO 10646

The proposal by Unicode was **partially adopted** by the International Organization for Standardization (ISO).

**Each character in a writing system will have a unique number, called a codepoint.**

<img src="https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-04-29-at-09.25.54.45hvy3p05c.webp" alt="Screenshot 2025-04-29 at 09.25.54" style="zoom:50%;" />

- It deals with characters, not with languages.
- ISO 10646 gives only a formal description of the character. Glyphs are not included in the international standard. (glyphs 字形)
- ISO 10646 is **not an encoding scheme**, it is just a **numbering of characters** by codepoints (= integer).

### Glyphs, fonts

The appearance of a character is **given by the font** used.

Fonts that give a form for each character of ISO 10646 (abusively called Unicode) are called Unicode fonts.

### UTF-8

- UTF-8 is an encoding scheme using **variable-length** sequences of bytes of 8 bits.
- Use first bit to identify the length 
- 第一字节的高位标记了这是几字节的编码
- 后续字节都以 10 开头，表示是“续字节”

| **Unicode 范围**   | **字节数** | **字节表示方式（x 表示有效位）**    |
| ------------------ | ---------- | ----------------------------------- |
| 0x0000 - 0x007F    | 1字节      | 0xxxxxxx                            |
| 0x0080 - 0x07FF    | 2字节      | 110xxxxx 10xxxxxx                   |
| 0x0800 - 0xFFFF    | 3字节      | 1110xxxx 10xxxxxx 10xxxxxx          |
| 0x10000 - 0x10FFFF | 4字节      | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx |

### **例子：**

- **英文字符 A**
  - Unicode: U+0041
  - 二进制: 0100 0001
  - 因为小于 0x007F，直接用单字节：0100 0001 → 十六进制 0x41
- **汉字 中**
  - Unicode: U+4E2D
  - 二进制: 01001110 00101101
  - 属于 0x0800 - 0xFFFF → 用三字节编码：
    - 1110xxxx 10xxxxxx 10xxxxxx
    - 填入有效位后得到：11100100 10111000 10101101
    - 十六进制：0xE4 0xB8 0xAD

## L3

![](https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-19-at-17.09.43.4qrjt7suzr.png)

单词（words），词元（lemmas），特征（features），特征结构（feature structures）

英语书写系统的定义：单词是由blanks分隔的non-blank序列

不适用于：Arbic，Japanese，Chinese，Thai，Vietnamese



希腊书写系统（Greek writing system）的历史：在音节（syllabic）书写系统仍在使用时，用竖线（vertical bar）分隔单词。当书写系统转变为字母系统(alphabetic system)后，竖线消失了，单词之间不再有分隔。

拉丁(Latin)书写系统的历史：起初，单词由垂直居中的小点分隔(separated by a small dot vertically centered)。当罗马人开始受到希腊人的影响时，除了在官方石碑(steles)上，这个小点消失了，单词之间不再有分隔。

爱尔兰的抄写员开始对拉丁语中的单词进行分隔。

- 单词在不同书写系统中出现的方式不同
  - 日语/中文：单词间没有空格，句子结尾的标记（end-of-sentence marker）
  - Thai：单词之间没空白，没句尾标记
  - Arabic：单词之间没有真正的空格；每个字母有四种不同形式；

#### 单词定义

- General case：通过句子中的替换来定义 definition by commutation in a sentence
- Extreme case：definition in isolation 孤立条件下判断
- Term 术语：A group of words corresponds to a specific meaning in a specific field

#### Segmentation

不处理标点，按空格分开

#### Word tokenization

cutting a text into words, separating punctuation.

\>>> text = 'this is a sample of a text with 12 words in it.' 

\>>> re.sub('[.,:;!?]','\ <punc\>',text).split()

 ['this', 'is', 'a', 'sample', 'of', 'a', 'text', 'with', '12', 'words', 'in', 'it', '\<punc\>']

#### NLTK

`nltk.word_tokenize(text)`

标点按原形保留，不会变成（‘\<punc\>’）

### Word Forms

形态学（Morphology） is the field of linguistics（语言学） which studies the form of words.

#### Formal point of view 形式观点 前中后缀

- Prefixes: 波兰语（pl） pisac -> napisac.       imperfect->perfect
- suffixes: 食べる→食べます
- Infixes: 德语(de) laufen -> lief.  = run -> ran

#### 语言学（linguistic）的观点

- 变音（Mutations） 语音学：phonetics
  - tad -> ma zad
- 屈折变化Inflexion 形态学
  - Scharf ->Schafer 
- 完全重叠total reduplications（morph-synax）
- 部分重叠partial reduplications

#### 特征(Featural)观点

- Nouns: 根据 case, gender, number 变化
- Verbs：根据tense, mood, aspect, person ,gender ,number

#### Lemma词元 规范词形

日语：动词原形；Greek动词：第一人称单数；

阿拉伯语：三单；Ancient Greek，French，German，Spanish：不定式（infinitive for verbs）

一个词形可以由其词元，加上所有能将它与同一词元的其他形式区分开来的必要特征来表示。

- FORM
- LEMMA
- CATEGORY
- AGREEMENT 一致性，gender，number

### Morphological analysis 形态分析

It consists in giving the feature structure which describes a given word form.

输入word form，输出feature structure

<img src="https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-13-at-13.46.54.3yeo2pgbor.webp" style="zoom:50%;" />

### Lemmatization 词形还原

get the lemma from word form

### Morphological generation 形态生成

• Input: feature structure.
• Output: word form

### Conclusion

List of NLP tasks dealing with words and word forms:

- **Segmentation or word tokenization**: cutting into words;
- **Lemmatization**: assigning a lemma to a word form;
- **Morphological analysis**: giving the feature structure which describes a given word form (a lemma plus linguistic features);
- **Morphological generation**: generating a word form from a lemma plus linguistic features (usually given as a feature structure).

#### NLP Pipeline

cat text | segmentation | morphological analysis | syntactical analysis | named entity recognition | semantic analysis

## L4

![](https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-19-at-17.09.56.1sf9ppkv3u.png)

### 语言的词汇是如何组织的：

- Inflectional morphology  屈折形态学
- Parts of speech 词性（POS）
- Derivational morphology 派生形态学
- Lexical units 词汇单位

### Morphological Analysis

主要任务是：找出与一个词形（word form）相对应的词元(lemma)及特征集(feature set)

### Morphological Generation

lemma+feature -> word form

### Parts of speech (POS)

#### 历史

古希腊人最初区分：名词和动词

- 名词（nouns）和形容词（adjectives）没有区别。有些形容词可以用作名词
- Proper nouns专有名词和common nouns普通名词差别很大
- 每个单词应该只有一个类别

古希腊词汇分类：

- 不改变形式的词：不变词（invariable words）
- 改变的：
  - nouns change forms according to case （**declension**）
  - Verbs change forms according to tense (**conjugation** )

#### 方式1：

Interjection, 感叹词

Nouns (substantives and adjectives are in the same group),名词

Pronouns,代词

Participles (verbs from their root, but nouns because of cases),分词

Verbs,动词

Adverbs,副词

Prepositions,介词

Conjunctions 连词

#### 方式2:

Case but no tense: nouns

No case but tenses: verbs

Cases and tenses: participles 分词

No case and no tense: particles 小品词 如look up 中的up

#### 现代英语常用：**Penn Treebank**

###  定义词性（POS）的标准

- Abstract categories：动词有时态和语气，名词有格（cases）
- Position in a sentence: 在句中的位置。（德语）
- 有限Finite（封闭close） 无限Infinite（开放open）categories：是不是会出现新的单词

#### Close categories:  stop words

- 停用词，非常频繁

#### POS tagging 词性标注

日语POS  ChaSen,MeCab; 中文 KyTea

#### 标注方法

Dictionary approach字典法：将所有信息放入字典中

Machine Learning Approach：在已标注的语料库上训练学习设备

### Inflectional morphology 屈折形态学

In inflectional morphology, the **morpho-syntactic(形态句法)** category or **part of speech (POS)** **does not change from word form to word form**. We stay inside the same POS.

词性不变

### Derivational morphology 派生形态学

形态句法范畴或词性通常会发生编变化

table -> tabular; 

Long  -> to lengthen

形态上的不规则叫：anomaly

### Lexical Units

#### Groups of words

to translate, translate, translated, translator, translation

**与同义词（synonymy）的定义不同**

**类似于用Lemma表示不同的word forms，**

**lexical unit 可以代表 a set of words and their word forms** (Usually noted with small capital letters.)

TRANSLATE = to translate, , translate, translated, translator, translation

CHOICE = choose, chose, chosen, choice, choices, chooser, choosers

WEST = west, western, occidental

![](https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-19-at-22.02.20.6ikioesj12.webp)

![](https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-19-at-22.01.48.361su1b9cf.webp)

| **方面**       | **Lemma**                  | **Lexical Unit**                            |
| -------------- | -------------------------- | ------------------------------------------- |
| 是否有语义     | ❌ 不包含具体语义，只是形式 | ✅ 包含具体语义                              |
| 是否考虑词性   | ❌ 不一定                   | ✅ 明确包含词性                              |
| 是否区分多义词 | ❌ 不区分                   | ✅ 区分（一个 lemma 可能有多个 LUs）         |
| 举例           | choose、run、go            | run-v（奔跑）、run-v（运营）、run-n（比赛） |

lemma相同，lexical unit不一定相同

### HW1

upload python file NOT notebooks

.py.txt
