# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 11:36:32 2017

@author: 陈鑫一
"""

import datetime
sched_Timer=datetime.datetime(2017,6,10,21,24,10)

#def run_Task():
 #   print('1 minutes')


flag=0
while True:
    Now=datetime.datetime.now()    
    if Now==sched_Timer:
        print('1 min')
        flag=1
    else:
        if flag==1:
            sched_Timer=sched_Timer+datetime.timedelta(minutes=1)
            flag=0
            
        