import itchat

itchat.auto_login(hotReload=True)

user=itchat.search_friends(userName='@40bbb65cb4dea115550226167a5a97185c259718e22affef1905a7bec9073694')

userName=user['NickName']

print(userName)