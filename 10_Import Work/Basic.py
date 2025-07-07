# Explanation:
# Python's import system is a powerful mechanism for loading code from other modules/packages. 
# Here's a detailed explanation of how it works:

# 1. Basic Import Syntax
# Importing Entire Modules

import math
print(math.sqrt(16))  # 4.0


# Importing Specific Names

from math import sqrt, pi
print(sqrt(9))  # 3.0
print(pi)      # 3.141592653589793


# mporting with Aliases
import numpy as np
from datetime import datetime as dt


# = The Import Process Step-by-Step
# When Python executes import module:
# Checks sys.modules (import cache) first
# Searches sys.path if not found in cache:
# Current directory
# PYTHONPATH directories
# Installation-dependent default path
# Compiles to bytecode (.py → .pyc) if needed
# Executes the module (all top-level code runs)
# Creates a namespace for the module
# Binds the name in current scope


# = Import Search Path
# Python looks for modules in this order:
# Built-in modules
# Current directory
# Directories in PYTHONPATH
# Installation-dependent directories (site-packages)

import sys
print(sys.path)  # View the search path