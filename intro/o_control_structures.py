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
