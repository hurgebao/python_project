# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Fri Dec 28 14:08:55 2018

@author: admin
"""


import requests;
import datetime
from bs4 import BeautifulSoup
from selenium import webdriver
browser = webdriver.Firefox()
 

#url = 'https://mp.weixin.qq.com/mp/homepage?__biz=Mzk0NDAwMDExMA==&hid=26&sn=2053533ee6a807a3ddd80a8664e439bd&scene=18'
#url='http://mp.weixin.qq.com/s?__biz=Mzk0NDAwMDExMA==&amp;amp;mid=2247498260&amp;amp;idx=1&amp;amp;sn=b2c2fd09d4f39b596be932cc76156f6a&amp;amp;scene=19#wechat_redirect'
url='http://mp.weixin.qq.com/s?__biz=Mzk0NDAwMDExMA==&amp;mid=2247498260&amp;idx=1&amp;sn=b2c2fd09d4f39b596be932cc76156f6a&amp;chksm=c329e715f45e6e03d2aae346b3a88291880c1439856840d2645e9ffe0593525c9668e3827d20#rd'
#response = requests.get(url)
#response.encoding = 'utf-8'
##print("Status code:", response.status_code)
#soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.contents)

#str = response.text
#1、获取表头
#print(str)

browser.get(url)
active = browser.find_element_by_class_name  ('rich_media_content')
print(active) 