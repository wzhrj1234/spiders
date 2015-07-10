# -*- coding: utf-8 -*-
"""
    爬虫，读取糗事百科热门第一页的内容，输出不带图片的每条内容的发布人，时间，内容，赞数
"""


import urllib
import urllib2
import re

page=1
url='http://www.qiushibaike.com/hot/page/'+str(page)
user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers={'User-Agent':user_agent}
try:
    request=urllib2.Request(url,headers=headers)
    response=urllib2.urlopen(request)
    #content=response.read().decode('utf-8')
    content=response.read()
    content=content.replace('\n','')
    content=content.replace(' ','')
    print "start to compile"
    
    pattern=re.compile('jpg"\/>(.*?)<\/a><\/div><divclass="content">(.*?)<!--(.*?)'+
    '--><\/div><divclass="stats"><spanclass="stats-vote"><iclass="number">(.*?)<\/i>')
    
    items=re.findall(pattern,content)
    print "start to print "
    for item in items:
        #去掉带图片的内容
        haveImg=re.search("img",item[2])
        if not haveImg:
            print item[0],item[2]
            print item[1]
            print item[3],"个赞"
            
except urllib2.URLError,e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason