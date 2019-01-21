# -*- coding: utf-8 -*-
#!/usr/bin/python3
"""
Created on Fri Dec 28 14:08:55 2018

@author: admin
"""


import requests;
import datetime
from bs4 import BeautifulSoup
date_begin='var toshowDate'
date_length=20
header_begin='header:'
header_end='"停牌"]'
list_begin='list:'
list_end='};'
##去除空换行
def formatStr (str):
    str = str.replace('\'\',','').replace('\'','"').replace('\n','').replace('\t','')
    str = str.replace('\r','').replace('\r\n','')
    return str
def getHeader(str):
    start = str.find(header_begin)+len(header_begin)+1
    end=str.find(header_end)+len(header_end)
    str=str[start:end]
    str=formatStr(str)
    str=str[1:len(str)-1]
    titlelist=str.split('],[')
    header_str=''
    for title in titlelist:
            header_str=header_str+title[title.find(','):]
    return header_str[1:]
        
def getData(str):
    start = str.find(list_begin)+len(list_begin)
    str = str[start:]
    end = str.find(list_end)
    str = str[:end]
    str=formatStr(str)
    str = str.replace('"<div class="align_right">','"').replace('</div>','')
    end = str.find("\"\"");
    str = str[:end]
    end = str.rindex(',')
    str = str[1:end]
    return str

def getDate(str):
    start=str.find(date_begin)+len(date_begin)
    str=str[start:start+date_length]
    str=str[str.find('\'')+1:str.find(';')-1]
    return str.replace('-','');
    

url = 'http://www.sse.com.cn/assortment/options/disclo/preinfo/'
response = requests.get(url)
response.encoding = 'utf-8'
##print("Status code:", response.status_code)
soup = BeautifulSoup(response.text, 'html.parser')
#print(soup.contents)

str = response.text
#1、获取表头
headerlist=getHeader(str)
#print(headerlist)
#2、获取数据
datalist=getData(str)
datalist=datalist[1:len(datalist)-1]
dataarray=datalist.split('],[')
#now_time = datetime.datetime.strftime(datetime.datetime.now(),'%Y%m%d-%H')
now_time=getDate(str)
f = open('/home/www/optioncontract/option_contract_'+now_time+'.csv','w+',encoding="utf-8")
f.write('"数据日期",'+headerlist+'\n')
for data in dataarray:
    f.write('"'+now_time+'",'+data+'\n')
f.close()
