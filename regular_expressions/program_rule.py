# word
# import re
#
# n="helloo"
# x='\w*'
# match=re.fullmatch(x,n)
# if match is not None:
#     print("valid")
# else:
#     print("invalid")



import re
# n="56kg"
# x='\d{2}[k][g]'
#
# matcher=re.fullmatch(x,n)
#
# if matcher is not None:
#
#     print("valid")
# else:
#     print("invalid")

# "Abc6"
# "fgRtggg7"
# import re
# a=input("enter a string")
# x='[a-zA-Z]+\d{1}$'
# match=re.fullmatch(x,a)
#
# if match is not None:
#     print("Valid")
#
# else:
#     print("invalid")


# ab, #aGhjk#b  #aKJcg5#b
# import re
# a=input("enter a string")
# x='^a[a-zA-Z0-9\W]*b$'
# match=re.fullmatch(x,a)
#
# if match is not None:
#     print("Valid")
#
# else:
#     print("invalid")



# minimum length 8 maximum length 15  and no numbers
# advbfvgy
# import re
#
#
# a=input("enter a string")
# x='[\D]{8,15}'        #[a-zA-Z]{8,15}
# match=re.fullmatch(x,a)
#
# if match is not  None:
#     print("Valid")
#
# else:
#     print("invalid")



# starting with a uppercase letter,numbers,special character,lowercase
# import re
#
# a=input("enter a string")
# x='[A-Z]{1}[a-z0-9\W]+'
# match=re.fullmatch(x,a)
#
# if match is not  None:
#     print("Valid")
#
# else:
#     print("invalid")



#Indian phone number validation
# import re
# a=input("Enter your phone number")
# x='[+][9][1][\d]{10}'         #[+][9][1][0-9]{10}
# match=re.fullmatch(x,a)
# if match is not None:
#     print("valid phone number")
# else:
#     print("invalid phone number")




# vehicle registration  #KL45DF5643
# import re
# a=input("Enter your Vehicle number")
# x='[K][L][0-9]{2}[A-Z]{2}[0-9]{4}'
# match=re.fullmatch(x,a)
# if match is not None:
#     print("Registered and valid vehicle number")
# else:
#     print("Invalid vehicle number")




# mail validation
# string@string.in/com

import re
mail=input("Enter your E-mail")
x='[A-Za-z0-9]+[@][a-z]+[.][a-z]{2,3}$'

match=re.fullmatch(x,mail)
if match is not None:
    print("Valid E-mail")
else:
    print("Invalid E-mail")






