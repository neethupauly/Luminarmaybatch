# converting list to set
# and finding common elements
list1 = [1, 2,3,5,7,]
list2 = [1, 3,5,9]
list1_set = set(list1)
list2_set=set(list2)
print(list1_set)
i= list1_set.intersection(list2)


intersection_as_list = list(i)

print(intersection_as_list)


# calculator
# def add(x, y):
#     return x + y
# def subtract(x, y):
#     return x - y
# def multiply(x, y):
#     return x * y
# def divide(x, y):
#     return x / y
# def floor_division(x,y):
#     return x//y
# def exponent(x,y):
#      return x**y
# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")
# print("5.floor division")
# print("6.exponent")
#
# choice = input("Enter choice(1/2/3/4/5/6):")
#
# num1 = int(input("Enter first number: "))
# num2 = int(input("Enter second number: "))
#
# if choice == '1':
#    print(num1,"+",num2,"=", add(num1,num2))
#
# elif choice == '2':
#    print(num1,"-",num2,"=", subtract(num1,num2))
#
# elif choice == '3':
#    print(num1,"*",num2,"=", multiply(num1,num2))
# elif choice == '4':
#    print(num1,"/",num2,"=", divide(num1,num2))
# elif choice == '5':
#    print(num1,"//",num2,"=",floor_division(num1,num2))
# elif choice == '6':
#    print(num1,"**",num2,"=",exponent(num1,num2))
# else:
#    print("Invalid input")