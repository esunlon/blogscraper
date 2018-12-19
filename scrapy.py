import urllib.request
import re
class Scrapier:

    def decodeHTML(self, url):
        page = urllib.request.urlopen(url)
        html = page.read().decode('utf-8') #coverts bytes type to string
        return html

    def downElement(self, html, regstr):
        elem_reg = re.compile(regstr)
        elem_url_list = elem_reg.findall(html)

        for url in elem_url_list:
            seg_name = url.split('/')
            urllib.request.urlretrieve(url, seg_name[-1])
        return elem_url_list
