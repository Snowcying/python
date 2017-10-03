# -*- coding: utf-8 -*-
"""
Created on Sat Jul 29 10:09:25 2017

@author: 陈鑫一
"""

import requests
import re
Url='http://oj.acmclub.cn/contestrank.php?cid=1111'
r=requests.get(Url)
#print(r.encoding)
r.encoding=r.apparent_encoding
demo=r.text
from bs4 import BeautifulSoup
soup=BeautifulSoup(demo,"html.parser")
#print(soup.prettify())
#print(soup.title,'\n')
#print(soup.a)
#print(soup.b.string)
temp=soup.find_all(string=re.compile('CS-'))
temp1=soup.find_all(href=re.compile('status.php?'))
print(temp1)