'''
@summary: Python Intro - Comparison 
'''
# ---------------------------
# Comparison uses '==' '!=' 'or' 'not' 'and'
# ---------------------------
print 2 == 2.5  # False
print 2 != 2.5 or 2.5 != 2  # True
print not 2 == 2.5  # True
print not True == False  # True
print "ABC" == "abc"    # False
print "ABC".lower() == "abc"    # True

# ---------------------------
# Type comparison
# ---------------------------
print type(1) == int  # True
print type("string value") == str  # True