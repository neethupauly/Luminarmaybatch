# a=int(input("enter the number"))
#
# if a>0:
#     fact=1
#     for i in range(1,a+1):
#         fact=fact*i
#     print("factorial of the given number is",fact)
# elif a==0:
#     print("fact of 0 is 1")
# else:
#     print("please enter a positive number")

def factorial(x):
    if x==1:
        return 1
    else:
        return (x*factorial(x-1))
num=int(input("enter the number"))
print("the factorial of",num,"is",factorial(num))
