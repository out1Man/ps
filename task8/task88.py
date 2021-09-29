# 图片合成视频
import cv2
import os

# 获取长度，宽度
img=cv2.imread("C:\\Users\\out Man\\Desktop\\ps_png\\2.png")
size=img.shape[:2]
# 指定编码器
forcc=cv2.VideoWriter_fourcc(*'mp4v')
# 保存格式，参数分别为filename,编码器，帧率，尺寸
out=cv2.VideoWriter("C:\\Users\\out Man\\Desktop\\ps_png1\\1.mp4",forcc,20,(size[1],size[0]))
# 写入视频
for i in range(2,2877):
    img = cv2.imread('C:\\Users\\out Man\\Desktop\\ps_png1\\'+str(i)+'.png')
    out.write(img)
out.write(img)
# 注意：尺寸一定要和图像保持一致，否则看不了视频
# 如果想改变保存视频尺寸，应该先把读入的图像的尺寸改变
