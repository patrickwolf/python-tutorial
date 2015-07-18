#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@summary: Python Intro - Standard Libraries - DateTime
Further resources: http://pymotw.com/2/datetime/
"""
import datetime

print "# TIME"
t = datetime.time(10,11,15)
print t.hour, t.minute, t.second, t.tzinfo
# Limits
print 'Earliest  :', datetime.time.min
print 'Latest    :', datetime.time.max
print 'Resolution:', datetime.time.resolution

print "# DATE"
d = datetime.date.today()
print d.day, d.month, d.year
# Limits
print 'Earliest  :', datetime.date.min
print 'Latest    :', datetime.date.max
print 'Resolution:', datetime.date.resolution

print "# DATE & TIME"
now = datetime.datetime.now()
print now
print repr(now)
print type(now)
print now.year, now.month, now.day, now.hour, now.minute, now.second, now.microsecond

print "# TIMEDELTAS"
now = datetime.datetime.now()
week = datetime.timedelta(7)
print now - week, now, now + week

print "# FORMATTING"
format = "%Y%m%d"
print (now-week).strftime(format), (now).strftime(format), (now+week).strftime(format)


