'''
@summary: Python Intro - Code Sample
'''

def add(a, b):
    return a + b

x = 200 
y = 150
z = add(x, y)

if z > 100 and z < 1000:
    print "in the hundreds:" ,z
elif z > 0:
    print "positive number:" , z
else:
    print "negative number"
