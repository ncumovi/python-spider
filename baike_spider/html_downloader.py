#coding=utf-8
#设置编码  
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding() 

import urllib2

class HtmlDownLoader(object):
    def download(self, url):
        if url is None:
            return None

        request = urllib2.Request(url) #使用python自带模块 下载html
        request.add_header('user-agent','Mozilla/5.0')
        response  = urllib2.urlopen(request)

        if response.getcode() != 200:
            return None

        return response.read() #返回数据