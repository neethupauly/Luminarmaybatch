class  Person:
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

ob=Employee(704,25000,"infosys","Anoop",29)
ob.printval()
ob.print()