.# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 17:03:35 2017

@author: 陈鑫一
"""
import re

s='戴尔 xps'

m=re.findall(r'[a-z]{3}',s)
if m:
    print(m)