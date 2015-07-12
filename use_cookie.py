# coding:utf-8

"""
    使用cookie登入页面，限post登入的网站
"""
import urllib,urllib2,cookielib

class WEB:
    
    def __init__(self):
        #查找到要登录的URL
        self.loginUrl='******'
        self.cookies=cookielib.CookieJar()
        #查找到post使用的字段并填充
        self.postdata=urllib.urlencode({'log':'****','pwd':'****'})
        self.opener=urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cookies))
        
    def getPage(self):
        request=urllib2.Request(url=self.loginUrl,data=self.postdata)
        result=self.opener.open(request)
        print result.read()
        
web=WEB()
WEB.getPage()
