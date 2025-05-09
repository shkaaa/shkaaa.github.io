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
