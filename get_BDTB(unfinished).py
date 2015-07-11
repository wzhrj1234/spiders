# -*- coding: utf-8 -*-
__author__='bluecat'
"""
    爬虫，读取百度贴吧帖子内容，原作者http://cuiqingcai.com/993.html
"""

import urllib
import urllib2
import re

#百度贴吧爬虫
class BDTB:
    #初始化，传入基地址和是否只看楼主参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)
        self.tool=Tool()
        
    #传入页码，获取
    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            html=response.read()
            html=html.replace('\n','')
            html=html.replace(' ','')
            return html     
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败",e.reason
                return None
                
    def getTitle(self):
        page=self.getPage(1)
        title=page.split(r'<spanclass="core_title_cate"></span>')[1]
        title=title.split(r'</h1>')[0]
        print title
        
    def getPageNum(self):
        page=self.getPage(1)
        f=open(r'E:\code\spiders\test.html','w')
        f.write(page)
        f.close()
        pattern=re.compile('<liclass="l_reply_num"style="margin-left:8px">'+
            '<spanclass="red"style="margin-right:3px">(.*?)<\/span>.*?<spanclass="red">(.*?)<\/span>')
        result=re.search(pattern,page)
        if result:
            print result.group(2).strip()
        else:
            return None
    
    def getContent(self,page):
        html=self.getPage(page)
        pattern=re.compile('<cc><divid="post_content_.*?"class="d_post_contentj_d_post_contentclearfix">(.*?)<\/div>')
        results=re.findall(pattern,html)
        for result in results:
            print self.tool.replace(result)


#处理页面标签类
class Tool:
    removeImg=re.compile('<img.*?>')
    removeAddr=re.compile('<a.*?>|</a>')
    replaceLine=re.compile('<tr>|<div>|</div>|</p>')
    repaceTD=re.compile('<td>')
    replacePara=re.compile('<p.*?>')
    replaceBR=re.compile('<br><br>|<br>')
    removeExtraTag=re.compile('<.*?>')
    def replace(self,x):
        x=re.sub(self.removeImg,'',x)
        x=re.sub(self.removeAddr,'',x)
        x=re.sub(self.replaceLine,'\n',x)
        x=re.sub(self.repaceTD,'\t',x)
        x=re.sub(self.replacePara,'\n  ',x)
        x=re.sub(self.replaceBR,'\n',x)
        x=re.sub(self.removeExtraTag,'',x)
        return x.strip()
    

baseURL='http://tieba.baidu.com/p/3750231995'
bdtb=BDTB(baseURL,1)
bdtb.getTitle()
bdtb.getPageNum()
bdtb.getContent(1)