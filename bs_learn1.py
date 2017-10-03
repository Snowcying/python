# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 16:19:10 2017

@author: 陈鑫一
"""

from bs4 import BeautifulSoup
import requests
import re
url="http://www.variflight.com/schedule/CTU-TSN-GS7888.html?AE71649A58c77=&fdate=20170818"
r=requests.get(url)
r.encoding=r.apparent_encoding
html=r.text
soup=BeautifulSoup(html,'html.parser')
time=soup.find_all('li',{'class':'age'})[0]
print(time.attr)