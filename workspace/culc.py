import cv2
import numpy as np
import math

kaizo=0.173#mm/piexl

len = 48.229308238993575
xy = abs(len)

#画像の中のix13~14間の長さ
midpoint_len = xy * kaizo

#実際の円周とix13~14の長さ
myCircumference = 53.0#mm
mymidpoint_len = 36.0#mm

#実際の長さとの尺度を計算
coff = mymidpoint_len/midpoint_len

#measure.pyで測った横幅
midpoint_width = 3.637#mm

#円周＝dπ
circumference = midpoint_width * math.pi

#画像の中の直径に尺度をかけ合わせて実際の値との比較
result = circumference * coff
len_diff = myCircumference - result

print('円周 : ' + '{:.03f}'.format(result))
print( '差 : ' + '{:0.3f}'.format(len_diff))