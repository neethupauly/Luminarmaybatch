# oop....object oriented programming
# class:design patter/blueprint
# object:real world entity
# reference:to perform operations on object
# self-is an instance keyword-inside class
# methods-functions which are inside the class is called methods
# two types of variables
#         1.static variable-class-access using class name
#         2.instance variable-method-access using self


# class  Person:
#     def walk(self):         #method1
#         print("person is walking")
#     def reading(self):      #method2
#         print("person is reading")
# obj1=Person()       #person is object obj is reference
# obj1.walk()         #calling methods
# obj1.reading()      #calling methods


# class with attributes/arguments
# class Person:
#     def setval(self,name,age):
#         self.name=name      #instance variable
#         self.age=age
#     def printval(self):
#         print("name:",self.name)
#         print("age",self.age)
# p=Person()
# # n=input("enter name")
# p.setval("neethu",24)
# p.printval()

# employee class
# class Employee:
#     def setval(self,eid,age,company,designation):
#         self.id=eid
#         self.age=age
#         self.company=company
#         self.designation=designation
#     def printval(self):
#         print("employee id:",self.id)
#         print("employee age:",self.age)
#         print("employee company:",self.company)
#         print("employee designation:",self.designation)
# emp=Employee()
# emp.setval(101,36,"Infosys","Manager")
# emp.printval()
# emp2=Employee()
# emp2.setval(102,39,"Infosys","employee")
# emp2.printval()

# addition program
# class Addition:
#     def setval(self,a,b):
#         self.no1=a
#         self.no2=b
#     def printval(self):
#         c=self.no1+self.no2
#         print("After addition",c)
# add=Addition()
# n1=int(input("enter no1"))
# n2=int(input("enter no2"))
#
# add.setval(n1,n2)
# add.printval()

# student class
# class Student:
#     def setval(self,name,rollno,mark,school_name):
#         self.name=name
#         self.rollno=rollno
#         self.mark=mark
#         self.school_name=school_name
#     def printval(self):
#         print("name:",self.name)
#         print("roll no:",self.rollno)
#         print("mark:",self.mark)
#         print("school name:",self.school_name)
# st=Student()
# n=input("enter name")
# r=input("enter rollno")
# m=int(input("enter marks"))
# s=input("enter school name")
# st.setval(n,r,m,s)
# st.printval()


# bank class
# create account
# deposit  print balance
# withdraw   print balance
# class Bank:
#
#     def accCreate(self,accno,name,bname):
#         self.accno=accno
#         self.name=name
#         self.bname=bname
#         self.minimumbal=5000
#         self.balance=self.minimumbal
#     def deposit(self,amt):
#         self.amt=amt
#         self.balance+=self.amt
#         print("your ",self.bname,"account has been credited with amt",self.amt)
#         print("your current balance =",self.balance)
#     def withdraw(self,amt):
#         self.amt=amt
#         if self.amt>self.balance:
#             print("insufficient balance")
#         else:
#             print("account debited with ",self.amt)
#             self.balance-=self.amt
#             print("availiable balance =",self.balance)
#
#
# obj=Bank()
# num=input("enter account num")
# name=input("enter name")
# bname=input("enter bank name")
# obj.accCreate(num,name,bname)
# print("1.deposit")
# print("2.withdraw")
# ch = input("(1/2)")
#
# if ch=="1":
#     dep = int(input("enter deposit amount"))
#     obj.deposit(dep)
# elif ch=="2":
#     wid = int(input("enter withdrawal amount"))
#     obj.withdraw(wid)
# else:
#     print("invalid choice")





class Book:
    library_name="ABC library"      #static variable
    def setval(self,bkname,author,pages):
        self.bkname=bkname
        self.author=author
        self.pages=pages
    def printval(self):
        print(self.bkname,self.author,self.pages)
        print(Book.library_name)   # printing static variable using class name
bk=Book()
b=input("enter book name")
a=input("enter author name")
p=int(input("enter pages"))
bk.setval(b,a,p)
bk.printval()
bk2=Book()
bk2.setval("world","Neethu",300)
bk2.printval()


class Employee:
    company_Name="Infosys"
    def setval(self,empno,name,salary):
        self.empno=empno
        self.name=name
        self.sal=salary
        print("employee id:",self.empno)
        print("employee name:",self.name)
        print("employee salary:",self.sal)
        print("company:",Employee.company_Name)
emp=Employee()
emp.setval(12,"neethu",25000)

emp2=Employee()
emp2.setval(13,"anu",20000)




