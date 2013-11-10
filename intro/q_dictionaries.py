'''
@summary: Python Intro - Dictionaries
'''
# key needs to be hashable -> immutable

# -----------------------
# Initialize empty
# -----------------------
dic = {}

# -----------------------
# Init and populate
# -----------------------
dic = {"int":1, "st":"str", "li": [1, 2, 3], (2, 3):"tuple value"}

# -----------------------
# Extend (value can have any type)
# -----------------------
dic["dic"] = {"int":55}

# -----------------------
# Edit
# -----------------------
dic["dic"] = dic["st"]

# -----------------------
# Delete key/value
# -----------------------
del dic["dic"]

# -----------------------
# Check for presence
# -----------------------
print dic.has_key("int")  # True
print "int" in dic  # True

# -----------------------
# key has to be Immutable
# -----------------------
# dic={[0,1]:1}  # TypeError: unhashable type: 'list'

# tuple is immutable
dic = {(0, 1):1}  # works

# -----------------------
# Extracting
# -----------------------
dic = {(0, 1):1, "st":"abc", "int":3}  
print dic.keys()  # [(0, 1), 'int', 'st']
print dic.values()  # [1, 3, 'abc']
print dic.items()  # [((0, 1), 1), ('int', 3), ('st', 'abc')]

print "-------------------------"
dic = {"int":1, "st":"str", "li": [1, 2, 3], (2, 3):"tuple value"}
for key, value in dic.iteritems():
    print key, value
