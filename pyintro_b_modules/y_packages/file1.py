'''
@summary: Python Intro - Importing Packages
'''

import package.module1
package.module1.Module1()

from package.module1 import Module1
Module1()

from package.subpackage.submodule1 import SubModule1 
SubModule1()

from package import *
module1.Module1()
module2.Module2()

if __name__ == '__main__':
    pass
