# quantifiers

# x='a+'        a including group ( a condition  should come )
# x='a*'        count including zero number of a(a condition may or may not come)
# x='a?'        count a as each including zero no of a
# x='a{2}'      2 no of a position
# x='a{2,3}'    minimum 2 a and maximum 3 a
# x='^a'        check starting with a
# x='a$'        check ending with a



# x='a+'        a including group
# import re
#
#
# x="a+"    #a    including group
# r="aaa  abc  aaaa aaaaa cagaa"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())



# x='a*'        count including zero number of a
# import re
#
#
# x="a*"    #a  count including zero number of a,including space
# r="aaa  abc  aaaa aaaaa cagaa"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x='a?'        count a as each including zero no of a
# import re
#
#
# x="a?"    #a  count  a as each including zero number of a,without group
# r="aaa  abc  aaaa aaaaa cagaa"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())



# x='a{2}'      2 no of a position
# import re
#
#
# x="a{2}"    #2 no of 'a' position
# r="aaa  abc  aaaa aaaaa cagaa"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())



# x='a{2,3}'    minimum 2 a and maximum 3 a
# import re
#
#
# x="a{2,3}"    #minimum 2 a and maximum 3 a,maximum is highest priority then minimum checked
# r="aaa  abc  aaaa aaaaa cagaa"
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x='^a'        check starting with a
# import re
#
#
# x="^a"   #check starting with a
# r="aaa  abc  aaaa aaaaa cagaa"  #considers as complete strig
# matcher=re.finditer(x,r)
# for match in matcher:
#     print(match.start())
#     print(match.group())




# x='a$'        check ending with a
import re


x="a$"   #check ending with a
r="aaa  abc  aaaa aaaaa cagaa"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())