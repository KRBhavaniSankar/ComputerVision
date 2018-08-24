#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 15:36:40 2018

@author: bhavani
"""


from PIL import Image
from pytesseract import image_to_string


img = Image.open('light-absorb-reflect-text.png')

text = image_to_string(img)
