# Create a valid phone numbers file from the following file?
# +915678905432 +914567890321 765432167 123450987765 +919976532456

import re
x='[+][9][1][0-9]{10}'
f=open("file1","r")
f1=open("validphn","w")
for i in f:
    num=i.rstrip("\n")
    matcher = re.fullmatch(x,num)

    if matcher is not None:
        f1.write(i)


