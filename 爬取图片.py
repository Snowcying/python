# -*- coding: utf-8 -*-
"""
Created on Sun Aug 20 21:46:58 2017

@author: 陈鑫一
"""

import urllib.request
import os
from bs4 import BeautifulSoup
#这个是要爬取的网站地址
url ='https://pixabay.com/zh/photos/?hp=&image_type=&cat=&min_width=&min_height=&q=%E9%A3%8E%E6%99%AF&order=popular'
#先读取出我们要爬取的网址信息
res = urllib.request.urlopen(url)
html = res.read()
#构建一个BeautifulSoup对象
soup = BeautifulSoup(html,'html.parser', from_encoding='utf-8')
#找出所以'img'标签对应的值
result = soup.find_all('img')
links = []
index = 0
for content in result:
#担心下载太多（毕竟是测试）做了一个数量限制（我们做测试不需要爬取太多图片）
    if index < 10:
        s = content.get('srcset')
        if s is None:
           ss = s
        else:
           links.append(s.split(' ')[0])
    index+=1
#输出一共找出几个符合的图片地址
print(len(links))
#判断本地是否有photo这个路径，没有的话创建一个
if not os.path.exists('D:\photo'):
    os.makedirs('D:\photo')
#循环把图片下载到本地photo路径下
i = 0
#for循环 循环读取我们爬取到的 图片地址列表
for link in links:
    i+=1
    filename ='D:\\photo\\'+'photo'+str(i)+'.jpg'
    with open(filename,'w'):
        urllib.request.urlretrieve(link,filename)

