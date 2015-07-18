#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# exception handling syntax
try:
    raise ValueError("ValueError raised")
except ValueError as ex:
    print ex
except IOError as ex:
    print ex
# Multiple Exception as tuple
except (IOError, EOFError) as ex:
    print type(ex), ex
# as is not required if no reference to the exception is needed
except MemoryError:
    print "Out of memory"
# this catches any uncaught exception
except:
    # throw the same exception again
    raise
else:
    print "No exception was raised"
finally:
    print "Finally is always called"

# exercise: devide number by 0 and catch the error

# exception strategy




