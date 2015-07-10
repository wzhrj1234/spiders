#coding:utf-8
"""
    一个Python爬虫，将廖雪峰教程所有页面保存下来到本地文件夹
"""

import urllib

domain='http://www.liaoxuefeng.com'     #廖雪峰的域名
path=r'C:\Users\hrj\Desktop\content\\'  #HTML要保存的路径

#一个HTML的头文件
input=open(r'C:\Users\hrj\Desktop\content\0.html','r')
head=input.read()

#打开Python教程主界面
f=urllib.urlopen('http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000')
home=f.read()
f.close()

#去掉空格回车，方便获取url
geturl=home.replace('\n','')
geturl=geturl.replace(' ','')

#获取所有教程的URL
list0=geturl.split(r'em;"><ahref="')[1:]

#加上第一个页面（观察HTML会发现就第一个页面之前不是'em;"><ahref="'）
list0.insert(0,'/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')

for li in list0:
    url=li.split(r'">')[0]
    url=domain+url
    print url
    f=urllib.urlopen(url)
    html=f.read()
    
    #获取每个教程标题
    title=html.split("<title>")[1]
    title = title.split(" - 廖雪峰的官方网站</title>")[0]

    #转码
    title = title.decode('utf-8').replace("/", " ")
    
    #截取正文
    html = html.split(r'<div class="x-wiki-content">')[1]
    html = html.split(r'</div>')[0]
    html = html.replace(r'src="', 'src="' + domain)
    
    #加头部尾部组成完整HTML
    html=head+html+"</div></body></html>"
    
    #输出文件
    output=open(path+"%d" %list0.index(li)+title+'.html','w')
    output.write(html)
    output.close()
    
