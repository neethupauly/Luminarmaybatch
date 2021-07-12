# if there is a condition perfomed on objects we can use filter

# even numbers only

# lst=[1,2,3,4,5,6,7,8,9]

# even=list(filter(lambda num:num%2==0,lst))
# print(even)

# odds only

# odds=list(filter(lambda num:num%2!=0,lst))
# print(odds)

# products=[
#     {"item_name":"boost","mrp":290,"stock":50},
#     {"item_name":"complan","mrp":240,"stock":10},
#     {"item_name":"bournvita","mrp":320,"stock":20},
#     {"item_name":"horlicks","mrp":280,"stock":13},
#     {"item_name":"nutricharge","mrp":275,"stock":0},
# ]
#
# product names only
# -------------------------------
# for product in products:
#     print(product["item_name"])

# name=list(map(lambda product:product["item_name"],products))
# print(name)

# out of stock products
# ---------------------------
# for product in products:
#     if product["stock"]==0:
#         print(product)

# out_of_stock=list(filter(lambda product:product["stock"]==0,products))
# print(out_of_stock)



# print product details available below<250

# mrp=list(filter(lambda rupees:rupees["mrp"]<250,products))
# print(mrp)



# l2=[]
# for num in lst:
#     if num<5:
#         l2.append(num-1)
#     else:
#         l2.append(num+1)
# print(l2)

