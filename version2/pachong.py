#coding(utf-8)
import urllib.request
from bs4 import BeautifulSoup
from urllib import parse

page=urllib.request.urlopen('http://www.chaoguwaigua.com/downloads/qszl.htm')
html=page.read()
#print(html);
pageFile0=open('0_pt.csv','w+',encoding="utf-8")
pageFile1=open('1_lr.csv','w+',encoding="utf-8")
pageFile2=open('2_yyb.csv','w+',encoding="utf-8")
pageFileerror=open('3_error.csv','w+',encoding="utf-8")
soup=BeautifulSoup(html,'html.parser',from_encoding='gb2312')
for k in soup.findAll("a"):
  try:
    print(k.string)
    sec_url="http://chaoguwaigua.com/downloads/"+format(parse.quote(k.string))+".htm"
    page_sub=urllib.request.urlopen(sec_url)
    html_sub=page_sub.read()
    soup_sub=BeautifulSoup(html_sub,'html.parser',from_encoding='gb2312')
    for t in soup_sub.findAll("tr"):
      try:
        j=t.findAll("td")
        #print(j[0].text)
        if j[0].text.strip!="":
          pageFile0.write(k.string+","+j[0].text+"\n")
        if j[1].text.strip!="":
          pageFile1.write(k.string+","+j[1].text+"\n")
        if j[2].text.strip!="":
          pageFile2.write(k.string+","+j[2].text+"\n")
      except BaseException as e:
          print(e)
          pageFileerror.write(k.string+"数据解析错误td")
  except BaseException as e2:
    print(e2)
    pageFileerror.write(k.string+"数据解析错误")
#pageFile.write(html)
pageFile0.close()
pageFile1.close()
pageFile2.close()
pageFileerror.close()
