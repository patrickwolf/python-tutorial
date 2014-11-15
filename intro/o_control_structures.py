'''
@summary: Python Intro - Control Structures
'''

# ----------------------
# if condition:
#     statements
# [elif condition:
#     statements] ...
# else:
#     statements
# ----------------------

print "\n--- if ---"
if ((10 == 5 + 5 or 20 == 10 + 10) and True):
    print "correct"
elif 10 == 20:
    print "this is wrong"
else:
    print "they are both wrong"

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


# ----------------------
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
