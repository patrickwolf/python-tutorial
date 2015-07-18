#!/usr/bin/env python
# encoding: utf-8
'''
Created on Jul 27, 2013
@author: Patrick
'''
import unittest
import os
from extract_images import ExtractImages

class Test(unittest.TestCase):

    def test_get_urls(self):
        # multi line string
        html = """
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<body>
<table border="1">
<tr>
<td>test</td>
<td><img src="http://www.patrickwolf.net/wp-content/uploads/2008/09/mcp.png"></td>
<td><img src="http://abc/test.png" data-defer-src="http://abc/testdefer.jpg"></td>
<td><img src="http://abc/test.png" data-defer-src="/testdefer.jpg"></td>
<td><img src="abc/test.png" data-defer-src="wp/testdefer.jpg?test=true"></td>
</tr>
</table> 
</body></html>
"""        
        correct_urls = [
        "http://www.patrickwolf.net/wp-content/uploads/2008/09/mcp.png",
        "http://abc/testdefer.jpg",
        "http://www.test.com/testdefer.jpg",
        "http://www.test.com/wp/testdefer.jpg?test=true"]

        ei = ExtractImages("http://www.test.com/?q=test")
        urls = ei.get_image_urls(html)
        self.assertItemsEqual(urls, correct_urls)

    def test_download_url(self):
        # get url to dummy.jpg
        pn = os.path.dirname(__file__)
        fpn = os.path.join(pn, "dummy.png")
        url = "file:///" + fpn.replace("\\", "/").replace(":", "|")
        # get target path
        target_fpn = os.path.join(pn, "dummy_1.png")
    
        ei = ExtractImages("http://www.test.com/?q=test")
        ei.download_image_from_url(url, pn)
        # test file was correctly downloaded
        self.assertTrue(os.path.exists(target_fpn), "target file missing")
        self.assertEqual(os.path.getsize(fpn), os.path.getsize(target_fpn), "file size mismatch")
        # cleanup 
        os.remove(target_fpn)
        
if __name__ == "__main__":
    unittest.main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
