# supports duplicates elements
# order keeps
# supports hetrogenous data
# nesting is possible
# mutable - can be updated


# lst=[1,2,3,1,2,3,"hello",True]
# print(lst)
# print(type(lst))
# lst1=[] #empty list creation
# print(lst1)
# print(type(lst1))
# lst1.append("hello")
# lst1.append(8)
# print(lst1)

# iterating
# for i in lst1:
#     print(i)
#
# # removing elements
# lst.remove(1)
# print(lst)
# lst.clear()   #for clear all elements
# print(lst)
# del lst      #for deleting the list

# integer list
# lstin=[1,8,9,7,6,5,544,3,2,44]
# add=0
# mul=1
# for i in lstin:
#     add=add+i
#     mul=mul*i
# print("Added list",add)
# print("Multiplied list",mul)
#
# l1=[7,8,[9,0]]
# print(l1)  #nested list
#
# # nested list iterating
# l2=[[1,2,3],[8,9,7]]
# for i in l2:
#     for j in i:
#         print(j)
#
# # odd even lists
# l3=[1,2,4,3,66,54,37,87,9,8]
# odd=[]
# even=[]
# for i in l3:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(odd)
# print(even)

l3=[1,8,9,0,5,6,37,23,89,99]
el=int(input("enter the element to search"))
for i in l3:
    if el in l3:
        print("present")
        break
else:
    print("not present")








