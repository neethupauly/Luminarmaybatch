# to string returns the reference
# class College:
#     collegename = "LT"
#
#     def __init__(self,name,roll):
#         self.roll=roll
#         self.name=name
#
#     def printdetails(self):
#         print("college name =",College.collegename)
#         print("name of student",self.name)
#         print("rollno",self.roll)
#     def __str__(self):
#         return str(self.roll)+self.name+College.collegename
# ob=College("anu",4)
# print(ob)
# ob1=College("amal",8)
# print(ob1)


# 2nd program - to string

# class Employee:
#
#     employee_exp="  4 years"
#
#     def __init__(self,id,salary):
#         self.id=id
#         self.sal=salary
# 3
#     def printdet(self):
#
#         print("employee experience:",Employee.employee_exp)
#         print("employee id :",self.id,"employee salary :",self.sal)
#     def __str__(self):
#         return str(self.id)+Employee.employee_exp
#
# ob=Employee(3,20000)
# print(ob)
#
# ob1=Employee(2,25000)
# print(ob1)


# program

class Vehicle:
    def attributes(self,model,reno,color):
        self.model=model
        self.reno=reno
        self.color=color

    def printval(self):
        print("vehicle model:",self.model)
        print("register number:",self.reno)
        print("colour :",self.color)

    def __str__(self):       #to-string method
        return self.reno

v=Vehicle()
v.attributes(2012,"KL-08-8765","Black")

ve=Vehicle()
ve.attributes(2013,"KL-08-6564","Blue")

v.printval()
print(v)
