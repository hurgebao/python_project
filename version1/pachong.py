#coding(utf-8)
import urllib.request

page=urllib.request.urlopen('http://www.chaoguwaigua.com/downloads/qszl.htm')
html=page.read()
#print(html);
pageFile=open('pageCode.txt','wb+')
pageFile.write(html)
pageFile.close()
