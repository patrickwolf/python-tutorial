'''
@summary: Python Intro - Slicing
'''
# ---------------------------
# slicing or accessing members via "array" notation
# ---------------------------
# variable[X]          - item X
# variable[fromX:toY]    
# variable[fromX:-toY] - "-toY" starting from last    
# variable[:toY]       - from first
# variable[fromX:]     - to last
# variable[:]          - all items

st = "abcdefghijklmnop"
print st[:], st[:2], st[2:], st[1], st[2:3], st[-1] # abcdefghijklmnop ab cdefghijklmnop b c p

# slicing always returns a copy
print id(st), id(st[:])


