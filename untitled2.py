# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 17:46:37 2017

@author: 陈鑫一
"""

import itchat
itchat.auto_login()
itchat.send('ok',toUserName='filehelper')

#friendList = itchat.get_friends(update=True)
#发消息
#user = itchat.search_friends(name=u'表叔')[0]
#user.send(u'机器人say hello')

#发图片
#itchat.send('@img@%s'%'C:/上传素材/gz.gif' , toUserName=None)

#发视频
#itchat.send('@vid@%s'%'C:/上传素材/demo' , toUserName=None)

#发文档
#itchat.send('@fil@%s'%'C:/上传素材/xlsx.xlsx' , toUserName=None)


import requests
import itchat

KEY = '8edce3ce905a4c1dbb965e6b35c3834d'

def get_response(msg):
    apiUrl = 'http://www.tuling123.com/openapi/api'
    data = {
        'key'    : KEY,
        'info'   : msg,
        'userid' : 'wechat-robot',
    }
    try:
        r = requests.post(apiUrl, data=data).json()
        return r.get('text')
    except:
        return

@itchat.msg_register(itchat.content.TEXT)
def tuling_reply(msg):
    defaultReply = 'I received: ' + msg['Text']
    reply = get_response(msg['Text'])
    return reply or defaultReply

#itchat.auto_login(hotReload=True)
itchat.run()