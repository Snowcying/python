# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 16:55:07 2017

@author: 陈鑫一
"""

import itchat
from itchat.content import *

itchat.auto_login()
itchat.send('ok',toUserName='filehelper')

@itchat.msg_register(TEXT)
def self_reply(msg):
    
    #user=itchat.search_friends(name=u'皮皮怪')
    #userName=user[0]['UserName']
    
    #itchat.send(msg['Text'],userName)
    return 'I receive it \n %s' % msg['Text']

itchat.run()