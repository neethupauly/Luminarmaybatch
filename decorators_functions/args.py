# *args is used to provide more number of arguments

# def add(*args):
#     print(args)
#     sum=0
#     for i in args:
#         sum+=i
#     print(sum)
# add(2,3,4,5,6)

def employee(*args):
    print(args)
employee(1,"anu","kochi",25000,"SEO")    #prints as tuple

# we can define variable by using **
# def printEmployee(**args):
#     print(args)
# printEmployee(id=1,name="amal",designation="manager")   #prints as dictionary