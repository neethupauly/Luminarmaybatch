# l1=[0,9,8,5,-2,-80,4,96,3]
# l2=[]
# while l1:
#     min = l1[0]
#
#     for i in l1:
#         if i < min:
#             min = i
#     l2.append(min)
#     l1.remove(min)
# print(l2)
# print(l1)

# 2nd method
lst=[8,0,-1,-3,-4,4,5]
t=len(lst)
temp=0
for i in range(t):
    for j in range(i+1,t):
        if lst[i]>lst[j]:
            temp=lst[i]
            lst[i]=lst[j]
            lst[j]=temp
print(lst)



# sorting home work
