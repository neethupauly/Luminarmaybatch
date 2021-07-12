# Quantifiers

# x= '[abc]' either a b or c
# x= '[^abc]' except abc
# x= '[a-z]' a to z
# x= '[A-Z]' A to Z
# x= '[a-zA-z]' a to z  both lower and uppercase are checked
# x= '[0-9]' check digits
# x= '[^a-zA-Z0-9]' special symbols
# x= '\s' check space
# x= '\d' check the digits
# x= '\D' except digits
# x= '\w' all the words except special characters
# x= '\W' special characters




# x= '[abc]' either a b or c
# import re
#
# x="[abc]"  #either a or b or c
# matcher=re.finditer(x,"abtcbbfhcdghabllc")
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x= '[^abc]' except abc
# import re
#
# x="[^abc]"  #either a or b or c
# matcher=re.finditer(x,"abtcbbfhcdghabllc")
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x= '[a-z]' a to z
# import re
#
# x='[a-z]'   #only considers lowercase
# matcher=re.finditer(x,"abbcdvhjiklmnopqA34AGHBNrstvuwxyzdef")
# for match in matcher:
#     print(match.start())
#     print(match.group())



# x= '[A-Z]' A to Z
# import re
#
# x='[A-Z]'   #only considers uppercase
# matcher=re.finditer(x,"abbcdvhjiklmnopqA34AGHBNrstvuwxyzdef")
# for match in matcher:
#     print(match.start())
#     print(match.group())





# x= '[a-zA-z]' a to z  both lower and uppercase are checked
import re

# x='[a-zA-z]'   #considers uppercase and lowercase
# matcher=re.finditer(x,"abbcdvhjiopqA34AGHBNstvuwdef")
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x='[0-9]'  #check digits
# import re
#
# x='[0-9]'   #considers uppercase and lowercase
# matcher=re.finditer(x,"ab1234098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())




# x= '[a-zA-Z0-9]'# special symbols
import re

x='[a-zA-Z0-9]'   #considers uppercase and lowercase
matcher=re.finditer(x,"ab12 34#098765%")
for match in matcher:
    print("position",match.start())
    print(match.group())



# x= '\s' check space
# import re
#
# x='[\s]'   #considers uppercase and lowercase
# matcher=re.finditer(x,"ab12 34#098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())




# x= '\d' check digits
# import re
#
# x='[\d]'   #check digits
# matcher=re.finditer(x,"ab12 34#098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())




# x= '\D' check digits
# import re
#
# x='[\D]'   #except digits
# matcher=re.finditer(x,"ab12 34#098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())



# x= '\w' check all the words except special characters
# import re
#
# x='[\w]'   #all the words except special characters
# matcher=re.finditer(x,"ab12 34#098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())



# x= '\W' check special characters
# import re
#
# x='[\W]'   #check special characters
# matcher=re.finditer(x,"ab12 34#098765%")
# for match in matcher:
#     print("position",match.start())
#     print(match.group())
