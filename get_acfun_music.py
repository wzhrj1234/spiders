#coding:utf-8
"""
    爬虫，监测AcFun音乐榜单是否更新
"""

import urllib

domain='http://www.acfun.tv/u/454711.aspx#area=post-history'
path=r'E:\code\spider\acfun_music\\'

f=urllib.urlopen('http://www.acfun.tv/lite/list/#channel=105')
home=f.read()
f.close()

#content=home.replace('\n','')
#content=home.replace(' ','')

output=open(path+'test1.html','w')
output.write(home)
output.close()