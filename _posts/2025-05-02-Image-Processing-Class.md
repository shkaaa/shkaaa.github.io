---
layout:     post
title:     Image Processing Class
subtitle:   IP class
date:       2025-05-02
author:     SHK
header-img: img/post-bg-debug.png
catalog: true
tags: 
    - Image Processing
---

# Image Processing

## Math

### Eular

$$
e^{j\theta}=\cos \theta + j \sin \theta\\
\frac{d}{dt}e^{jwt}=jwe^{jwt}\\
\int e^{jwt}=\frac{1}{jw}e^{jwt}+C\\
$$

逆时针遍历单位圆一周 

### Q1

<img src="https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-02-at-10.32.06.1e8ta5nihj.webp" alt="Screenshot-2025-05-02-at-10.32.06.1e8ta5nihj" style="zoom: 33%;" />

### Q2

calculate bit size of image & video

Value Range: 0~255 = 8 bit/pixel

Image Size = ColorNum * pixels * **log_2 (ValueRange)**

Video size = bands * pixels * AllFrames *  **log_2 (ValueRange)**

- RGB color distance: same distance in color space varies in the color difference people seeing.

$$
C=1-R;c=255-r
$$

RGB转CMY要用 $c=2^n-1-r$

<img src="https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-02-at-13.40.26.sz5o1j7py.webp" alt="https://shkaaa.github.io/picx-images-hosting/Screenshot-2025-05-02-at-13.40.26.sz5o1j7py.webp" style="zoom: 33%;" />

- RGB to YIQ: directly multiply the transform matrix, and make the answer to integer:
  - The answer should $\geq$0
  - eg: Y=round(Y'), I = round(I'+8), Q=round(Q'+8)

### Q3

Aliasing Errors: sampling frequency is less than $2\times \Omega_{max}$

Signal-to-Noise ratio: 
$$
SN=10\log_{10}\frac{P_{signal}}{P_{noise}}
$$

### Q4

傅立叶变换 连续

### Q5

离散傅立叶变换公式
$$
X(u, v) = \sum_{x=0}^{M-1} \sum_{y=0}^{N-1} f(x, y) \cdot e^{-j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}
$$
Inverse DFT
$$
f(x, y) = \frac{1}{MN} \sum_{u=0}^{M-1} \sum_{v=0}^{N-1} X(u, v) \cdot e^{j 2\pi \left( \frac{ux}{M} + \frac{vy}{N} \right)}
$$
