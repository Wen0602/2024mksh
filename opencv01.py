# -*- coding: utf-8 -*-
import cv2#使用OpenCV的外掛
#匯入cv2

img = cv2.imread('onepiece.png')
#小心副檔名
cv2.imshow('opencv01',img)
cv2.imshow('hello',img)
cv2.imshow('mksh',img)

cv2.waitKey(0)#等待任意鍵
#File-New Ctrl-N開新黨
#存在桌面的 opencv01.py
#不要執行,會當掉
#存在桌面的opencv01.py 


