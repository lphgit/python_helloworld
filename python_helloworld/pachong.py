#coding=utf-8
import urllib2
import re
import os
import socket 
def pachong(url , thref , ttitle):
    "我的第一个爬虫程序 url 是网页路径 ， href 是返回的连接 ， title 是标题"
    try:
        htmlfile = open("firstfile","a")
    except IOError:
        print "Error: 没有找到文件，或者读取文件失败"
        return '1'
    else:
        #print "建立文件成功"
        try:
#           url = input("please input a url\n")
            response = urllib2.urlopen(url, timeout = 10)
            #获取网页数据
        except urllib2.URLError, e:
            if isinstance(e.reason, socket.timeout): 
                print("Restart");
                return '2'
            else:
                #如果有错打印错误
                return '1'
        else:
            try:
                tem = response.read()
            except IOError:
                print "Error: 读取错误或者文件错误"
                return '1'
            else:
                print("firstfile")
                patter = re.compile(r'<a.+?class="j_th_tit ".+?>')
                nextPatter= re.compile(r'<a.+?class="next pagination-item ".+?>')
                nextlink = re.compile(r'.+?href="(?P<href>.+?)".+')
                #patter = re.compile(r'<a.+href="(?P<href>.+?)".+title="(?P<title>.+?)".+</a>')
                pattern= re.compile(r'.+?href="(?P<href>.+?)".+title="(?P<title>.+?)".+')

                Nextpage = nextPatter.findall(tem)
                #print Nextpage
                Nextlink = nextlink.search(Nextpage[0])
                os.environ['var']=str(Nextlink.group(1))
                os.system('echo $var > NextLink')
                print Nextlink.group(1)
                
                match = patter.findall(tem)
                for var in match:
                 #  print(var.decode('utf-8'))
                    tmatch = pattern.search(var)
                    thref.append(tmatch.group(1).decode('utf-8'))
                    ttitle.append(tmatch.group(2).decode('utf-8'))
                    htmlfile.write(tmatch.group(1)+'\n')
                    htmlfile.write(tmatch.group(2)+'\n')
                htmlfile.close()
                return Nextlink.group(1) 


refile = open('NextLink',"r+")
url = refile.read()
title = []
href  = []
while True:
    nexturl = pachong(url , href , title)
    if (nexturl == '1'):
        print("ERROR")
    elif(nexturl == '2'):
        url = refile.read()
    elif(nexturl == ''):
        break;
    else:
        url = nexturl

