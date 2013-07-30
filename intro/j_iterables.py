'''
@summary: Python Intro - Iterables 
'''

# ---------------------------
# tuple - immutable
# ---------------------------
tu = ('spam', 'eggs', 100, 1234, (4,1))
print tu, tu[2]
#tu[2] = "bacon"     # raises TypeError 

# ---------------------------
# string - immutable
# ---------------------------
st = "abc"
st = 'abc'
st = """ multi line
string """
#st[2] = "e"         # raises TypeError

# ---------------------------
# list - mutable
# ---------------------------
a = ['spam', 'eggs', 100, 1234, [4,1]]
# mutable - change values
print "before", a[3]
a[3] = 345
print "after", a[3]
