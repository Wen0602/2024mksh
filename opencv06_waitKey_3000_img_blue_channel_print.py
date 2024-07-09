# -*- coding: utf-8 -*-
import cv2
#要先把圖檔,放在同一個目錄
#小心副檔名 檔案總管-檢視-(勾)附檔名
img = cv2.imread('MKSH.png')
b = img[:,:,0]#藍色channel
print(b)
cv2.imshow('opencv06',img)
cv2.waitKey(3000)#等案空白建
#等三秒鐘,不用按就離開
cv2.destroyAllWindows()#在關視窗
