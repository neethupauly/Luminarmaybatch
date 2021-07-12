# all objects outputs are generated then we can use - map
# all objects output are generated currespondingly -map


# map(function,iterables)
# first argument is function name
lst=[1,2,3,4,5,6,7,8]
# def square(num):
#     return (num**2)
# sqr=list(map(square,lst))
# print(sqr)


products=[
    {"item_name":"boost","mrp":290,"stock":50},
    {"item_name":"complan","mrp":240,"stock":10},
    {"item_name":"bournvita","mrp":320,"stock":20},
    {"item_name":"horlicks","mrp":280,"stock":13},
    {"item_name":"nutricharge","mrp":275,"stock":0},
]
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
# list[2,3,4,8,10,7] if num<5 then num-1 else num+1   o/p=[1,2,3,9,11,8]


lst=[2,3,4,8,10,7]
l2=list(map(lambda num:num+1 if num>5 else num-1 ,lst))
print(l2)