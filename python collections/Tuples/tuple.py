# tuples are immutable
# so that updations are not possible
# values  cant be removed
# tuples are hetrogenous
# indexing is possible
# nesting is possible
# tuple unpacking is also possible


tup=(1,2,3,4,5,6,7,8,9)    #brackets are not mandatory
print(type(tup))
print(tup)
tup2=()    #empty tuple creation
print("max value",max(tup))
print("min value",min(tup))
print("length of tuple",len(tup))
t=(1,2,3,"hello",5.6)
print(t)
print(t[1])
print(t[-2])

