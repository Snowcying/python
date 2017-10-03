# -*- coding: utf-8 -*-
"""
Created on Mon Aug  7 22:23:07 2017

@author: 陈鑫一
"""

import requests
import re
import traceback
from bs4 import BeautifulSoup

def getHTMLText(url):
    try:
        r=requests.get(url)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return ""

def getStockList(lst,stockURL):
    html=getHTMLText(stockURL)
    soup=BeautifulSoup(html,'html.parser')
    a=soup.find_all('a')
    for i in a:
        try:
            href=i.attrs['href']
            lst.append(re.findall(r'[s][hz]\d{6}',href)[0] )  #findall 找出来的是一个列表，所以要[0]才能储存
        except:
            continue

def getStockInfo(lst,stockURL,fpath):
    for stock in lst:
        url=stockURL+stock+'.html'
        html=getHTMLText(url)
        try:
            if html =='':
                continue
            infoDict={}
            soup=BeautifulSoup(html,'html.parser')
            stockInfo=soup.find('div',attrs={'class':'stock-bets'})
            
            name=stockInfo.find_all(attrs={'class':'bets-name'})[0]
            infoDict.update({'股票名称': name.text.split()[0]})
            
            keylist=stockInfo.find_all('dt')
            valuelist=stockInfo.find_all('dd')
            
            for i in range(len(keylist)):
                key=keylist[i].text
                value=valuelist[i].text
                infoDict[key]=value
                
            with open(fpath,'a',encoding='utf-8') as f:
                f.write(str(infoDict)+'\n')
        except:
            traceback.print_exc()
            continue
        
        
def main():
    stock_list_url='http://quote.eastmoney.com/stocklist.html'
    stock_info_url='https://gupiao.baidu.com/stock/'
    output_file='D:/BaiduStockInfo.txt'
    slist=[]
    getStockList(slist,stock_list_url)
    getStockInfo(slist,stock_info_url,output_file)
    
main()