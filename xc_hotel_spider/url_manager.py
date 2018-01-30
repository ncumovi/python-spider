#coding=utf-8
#设置编码  
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding() 

class UrlManager(object):
    
    def __init__(self):
        self.new_urls = set()
        self.old_urls = set()

    def add_new_url(self, url):
        if url is None:
            return
        if url not in self.new_urls and url not in self.old_urls: #如果传入的地址不在新地址库和旧地址库的话 就加入到新的地址库里面
            self.new_urls.add(url)

    def add_new_urls(self, urls):
        if urls is None or len(urls) == 0:
            return
        for url in urls:
            self.add_new_url(url)

    def has_new_url(self):
        return len(self.new_urls) != 0 #新地址库长度不为0 则返回true 否则返回false

    def delete_url(self,url):
        list_urls = list(self.new_urls)
        for i in list_urls:
            if url.find(i) != -1 or i.find(url) != -1:
               self.new_urls.remove(i)
        print self.new_urls

    def get_new_url(self):  #获取新的地址
        new_url = self.new_urls.pop() #从新的地址库里拿出一个地址
        self.old_urls.add(new_url) #同时把这个拿出来的地址放入到旧的地址库
        print 'url_manager'
        return new_url

    