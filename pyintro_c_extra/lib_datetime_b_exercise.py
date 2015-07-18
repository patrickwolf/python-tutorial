#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import
import datetime

# DateTime value as string
dt_value = "2015-01-31 15:55:21"

# convert to date time (see lib_datetime_strftime.txt)
format = "..."
dt = datetime.datetime.strptime(dt_value, format )

# print out as "01/31/2015 3:55:21pm"
format2 = "..."
print dt.strftime(format2)