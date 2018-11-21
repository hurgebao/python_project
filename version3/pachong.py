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
    pt_index=-1
    lr_index=-1
    yyb_index=-1
    i=0
    for t in soup_sub.findAll("tr"):
      try:
        j=t.findAll("td")
        if(i==0):
          for index in range(len(j)):
            if  '营业部' in j[index].text:
              yyb_index=index
            elif '融资融券' in j[index].text:
              lr_index=index
            elif '交易服务器' in j[index].text:
              pt_index=index
        else:
          #print(str(yyb_index)+","+str(pt_index)+","+str(lr_index)) 
          #print(j[0].text)
          if j[pt_index].text.strip()!="" and pt_index!=-1:
            pageFile0.write(k.string+","+j[pt_index].text+"\n")
          if j[lr_index].text.strip()!="" and lr_index!=-1:
            pageFile1.write(k.string+","+j[lr_index].text+"\n")
          if j[yyb_index].text.strip()!="" and yyb_index!=-1:
            pageFile2.write(k.string+","+j[yyb_index].text+"\n")
      except BaseException as e:
          print(e)
          pageFileerror.write(k.string+"数据解析错误td")
      i=i+1
  except BaseException as e2:
    print(e2)
    pageFileerror.write(k.string+"数据解析错误")
  #break
#pageFile.write(html)
pageFile0.close()
pageFile1.close()
pageFile2.close()
pageFileerror.close()
