#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 27 17:00:10 2018
Last Updated on Tue Aug 28 16:01:10 2018

@author: bhavani
"""

from skimage import io
img = io.imread("image.png")
io.imshow("image.png")
#io.show()

""" Writing or Saving an Image"""
io.imsave("new_image.png",img)

""" Data Module provides some standard test images """
from skimage import data
io.imshow(data.camera())
io.imshow(data.text())
io.show()

"""COlor module Contains methods to convert image from One to another color"""

from skimage import color
img = io.imread("BusinessCard.JPEG")
io.imshow("BusinessCard.JPEG")
gray = color.rgb2gray(img)
io.imshow(gray)
io.show()
io.imsave("Gray_BusinessCard.png",gray)

#Convert RGB to HSV
img = data.astronaut()
img_hsv = color.rgb2hsv(img)
io.imshow(img_hsv)
io.show()

""" Draw Modules : Circles, Eclipses, Polygons...etc """
import numpy as np
from skimage import io, draw
img = np.zeros((100,100),dtype = np.uint8)
x,y = draw.circle(50,50,10)
img[x,y] = 1
io.imshow(img)
io.show()

x,y = draw.ellipse(50,50,10,20)
img[x,y] = 1
io.imshow(img)
io.show()

r = np.array([10,25,80,50])
c = np.array([10,60,40,10])
x,y = draw.polygon(r,c)
img[x,y] = 1
io.imshow(img)
io.show()
