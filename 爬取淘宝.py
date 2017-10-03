# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 12:04:33 2017

@author: 陈鑫一
"""

import requests
import re
import pandas
coutilt=[]
def getHTMLText(url):
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "wrong"
    
def parsePage(ilt,html):
    try:
        
        plt=re.findall(r'\"price\":\"[\d\.]*\"',html)
        tlt=re.findall(r'\"title\":\".*?\"',html)
        for i in range(len(plt)):
            tempdic={}
            price=eval(plt[i].split(':')[1])
            title=eval(tlt[i].split(':')[1])
            tempdic['价格']=price
            tempdic['商品名称']=title
            s=re.findall(r'戴尔',title)
            if s:   
                coutilt.append(tempdic)
            ilt.append([price,title])
    except:
        print("")
def printGoodList(ilt):
    tplt='{:4}\t{:8}\t{:16}'
    print(tplt.format("序号","价格","商品名称"))
    count=0
    for g in ilt:
        count=count+1
        print(tplt.format(count,g[0],g[1]))
def main():
    goods='笔记本电脑'
    depth=3
    start_url='https://s.taobao.com/search?q='+goods
    infoList=[]
    for i in range(depth):
        try:
            url=start_url+'&s='+str(48*i)
            html=getHTMLText(url)
            parsePage(infoList,html)
        except:
            continue
     
    printGoodList(infoList)
    df=pandas.DataFrame(coutilt)
    df.head(50)
    df.to_excel('淘宝.xlsx')
    
main()