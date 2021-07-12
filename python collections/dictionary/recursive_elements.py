# adding recursive elements
# ex:same elements in a string

# pattern=input("enter a string")
# dict={}
# for i in pattern:
#     if i not in dict:
#         dict.update({i:1})
#     else:
#         print("first recursive element",i)
#         break


# second method
x=input("enter  string")
count=0
for i in x:
    count=x.count(i)
    if count>1:
        break
print("first recursive element is:",i)

