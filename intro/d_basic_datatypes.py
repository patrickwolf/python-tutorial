'''
@summary: Python Intro - Basic DataTypes
'''
# ----------------------
# Assignments
# ----------------------
# first assignment creates name which references value in memory, types are inferred
aint = 5
cstr = dstr = "test"  # both cstr and dstr will contain the value: test
aint = "test"

# ---------------------------
# Numbers
# ---------------------------
a = 5 + 5  # int
b = 2.5  # float

# ---------------------------
# Boolean
# ---------------------------
a = True
b = False

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

# string formating
print "part1 '%s' part2 '%s'" % ('a', 'b')

print "part1 '%s' " % 'b'


