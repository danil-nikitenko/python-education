"""Modules and packages"""

import re

# Your code goes here
find_functions = []
for i in dir(re):
    if "find" in i:
        find_functions.append(i)
find_functions.sort()
print(find_functions)
