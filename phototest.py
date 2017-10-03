# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 17:27:27 2017

@author: 陈鑫一
"""

from PIL import Image,ImageFilter
im=Image.open('F:/Anaconda/photo.jpg')
w,h=im.size
im2 = im.filter(ImageFilter.BLUR)
im2.save('blur.jpg','jpeg')