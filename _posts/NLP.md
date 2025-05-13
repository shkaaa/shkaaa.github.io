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

morphology
