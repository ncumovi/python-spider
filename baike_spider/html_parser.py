#coding=utf-8
#设置编码  
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding() 

from bs4 import BeautifulSoup
import urlparse
import re

class htmlParser(object):
    
    def _get_new_urls(self, page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r"/item/([\s\S]*)")) #正则匹配相关链接
        for link in links:   #组装新的url 并返回新的URL
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)

        return new_urls

    def _get_new_data(self, page_url,soup):
        res_data = {}
        #url
        res_data['url'] = page_url

        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>

        title_node = soup.find('dd',class_='lemmaWgt-lemmaTitle-title').find('h1')  #找到对应节点
        res_data['title'] = title_node.get_text()   #获取文本

        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node = soup.find('div',class_='lemma-summary')
        res_data['summary'] = summary_node.get_text()

        return res_data

    def parse(self, page_url,html_cont):
        if page_url is None or html_cont is None:
            return

        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')  #用bs4解析html
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data #返回新的地址以及新的数据