#coding=utf-8
#设置编码  
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding() 

#引入相关模块 
import url_manager,html_downloader,html_parser,html_outputer
#实例化相关模块 
urls = url_manager.UrlManager()
downloader = html_downloader.HtmlDownLoader()
parser = html_parser.htmlParser()
outputer = html_outputer.htmlOutputer()

class SpiderMain(object):
    
    def __init__(self): #初始化数据 
        self.urls = urls
        self.downloader = downloader
        self.parser = parser
        self.outputer = outputer

    def craw(self, root_url): #爬虫调度函数
        count = 1
        self.urls.add_new_url(root_url) #将主地址加入到新的地址库里面
        while self.urls.has_new_url(): #判断是否有新的url地址
            try:
                new_url = self.urls.get_new_url() #获取新的地址
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url) #下载html
                
                new_urls,new_data = self.parser.parse(new_url,html_cont) #解析html
               
                self.urls.add_new_urls(new_urls) #添加新的地址到新地址库
                self.outputer.collect_data(new_data)

                
                if  len(new_data['hotel_info'])  > 4:
                    self.urls.delete_url(new_url)
               

            except:
                print 'craw failed'
                #if count > 30:
                    #break
                count = count + 1

        self.outputer.output_html()

if __name__ == '__main__': #主程序入口
    root_url = 'http://hotels.ctrip.com/'
    obj_spider = SpiderMain()
    obj_spider.craw(root_url)










