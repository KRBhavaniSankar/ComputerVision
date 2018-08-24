#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 24 10:20:25 2018

@author: bhavani
"""


try:
    import Image
except ImportError:
    from PIL import Image
import pytesseract

# Japanese and English text image to string
text =pytesseract.image_to_string(Image.open('BusinessCard.JPEG'), lang='jpn+eng')


