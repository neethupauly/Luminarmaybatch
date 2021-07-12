# l1=[1,2,3,4,5,8,2,3,0,54,21,12,14]
# l2=[]
# while l1:
#     min=l1[0]
#     for i in l1:
#         if i<min:
#             min=i
#     l2.append(min)
#     l1.remove(min)
# print(l2)
# print("minimum element",l2[0])
# print("maximum element",l2[-1])

# printing duplicate elements
# a=[1,2,3,4,5,6,7,8,9,4,5,2,1]
# b=[]
# for i in a:
#     if i not in b:
#         b.append(i)
#     else:
#         print(i)

# multiplied list
# a=[1,2,3,4,5,6,7,8,9,4,5,2,1]
# b=[]
# for i in a:
#     b.append(i*5)
# print(b)


# list comprehension
# b=[i*5 for i in a]
# print(b)

# list comprehension
# c=[i for i in range(1,20) if i%2==0 ]
# print(c)

# find all of the numbers from 1 to 1000 that are divisible by 8

# a=[i for i in range(1,1000) if i%8==0]
# print(a)
# print(len(a))

a=[1,2,3]
b=[]
for i in a:
     b.append(i)
print(b)


# removing duplicate elements
# lst=[1,0,7,5,9,2,3,5,7,2,0,1,10]
# s=[]
# b=[s.append(i) for i in lst if i not in s ]
# print(s)


