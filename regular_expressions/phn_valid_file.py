import re

x='[+][9][1][0-9]{10}'
f=open("phn_num","r")
# f1=open("phn_num1","w")

for i in f:
    num=i.rstrip("\n")
    matcher = re.fullmatch(x,num)

    if matcher is not None:
        # f1.write(i)
        print(num)
