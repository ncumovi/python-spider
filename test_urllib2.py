#coding=utf-8

import urllib2
import cookielib
import sys  

#设置编码  
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding()  



#url = 'https://ncumovi.github.io/'
url = 'http://www.baidu.com/'

print '第一种方法'.decode('utf-8').encode(type)
response1 = urllib2.urlopen(url)
print response1.getcode()
print len(response1.read())

print '第二种方法'.decode('utf-8').encode(type)
request = urllib2.Request(url)
request.add_header('user-agent','Mozilla/5.0')
response2 = urllib2.urlopen(request)
print response2.getcode()
print len(response2.read())


print '第三种方法'.decode('utf-8').encode(type)
cj = cookielib.CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
urllib2.install_opener(opener)
response3 = urllib2.urlopen(url)
print response3.getcode()
print cj
print response3.read().decode('utf-8').encode(type) #将网页以utf-8格式解析然后转换为系统默认格式 