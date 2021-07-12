# vehicle registration  with file #KL45DF5643

import re
# a=input("Enter your Vehicle number")
x='[K][L][0-9]{2}[A-Z]{2}[0-9]{4}'
f1=open("veh_valid","r")
f2=open("newf","w")
for j in f1:

    words=j.rstrip("\n")
    # str(words)
    match=re.fullmatch(x,words)
    if match != None:
        f2.write(j)


