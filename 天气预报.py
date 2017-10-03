# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 15:18:58 2017

@author: 陈鑫一
"""
import itchat
from itchat.content import *
#@itchat.msg_register(itchat.content.TEXT)
#def text_reply(msg):
#   return msg['Text']

itchat.auto_login()
itchat.send('Ok',toUserName='filehelper')

@itchat.msg_register([TEXT])
def text_reply(msg):
   itchat.send('%s:%s'%(msg['Type'],msg['Text']),msg['@ce5ba8c8c9e8a9f574417b990b5ba476dfb368e17adc2008dee1a4c2ddb698a4'])


#itchat.run()