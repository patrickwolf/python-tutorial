'''
@summary: Python Intro - Iterables 
'''

# ---------------------------
# string - immutable
# ---------------------------
st = "abc"
st = 'abc'
st = """ multi line
string """
# st[2] = "e"         # raises TypeError

# ---------------------------
# tuple - immutable
# ---------------------------
tu = ('spam', 'eggs', 100, 1234.0, (4, 1))
print tu, tu[2]
# tu[2] = "bacon"     # raises TypeError

# ---------------------------
# list - mutable
# ---------------------------
a = ['spam', 'eggs', 100, 1234, [4, 1]]
# mutable - change values
print "before", a[3]
a[3] = 345
print "after", a[3]


# ---------------------------
# tuple - slicing
# ---------------------------
tu = (23,51,"abc",5.2)
print tu[:], tu[:2], tu[2:], tu[1], tu[2:3], tu[-1] # (23, 51, 'abc', 5.2) 51 ('abc',) 5.2

# ---------------------------
# list - slicing
# ---------------------------
li = [23,51,"abc",5.2]
print li[:], li[:2], li[2:], li[1], li[2:3], li[-1] # [23, 51, 'abc', 5.2] [23, 51] ['abc', 5.2] 51 ['abc'] 5.2
