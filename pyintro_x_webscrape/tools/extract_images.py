#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jul 22, 2013
@author: Patrick Wolf
'''
import os
import urllib2
import urlparse
import mimetypes
from bs4 import BeautifulSoup

class ExtractImages(object):
    '''
    Retrieve images from website
    '''

    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url

        self.img_urls = None
        self.counter = 0

        # extract domain to allow converting relative image urls to absolute ones
        url_parts = urlparse.urlparse(url)
        self.url_root = "%s://%s" % (url_parts.scheme, url_parts.netloc) 
        
        # download page
        self.page = self._get_webpage()
        
    def _get_webpage(self):
        print "Getting page '%s'" % self.url
        try:
            response = urllib2.urlopen(self.url)
            return response.read()   
        except Exception, e:
            raise Exception("Error retrieving: %s, %s" % (self.url, str(e.args)))
         
    def get_image_urls(self, page=None):
        if not page: 
            page = self.page
        if not page:
            print "No page found"
            return
        print "Parsing HTML"
        
        soup = BeautifulSoup(page)
        images = soup.findAll("img")
        results = []
        for img in images:
            imgurl = None
            # Flickr uses these attributes
            if "data-defer-src" in img.attrs:
                imgurl = img.attrs["data-defer-src"]
            elif "src" in img.attrs: 
                imgurl = img.attrs["src"]            
            else:
                continue
            # skip embeded 
            if imgurl.lower().startswith("data:"):
                continue
            # fix relative url
            if "://" not in imgurl:
                imgurl = urlparse.urljoin(self.url_root, imgurl) 
            if imgurl not in results:
                results.append(imgurl)                
        
        # keep track
        self.img_urls = results
        return self.img_urls 
    
    def download_images_from_url(self, urls, target_path):
        """ download a list of image urls to target_path """
        if not urls:
            urls = self.img_urls
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        if (type(urls) == type(str)) or (type(urls) == type(unicode)): 
            urls = [urls]
        for url in urls:
            try:
                self.download_image_from_url(url, target_path)
            except Exception, ex:
                print str(ex)
            
    def download_image_from_url(self, url, target_path):
        """ download a list of image urls to target_path """
        # remove parameters from url
        urlparts = urlparse.urlparse(url)
        fn = os.path.basename(urlparts.path)
        # remove file extension
        fn_noext = os.path.splitext(fn)[0]

        print "Downlading: '%s'" % (url)
        response = urllib2.urlopen(url)
        if not response:
            print "URL invalid '%s'" % (url)
            return

        # get extension based on mime type
        if not "Content-Type" in response.headers:
            print "No content type"
            return
        ext = mimetypes.guess_extension(response.headers["Content-Type"])

        self.counter += 1
        tpfn = os.path.join(target_path, "%s_%s%s" % (fn_noext, self.counter, ext))

        # skip small files
        if int(response.headers["Content-Length"]) < 2048:
            print "Skip small image"
            return

        print "Saving: '%s'" % (tpfn)
        output = open(tpfn, 'wb')
        output.write(response.read())
        
        output.close()            

if __name__ == "__main__":
    # url = "http://www.picsearch.com/index.cgi?q=movies"
    url = "http://www.flickr.com/search/?q=mountains"
    # url = "http://www.pixomondo.com/wp/?page_id=43"
    hp = ExtractImages(url)
    hp.get_image_urls()
    hp.download_images_from_url(None, r"c:\temp\img")
