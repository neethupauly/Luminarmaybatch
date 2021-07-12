# it returns a single value
# builtin module contains map,filter
# reduce contains in functools

from functools import reduce

lst=[1,2,3,4,5,6,7,8]

# total=reduce(lambda num1,num2:num1+num2,lst)
# print(total)

# highest=reduce(lambda num1,num2:num1 if num1>num2 else num2,lst)
# print(highest)

result=list(map(lambda num:num-1 if num<5 else num+1 if num >5 else num,lst))
print(result)


# products=[
#     {"item_name":"boost","mrp":290,"stock":50},
#     {"item_name":"complan","mrp":240,"stock":10},
#     {"item_name":"bournvita","mrp":320,"stock":20},
#     {"item_name":"horlicks","mrp":280,"stock":13},
#     {"item_name":"nutricharge","mrp":275,"stock":0},
# ]
#
# prices=list(map(lambda product:product["mrp"],products))
# highest_cost=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
# print(highest_cost)