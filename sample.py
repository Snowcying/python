# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 20:33:04 2017

@author: 陈鑫一
"""

from qqbot import QQBotSlot as qqbotslot, RunBot
							

								 
							

@qqbotslot
							

def onQQMessage(bot, contact, member, content):
							

    if content == '-hello':
							

            bot.SendTo(contact, '你好，我是QQ机器人')
							

    elif content == '-stop':
							

            bot.SendTo(contact, 'QQ机器人已关闭')
							
            bot.Stop()
							

								 
							

if __name__ == '__main__':
							

    RunBot()