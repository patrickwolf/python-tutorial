'''
@summary: Python Intro - Strings
'''

# ---------------------------
# Strings
# ---------------------------
# usage of " and '
st = "abc"
st = 'abc'
st = "ab'c'd"

# multi line
val = """ 
'line1' <- can contain ' 
"line2" <- and "
"""

# raw strings (no need to escape)
print "c:\\test\\abc"  # c:\test\abc
print r"c:\test\abc"  # c:\test\abc

# string formating
print "part1 '%s' part2 '%s'" % ('a', 'b')

print "part1 '%s' " % 'b'


