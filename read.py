# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 14:51:46 2017

@author: 陈鑫一
"""

try:
    f=open('F:/Anaconda/cxy.txt','r')
    print(f.read())
finally:
    if f:
        f.close()
        
with open('F:/Anaconda/cxy.txt','r') as f:
    print(f.read())
    
p=open('F:/Anaconda/photo.jpg','rb')
p.read()    