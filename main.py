import sys
from scrapy import Scrapier
# class must be init before use it
sp = Scrapier()
html_url = sys.argv[1]
print (html_url)
decoded_html = sp.decodeHTML(html_url)

imglist = sp.downElement(decoded_html, r'src="(.+?\.jpg)" alt=')
medlist = sp.downElement(decoded_html, r'href="(.+?\.mp3)"')

print(imglist, medlist)
