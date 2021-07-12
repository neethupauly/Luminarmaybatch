# 1st program
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name",self.name)
        print("age",self.age)
class Student(Person):
    def __init__(self,rollno,mark,name,age):  #we are using inheritance so that we have to initialize the attributes
        super().__init__(name,age)   #calling superclass constructor
        self.rollno=rollno
        self.mark=mark
    def print(self):
        print("roll no:",self.rollno)
        print("mark :",self.mark)
s=Student(2,89,"Neethu",24)
s.printval()
s.print()

# 2nd program
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name is :",self.name)
        print("age is :",self.age)

class Employee(Person):
    def __init__(self,empid,salary,company,name,age):
        super().__init__(name,age)
        self.empid=empid
        self.sal=salary
        self.company=company
    def print(self):
        print("employee id :",self.empid)
        print("employee salary :",self.sal)
        print("employee company :",self.company)

ob=Employee(704,25000,"infy","jinto",29)
ob.printval()
ob.print()