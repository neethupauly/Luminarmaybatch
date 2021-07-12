# pattern matching
# pattern matching only supported in strings
# re-regular expressions
# re -- package for pattern matching

import re

count=0
matcher=re.finditer('ab','abaabaababab')
# print(matcher)  #returns a location
for match in matcher:
    print("match availiable at :",match.start())  #returns positions
    print("group:",match.group())  #return match object
    count=count+1
print("count:",count)