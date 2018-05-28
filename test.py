# coding = utf-8
import urllib.request
from bs4 import BeautifulSoup

#定义一个函数，用以获取指定网页的源码
def download(url):
    print('Downloading:',url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print('Download error:', e.reason)
        html = None
    return html

'''
broken_html = '<ul class=country><li>Area<li>Population</ul>'
soup = BeautifulSoup(broken_html, "html.parser")
fixed_html = soup.prettify()
print(fixed_html)
'''

