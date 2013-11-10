'''
@summary: Python Intro - Syntax
'''

# ----------------------
# Comments
# ----------------------
# there are no multi line comments but multi line strings which can be used as comments
""" 
line1  
line2
"""

# docstring to comment functions / classes etc. Will be used by intellisense / debugger etc.
def my_function():
    """ this function does a lot 12334"""
    pass  # this means don't do anything

# ----------------------
# Indentation
# ----------------------

# python uses indentation instead of brackets (can be space or tab)
if True:
    pass
    if False:
        pass
    elif True:
        pass
    else:
        pass

# you can write code after the :
if True: print "one liner also works" 

            
