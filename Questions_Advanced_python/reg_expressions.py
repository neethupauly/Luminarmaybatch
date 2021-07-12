# write a code to validate -string starting and ending with
# a uppercase letter -except special characters -minimum length 5 -maximum length 10

# import re
# a=input("enter a string")
# # [A-Z]{1}[a-z0-9\W]+
# x='[A-Z][\w]{3,8}[A-Z]$'
# match=re.fullmatch(x,a)
# if match is not None:
#     print("Valid string")
# else:
#     print("Invalid string")


# x='[A-Z]{1}[\w]+[A-Z]{1}'


# Write a Python program that matches a string that has an 'a' followed by numbers, ending in 'b'?
import re
a=input("enter a string")

x='a{1}[\d]+[b]$'
match=re.fullmatch(x,a)
if match is not None:
    print("Valid string")
else:
    print("Invalid string")


# Write a Python program to find the sequences of one upper case letter followed by lower case letters?
# import re
# a=input("enter a string")
#
# x='[A-Z][a-z]+$'
# match=re.fullmatch(x,a)
# if match is not None:
#     print("Valid string")
# else:
#     print("Invalid string")