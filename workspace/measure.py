import cv2
import numpy as np
import math
import math


#ハードコーディングで記載しているので、upload_file的なものに保存しに行きたい。
file_name='results/sample.jpg'
#ここが機種依存になるのでこれの自動化もできればしたい。
kaizo=0.173#mm/piexl
img=cv2.imread(file_name,cv2.IMREAD_GRAYSCALE)

image_hight, image_width = img.shape

cv2.namedWindow('measure', cv2.WINDOW_NORMAL)

x1,y1=0,0
counter=1

#ランドマーク推定に使った写真の指の測定ポイントを計算
x = 297.80667304992676
y = 265.06588339805603

midpoint_x = math.floor(x)
midpoint_y = math.floor(y)

#ランドマーク推定に使った画像ix13,14の2次元座標の距離をmmに計算
len = 48.229308238993575
xy = abs(len)
midpoint_len = xy * kaizo


def click_length(event, x, y, flags, params):

    global x1,y1,img2,counter,kaizo

    if event == cv2.EVENT_LBUTTONDOWN:
        counter=0
        x1=x
        y1=y

    elif event == cv2.EVENT_MOUSEMOVE and counter==0:

        img2=np.copy(img)
        cv2.circle(img2,center=(x1,y1),radius=3,color=255,thickness=-1)
        cv2.line(img2,(x1,y1),(x,y),255, thickness=1, lineType=cv2.LINE_4)
        cv2.imshow('measure', img2)

    elif event == cv2.EVENT_RBUTTONDOWN:

        counter=1
        img3=np.copy(img2)
        x2=x
        y2=y
        piexl=math.sqrt((x1-x2)**2+(y1-y2)**2)
        length=round(piexl*kaizo,3)
        length_str=str(length)+'mm'
        cv2.circle(img3,center=(x2,y2),radius=3,color=255,thickness=-1)
        cv2.putText(img3,length_str,(30, 50),cv2.FONT_HERSHEY_PLAIN,2,100,2,cv2.LINE_AA)
        cv2.imshow('measure', img3)




cv2.circle( img, center = (midpoint_x, midpoint_y), radius = 3, color = 255, thickness=-1)
cv2.putText(img, f'{midpoint_len}', (0, 700), cv2.FONT_HERSHEY_PLAIN, 2, (100,100,100), 2, 4)
cv2.imshow('measure', img)
cv2.setMouseCallback('measure', click_length)
cv2.waitKey(0) & 0xFF == 27
cv2.destroyAllWindows()
