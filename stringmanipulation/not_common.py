# a = "luminar technolab"
# b = input("enter the element to search")
# flag=0
# for i in a:
#     if i in b:
#         flag=1
# if flag==1:
#     print("present")
# else:
#     print("not present")

# two strings

# a="abc"
# b="bcd"
# c=""
# for i in a:
#     if i in b:
#         c=c+i
# if c=="":
#     print("no common")
# else:
#     print(c)

# a="abc"
# b="abds"
#
# for i in a:
#     if i not in b:
#         print(i)
# for j in b:
#     if j not in a:
#         print(j)

# count
# a="malayalam"
# b=input("enter a letter")
# c=0
# for i in a:
#     if b in i:
#         c=c+1
#
# print(c)

# vowels

# a="aeiou"
# b=input("enter an element")
# c=0
# for i in a:
#     if i in b:
#         c=c+1
# if c==0:
#     print("no vowels")
# else:
#     print(c)

# Removing punctuation
# a=input("enter a string")
# b="`!@#$%^&*()-=,.;""'/[]<>{}|?"
# c=""
# for i in a:
#     if i not in b:
#         c=c+i

# print(c)

s="neethu123"
n="1234567890"
countn=0
counts=0
for i in s:
    if i in n:
        countn=countn+1
    else:
        counts+counts+1
print(counts)
print(countn)

str1=" "
str2="abc"
print(str2[0])