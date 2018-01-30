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
        #if (soup.find('div',id='nearbyPopCity')) is None:
             #return
        #links = soup.find('div',id='nearbyPopCity').find_all('a',href=re.compile(r"/hotel/")) #正则匹配相关链接
        links = soup.find_all('a',href=re.compile(r"(/hotel/[^/^?^.]+$)|(/hotel/([a-z]|[A-Z])*\d*/p\d$)")) #正则匹配相关链接
        if links is None:
            return
        for link in links:   #组装新的url 并返回新的URL
            new_url = link['href']
            new_full_url = urlparse.urljoin(page_url,new_url)
            if new_full_url.find('m.ctrip.com') == -1:
                new_urls.add(new_full_url)
            
        return new_urls

    def _get_new_data(self, page_url,soup):
        
        res_data = {}
        #url
        res_data['url'] = page_url
       
        #<dd class="lemmaWgt-lemmaTitle-title"><h1>Python</h1>
       
        title_node = soup.find('div',class_='seo_pic') #找到对应节点
       
        if title_node is None:
            return
        title_node_h4 = title_node.find('h4')
        
        #<div class="lemma-summary" label-module="lemmaSummary">
        summary_node_lists = soup.find('div',id='hotel_list').find_all('div',class_='hotel_new_list')
        hotel_infos = []
        n = 0; #酒店个数 限制不超过10个
        for index in range(len(summary_node_lists)):
            hotel_info = {}
            hotel_info['img'] = urlparse.urljoin(page_url,summary_node_lists[index].find('img')['src']) # 酒店图片
            hotel_info['name'] = summary_node_lists[index].find('h2').find('a').get_text() # 酒店名称
            hotel_info['address'] = summary_node_lists[index].find('p',class_='hotel_item_htladdress').get_text() # 酒店地址
            hotel_info['rato'] = summary_node_lists[index].find('span',class_='hotel_value').get_text()# 酒店评分
            hotel_info['price'] = summary_node_lists[index].find('span',class_='J_price_lowList').get_text()# 酒店价格
           
            if n > 4:
                break
            else:
                if  int(hotel_info['price']) <= 300:
                    hotel_infos.append(hotel_info)
                    n = n + 1
        #当有具体酒店时再显示酒店名称
        if hotel_infos != []:
            res_data['title'] = title_node_h4.get_text()   #获取文本
        else:
            res_data['title'] = None
        #print  hotel_infos
        res_data['hotel_info'] = hotel_infos
        #res_data['summary'] = summary_node.prettify() #格式化输出 带标签的可解析
        #res_data['summary'] = summary_node.get_text() #格式化输出 带标签的可解析
        return res_data

    def parse(self, page_url,html_cont):
        if page_url is None or html_cont is None:
            return
  
        soup = BeautifulSoup(html_cont,'html.parser',from_encoding='utf-8')  #用bs4解析html
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)

        print 'html_parse'   

        return new_urls,new_data #返回新的地址以及新的数据