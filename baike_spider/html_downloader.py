'''


@author: Youb
'''
import urllib.request



class HtmlDownloader(object):
    
    def download(self,url):
        if url is None:
            return
        
        req=urllib.request.Request(url)
        req.add_header('user-agent','Mozilla/5.0')

        response=urllib.request.urlopen(req)
        if response.getcode() != 200:
            return None
        return response.read()
    
    