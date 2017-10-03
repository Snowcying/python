# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:57:41 2017

@author: qcy
"""

#coding=utf8  
  
import requests  
import itchat  
  
KEY = '8edce3ce905a4c1dbb965e6b35c3834d' # 这里填拿到的key  
  
def get_response(msg):  
    apiUrl = 'http://www.tuling123.com/openapi/api'  
    data = {  
        'key'    : KEY,  
        'info'   : msg,  
        'userid' : 'wechat-robot',  
    }  
    try:  
        r = requests.post(apiUrl, data=data).json()  
#        print(r)  
        return r.get('text')  
    except:  
        return  
  
import time

def tuling_reply(addr):  
    weather_reply = '[自动天气预报]'+get_response(addr+'天气')
    print(weather_reply)
    
    #在下面填备注名
    user=itchat.search_friends(name=u'陈鑫一')  #输入发送人备注
    
    userName=user[0]['UserName']
    itchat.send(weather_reply,
     toUserName=userName)
#    toUserName='@@f0f3316ed551e6e1920353136e5aa0ab8e37b431f5237d3316b137582607dd48')

itchat.auto_login(hotReload=True)


#输入发送天气地点
addr_list = ['北京','上海','重庆','成都','宜宾','筠连','秦皇岛']
#for addr in addr_list:
 #   tuling_reply(addr)
    
    
    
    
import datetime

# 输入发送时间
sched_time = '2017/06/20 22:37:20'


started = 0

while 1:
    
    if 0 == started:
        
        # str(datetime.datetime.now())[0:19]
        
        now_str = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print(sched_time, ' ', now_str)
        if now_str == sched_time:
            started = 1
            print('T=5s, exec...',now_str)
            for addr in addr_list:
                tuling_reply(addr)
    #        time.sleep(24*60*60)
            time.sleep(5*3)
        else:
            print('sleep 1s')
            time.sleep(1)
    else:
        now_str = datetime.datetime.now().strftime('%Y/%m/%d %H:%M:%S')
        print('T=5s, exec...', now_str)
        time.sleep(5)
    