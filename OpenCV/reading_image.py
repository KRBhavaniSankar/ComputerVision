#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  6 10:36:59 2018

@author: bhavani
"""

import cv2
img = cv2.imread("image.jpg")
cv2.imshow("this is an image",img)
cv2.waitKey(0)
#cv2.destroyAllWindows()


