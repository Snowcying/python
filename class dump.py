# -*- coding: utf-8 -*-
"""
Created on Mon Jun  5 16:13:59 2017

@author: 陈鑫一
"""

import json

class Student(object):
        def __init__(self,name,age,score):
            self.name=name
            self.age=age
            self.score=score
   
def student2dict(std):
    return{
            'name':std.name,
            'age':std.age,
            'score':std.score
            }
         
s=Student('Bob',20,88)
print(json.dumps(s,default=student2dict))