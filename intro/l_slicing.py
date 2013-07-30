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

tu = (23,51,"abc",5.2)
print tu[:], tu[:2], tu[2:], tu[1], tu[2:3], tu[-1] # (23, 51, 'abc', 5.2) 51 ('abc',) 5.2

st = "abcdefghijklmnop"
print st[:], st[:2], st[2:], st[1], st[2:3], st[-1] # abcdefghijklmnop ab cdefghijklmnop b c p

li = [23,51,"abc",5.2]
print li[:], li[:2], li[2:], li[1], li[2:3], li[-1] # [23, 51, 'abc', 5.2] [23, 51] ['abc', 5.2] 51 ['abc'] 5.2

# slicing always returns a copy
print id(li), id(li[:])