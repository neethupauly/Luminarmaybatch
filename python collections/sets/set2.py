# finding common elements
# s1={1,3,4,5,6,33,77,8,9,80,55,63,23,14,7}
# s2={1,2,3,4,100,200}
# s3=set()
# for i in s1:
#     if i in s2:
#         s3.add(i)
# print(s3)

# prime and nonprime sets

s=(1,2,3,4,5,6,7,8,9,33,44,54,65,22)
prime=set()
nonprime=set()
for i in s:
    if i>1:
        for j in range(2,i):
            if(i%j)==0:
                nonprime.add(i)
                break
        else:
                prime.add(i)
print(prime)
print(nonprime)
