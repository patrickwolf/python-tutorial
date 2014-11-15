'''
@summary: Python Intro - Functions
'''

# ---------------------------
# functions 
# ---------------------------

def func1(aint):
    """ docstring """
    return  # return nothing (the same as return None)

# ---------------------------
def add(aint, bint=0, cint=None):
    """ add up to three numbers together """
    result = aint + bint
    if cint:
        result += cint
    return result  # function returns value

print "\n--- add ---"
print add.__doc__
print add(4)
print add(4, 2, 5)
print add(3, bint=1, cint=15)
print add(10, cint=25)
# ---------------------------


# ---------------------------
def multiadd(*args):
    """ adds unlimited numbers together """
    result = 0
    for a in args:
        result += a 
    return result


print "\n--- multi add ---"
print multiadd.__doc__
print multiadd (5, 3, 1, 2341, 543, 12)
# ---------------------------
