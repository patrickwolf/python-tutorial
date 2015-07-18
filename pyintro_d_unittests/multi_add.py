'''
@summary: Python Intro - Functions
'''
__author__ = 'Patrick Wolf'

def add(aint, bint=0, cint=None):
    """ add up to three numbers together """
    result = aint + bint
    if cint:
        result += cint
    return result  # function returns value

def multi_add(*args):
    """ adds unlimited numbers together """
    result = 0
    for a in args:
        result += a
    return result


if __name__ == '__main__':
    print "\n--- add ---"
    print add.__doc__
    print add(4)
    print add(4, 2, 5)
    print add(3, bint=1, cint=15)
    print add(10, cint=25)

    print "\n--- multi add ---"
    print multi_add.__doc__
    print multi_add (5, 3, 1, 2341, 543, 12)
