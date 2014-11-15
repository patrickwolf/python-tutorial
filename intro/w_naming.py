'''
@summary: Python Intro - Naming rules 
'''
# ---------------------------
# naming rules
# ---------------------------

# Python is case sensitive
# Variables can't start with a number

# These are valid variable names
foo = _foo = __foo = foo_bar = foo3 = None

# ---------------------------
# scoping
# ---------------------------
# Python doesn't differentiate between private, protected, public but there is a convention

class SampleClass():
    def __init__(self):
        self.publicvar = None
        self._protectedvar = None
        self.__privatevar = None

    def public_function(self):
        pass
        
    def _protected_function(self):
        pass
    
    def __pricate_function(self):
        pass


# ---------------------------
# keywords
# ---------------------------
# don't use these as variable names
reserved_keywords = """
and       del       from      not       while
as        elif      global    or        with
assert    else      if        pass      yield
break     except    import    print
class     exec      in        raise
continue  finally   is        return
def       for       lambda    try
"""