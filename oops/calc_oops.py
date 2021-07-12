class Calculator:
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b

    def subtract(self):
        return self.a-self.b

    def multiply(self):
        return self.a*self.b

    def divide(self):
        return self.a/self.b
# take input from the user
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice(1/2/3/4):")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

cal=Calculator(num1,num2)

if choice == '1':
   print(num1,"+",num2,"=",cal.add())

elif choice == '2':
   print(num1,"-",num2,"=", cal.subtract())

elif choice == '3':
   print(num1,"*",num2,"=", cal.multiply())
elif choice == '4':
   print(num1,"/",num2,"=", cal.divide())
else:
   print("Invalid input")