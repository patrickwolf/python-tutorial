#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jul 22, 2013
@summary: Dowload images from websites
@author: Patrick Wolf
'''
import sys
import os

from optparse import OptionParser
from tools.extract_images import ExtractImages

def main(argv=None):
    '''Command line options.'''
    if argv is None:
        argv = sys.argv[1:]
    try:
        # setup option parser
        parser = OptionParser(version="ImageDowloader v0.1")
        parser.add_option("-u", "--url", dest="url", help="url of website")
        parser.add_option("-d", "--dst", dest="dst", help="destination path")
        
        # process options
        (opts, args) = parser.parse_args(argv)
        
        # --------------
        # MAIN APP
        # --------------
        print parser.version
        # Check parameters
        if not opts.url:
            print "URL missing"
            return
        if not opts.dst:
            print "Target path missing"
            return        
            
        ei = ExtractImages(opts.url)
        ei.get_image_urls()
        ei.download_images_from_url(None, opts.dst)       
        print "--- done ---"            
                          
    except Exception, ex:
        # rethrow exception to show stack trace
        raise
    
if __name__ == "__main__":
    # sample call: python img_downloader.py -u http://www.pixomondo.com/wp/?page_id=43 -d c:\temp\e
    argv = sys.argv[1:]
    if not argv:
        print "no args provided. doing testing"
        # needs to be a list as it would come in as a list from the command line as parameters
        argv = ["-u", "http://www.pixomondo.com/wp/?page_id=43", "-d", r"c:\temp\img"]
        argv = ["-u", "http://www.picsearch.com/index.cgi?q=movies", "-d", r"c:\temp\img"]
        argv = ["-u", "http://www.flickr.com/search/?q=mountains", "-d", r"c:\temp\img"]

    sys.exit(main(argv))
