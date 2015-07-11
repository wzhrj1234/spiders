# -*- coding: utf-8 -*-
__author__='bluecat'
"""
    爬虫，读取百度贴吧帖子图片
"""

import urllib,urllib2
import re
import os,os.path

#百度贴吧爬虫,爬帖子图片
class BDTB:
    #初始化，传入基地址和是否只看楼主参数
    def __init__(self,baseUrl,seeLZ):
        self.baseURL=baseUrl
        self.seeLZ='?see_lz='+str(seeLZ)
        
    #传入页码，获取
    def getPage(self,pageNum):
        try:
            url=self.baseURL+self.seeLZ+'&pn='+str(pageNum)
            request=urllib2.Request(url)
            response=urllib2.urlopen(request)
            html=response.read()
            html=html.replace('\n','')
            html=html.replace(' ','')
            print '获取第',pageNum,'页成功!'
            return html     
        except urllib2.URLError,e:
            if hasattr(e,"reason"):
                print u"连接百度贴吧失败",e.reason
                return None
                
    def getTitle(self):
        page=self.getPage(1)
        try:
            title=page.split(r'<spanclass="core_title_cate"></span>')[1]
            title=title.split(r'</h1>')[0]
            return title
        except IndexError:
            pattern=re.compile('<h3class="core_title_txtpull-lefttext-overflow"title="(.*?)"style')
            title=re.search(pattern,page)
            return title.group(1)
            
        
        
    def getPageNum(self):
        page=self.getPage(1)
        pattern=re.compile('<liclass="l_reply_num"style="margin-left:8px">'+
            '<spanclass="red"style="margin-right:3px">(.*?)<\/span>.*?<spanclass="red">(.*?)<\/span>')
        result=re.search(pattern,page)
        if result:
            return result.group(2).strip()
        else:
            return None
    
    #提取网址中图片，并存储到 path/帖子名 这个目录下
    def getjpg(self,path):
        pagenum=int(self.getPageNum())
        i=1
        pictures=[]
        while i<=pagenum:
            page=self.getPage(i)
            pattern=re.compile('<cc><divid="post_content_.*?"class="d_post_contentj_d_post_.*?">(.*?)<\/div>')
            results=re.findall(pattern,page)
            for result in results:
                pattern2=re.compile('src="(.*?jpg)"')
                pics=re.findall(pattern2,result)
                for pic in pics:
                    pictures.append(pic)                
            i+=1
        
        i=1    
        path=self.mkdir(path)
        for picture in pictures:
            u=urllib.urlopen(picture)
            html=u.read()
            filepath=os.path.join(path,str(i)+r'.jpg')
            f=open(filepath,'wb')
            f.write(html)
            f.close()
            i+=1

            
    def mkdir(self,path):
        path=path.strip()+self.getTitle()
        path=unicode(path,'utf-8')
        isExists=os.path.exists(path)
        if not isExists:
            os.makedirs(path)
        return path
        
        
        
baseURL='http://tieba.baidu.com/p/3644542586'
seeLZ=0
bdtb=BDTB(baseURL,seeLZ)
bdtb.getjpg('E:\code\spiders\storage\pic\\')