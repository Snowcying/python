# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 16:18:35 2017

@author: 陈鑫一
"""

import requests
from bs4 import BeautifulSoup
import bs4
import pandas
unilist=[]
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def fillUnivList(ulist,html):
    soup=BeautifulSoup(html,"html.parser")
    for tr in soup.find('tbody').children:
        if isinstance(tr,bs4.element.Tag):
            tds=tr('td')
            dic={}
            #print(tds[0])
            ulist.append([tds[0].contents[0].string,tds[1].contents[0].string,tds[2].contents[0].string,tds[3].contents[0].string])
            dic['排名']=tds[0].contents[0].string
            dic['学号']=tds[1].contents[0].string
            dic['姓名']=tds[2].contents[0].string
            dic['完成题目数量']=tds[3].contents[0].string
            unilist.append(dic)

def printUnivList(ulist,num):
    print("{:^10}{:^10}{:^10}{:^10}".format("排名","学号","姓名","完成题目数量"))
    for i in range(num):
        u=ulist[i]
        print("{:^10}{:^10}{:^10}{:^10}".format(u[0],u[1],u[2],u[3]))
        
def makeExcel(unilst):
    df=pandas.DataFrame(unilist)
    df.head(50)
    df.to_excel('oj完成数量.xlsx')
    
def main():
    uinfo=[]
    url= 'http://ncc.neuq.edu.cn/oj/contestrank.php?cid=1160'
    html=getHTMLText(url)
    fillUnivList(uinfo,html)
    printUnivList(uinfo,20) #20 uni
    makeExcel(unilist)
    
main()