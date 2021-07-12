# luminar register number validation and python regno moving to another file

import re
f=open("lumregno","r")
f2=open("register","w")
x = '[L][U][M][0-9]{2}[P][Y][0-9]{3}'

for i in f:
    regno=i.rstrip("\n")
    match = re.fullmatch(x, regno)
    if match is not None:
        f2.write(regno)
        f2.write("\n")




