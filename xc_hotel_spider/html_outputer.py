#coding=utf-8
#设置编码  
import sys 
reload(sys)  
sys.setdefaultencoding('utf-8')  
#获得系统编码格式  
type = sys.getfilesystemencoding() 

class htmlOutputer(object):
    def __init__(self):
       self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data) 

    def output_html(self):
        
        print 'out_html'   

        fout = open('output.html','w')  #文件输出对象 w写模式

        fout.write('<html>')
        fout.write('<head>')
        fout.write('<link rel="stylesheet" href="./css/outerputer.css">')
        fout.write('<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<h1>全国城市酒店top10</h1>')
        fout.write('<table border="1" class="table table-striped">')
        fout.write('<thead>')
        fout.write('<tr>')
        #fout.write('<th>地址(URL)</th>')
        fout.write('<th>地区</th>')
        fout.write('<th>酒店信息一览表</th>')
        fout.write('</tr>')
        fout.write('<tr>')
        fout.write('<th>/</th>')
        fout.write('<th>')
        fout.write('<ul>')
        fout.write('<li>')
        fout.write('<span>酒店名称</span>')
        fout.write('<span>酒店地址</span>')
        fout.write('<b>酒店图片</b>')
        fout.write('<span>评分</span>')
        fout.write('<span>价格(元)</span>')
        fout.write('</li>') 
        fout.write('</ul>') 
        fout.write('</th>')
        fout.write('</tr>')
        fout.write('</thead>')


        for data in self.datas:
            fout.write('<tr>')
            #fout.write('<td class="url"><p>%s</p></td>'% data['url'])
            if data['title'] is not None:
                fout.write('<td class="title">%s</td>'% data['title'].encode('utf-8'))
                fout.write('<td class="summary">')
                fout.write('<ul>')
                for s in data['hotel_info']:
                    fout.write('<li>')
                    fout.write('<span>%s</span>'% s['name'])
                    fout.write('<span>%s</span>'% s['address'])
                    fout.write('<img src="%s"/>'% s['img'])
                    fout.write('<span>%s</span>'% s['rato'])
                    fout.write('<span>%s</span>'% s['price'])
                    fout.write('</li>')  
                fout.write('<ul>')
                fout.write('</td>')
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()