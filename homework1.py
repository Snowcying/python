# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 15:21:41 2017

@author: 陈鑫一
"""

f= open("d:\TEST.txt",'r')
for line in range(len(f.readlines())):
    lines=f.readline()
    print(lines)
#print(len(f.readlines()))