import itchat, time

itchat.auto_login(True)

SINCERE_WISH = u'祝%s新年快乐！'

friendList = itchat.get_friends(update=True)[1:]

for friend in friendList:
    
    # 如果是演示目的，把下面的方法改为print即可
    print(friend)
    for k,v in friend.items():
        
        
        print("key:"+k+",value:"+str(v))
    
#    itchat.send(SINCERE_WISH % (friend['DisplayName']
#        or friend['NickName']), friend['UserName'])
#    itchat.send(SINCERE_WISH % (friend['DisplayName']
#           or friend['NickName']), friend['UserName'])
#    print(friend['NickName'],friend['UserName'])
    time.sleep(.5)