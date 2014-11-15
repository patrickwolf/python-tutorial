'''
@summary: Python Intro - Modules
namespace, reuse
pkg_tools is a package which is compareable to a self contained library with its own name space
'''
from pprint import pprint

# ---------------------------
# importing foundation
# ---------------------------
print "\n--- foundations ---"
import sys
# this is the path python consults when resolving imports
pprint (sys.path)

import os
# this path is always adds to the sys.path search list
print os.environ["PYTHONPATH"]

# ---------------------------
# different ways to import a module into the namespace
# ---------------------------
print "\n--- namespace modules ---"
import mod_logger
mod_logger.log_warning("only module imported")

from mod_logger import log_warning
log_warning("function imported - direct access")

from mod_logger import log_warning as logwarn
logwarn("alias imported logwarn")

# ---------------------------
# different ways to import a package into the namespace
# ---------------------------
print "\n--- namespace packages ---"
lst = [1, 2, 3, 1, 2, 3, 4]
import pkg_tools.mod_lists
print pkg_tools.mod_lists.get_unique_list(lst)

from pkg_tools import mod_lists
print mod_lists.get_unique_list(lst)

from pkg_tools.mod_lists import get_unique_list
print get_unique_list(lst)

from pkg_tools.mod_lists import get_unique_list as getunique
print getunique(lst)


# Only exectued when this is the startup script
if __name__ == '__main__':
    pass
