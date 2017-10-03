# -*- coding: utf-8 -*-
"""
Created on Sat Jun 10 22:03:44 2017

@author: qcy
"""

import datetime
import time


sched_time = '2017/06/20 22:21:20'


started = 0

while 1:
    
    if 0 == started:
        
        # str(datetime.datetime.now())[0:19]
        
        now_str = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(sched_time, ' ', now_str)
        if now_str == sched_time:
            started = 1
            print('T=5s, exec...',now_str)
    #        time.sleep(24*60*60)
            time.sleep(5)
        else:
            print('sleep 1s')
            time.sleep(1)
    else:
        now_str = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print('T=5s, exec...', now_str)
        time.sleep(5)
