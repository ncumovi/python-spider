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
        fout = open('output.html','w')  #文件输出对象 w写模式

        fout.write('<html>')
        fout.write('<head>')
        fout.write('<link rel="stylesheet" href="./css/outerputer.css">')
        fout.write('<link rel="stylesheet" href="https://cdn.bootcss.com/bootstrap/3.3.7/css/bootstrap.min.css" integrity="sha384-BVYiiSIFeK1dGmJRAkycuHAHRg32OmUcww7on3RYdg4Va+PmSTsz/K68vbdEjh4u" crossorigin="anonymous">')
        fout.write('</head>')
        fout.write('<body>')
        fout.write('<h1>Python相关名词爬虫</h1>')
        fout.write('<table border="1" class="table table-striped">')
        fout.write('<thead>')
        fout.write('<tr>')
        fout.write('<th>地址(URL)</th>')
        fout.write('<th>名词</th>')
        fout.write('<th>简介</th>')
        fout.write('</tr>')
        fout.write('</thead>')


        for data in self.datas:
            fout.write('<tr>')
            fout.write('<td class="url"><p>%s</p></td>'% data['url'])
            fout.write('<td class="title">%s</td>'% data['title'].encode('utf-8'))
            fout.write('<td class="summary">%s</td>'% data['summary'].encode('utf-8'))
            fout.write('</tr>')

        fout.write('</table>')
        fout.write('</body>')
        fout.write('</html>')

        fout.close()