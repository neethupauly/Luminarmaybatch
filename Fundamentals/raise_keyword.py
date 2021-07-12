# raise - keyword for exception printing

# same number
# no1=int(input("enter num1"))
# no2=int(input("enter num2"))
# if no1==no2:
#     raise Exception("two numbers are same")
# else:
#     print(no2+no1)



#age condition exception printing
age=int(input("enter your age"))
if age>18:
    print("eligible for vaccination")
else:
    raise Exception("Exception occured..not eligible")

