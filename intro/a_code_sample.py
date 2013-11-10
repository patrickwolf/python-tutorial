'''
@summary: Python Intro - Code Sample
'''

def add(a, b):
    """ add two numeric values """
    return a + b

def get_info(val):
    """ print out s"""
    if val > 1000: 
        print "in the thousands:" , val
    elif val > 100 and val < 1000:
        print "in the hundreds:" , val
    elif val > 0:
        print "positive number:" , val
    else:   
        print "negative number"
    
# only execute if this is the main file
if __name__ == "__main__":
    x = 200 
    y = 150
    z = add(x, y)    
    get_info(z)
