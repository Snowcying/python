# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 17:16:32 2017

@author: 陈鑫一
"""

import re
import requests

def GetHTMLText(url):
    try:
        proxies = {
  "https": "http://58.251.76.29"
}
        r=requests.get(url,proxies=proxies)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "wrong"

def parsePage(ilt,html):
    try:
        time=re.findall(r'比计划晚点(\d小时)*(\d*分钟)*到达',html)
        #for i in range(len(time)):
         #   if i:
          #      ilt.append(time[i])
        if time[0]:    
            ilt.append(time[0])    
    except:
        print("cuowu")
        
def parsepage(ilt,html,i):
    time=re.findall(r'比计划晚点(\d小时)*(\d*分钟)*到达',html)
    if time[0]:
        ilt.append(time[0])
    else:
        print('第{}天'.format(i))
        
def main():
    start_url="http://www.variflight.com/schedule/CTU-TSN-GS7888.html?AE71649A58c77=&fdate=201708"
    day=25
    infoList=[]
    for i in range(day):
        try:
            if (i+1)%31<10:
                url=start_url+'0'+str(i+1)
                html=GetHTMLText(url)
                parsepage(infoList,html,i+1)
            else :
                url=start_url+str(i+1)
                html=GetHTMLText(url)
                parsepage(infoList,html,i+1)
        except:
            continue
        
    print(infoList)
    
main()
