#!/usr/bin/env python
# -*- coding: utf-8 -*-

def divide(x, y):
    try:
        result = x / y
    #TODO: Catch error when 2,0 is given
    else:
        print "result is", result
    finally:
        print "executing finally clause"

divide(2, 1)
divide(2, 0)
divide("2", "1")