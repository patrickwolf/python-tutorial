'''
@summary: Python Intro - Control Structures
'''

# ----------------------
# while condition:
#     statements
#     break
#     continue
# ----------------------
print "\n--- while ---"
i = 11
result = ""
while True:
    i -= 1
    if i % 2 != 0:
        continue
    elif i < 0:
        break
    result += "..." + str(i)    
print result


# for var in sequence:
#     statements
#     break
#     continue
# ----------------------
print "\n--- for ---"
# iterating tuple
tu = (23, 51, "abc", 5.2)
for t in tu: 
    print ">", t

# iterating string
st = "abcdefghijklmnop"
result = ""
for t in st: 
    result += "|" + t * 3
print result
