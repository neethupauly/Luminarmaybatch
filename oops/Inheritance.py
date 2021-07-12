# inheritance
# single inheritance  - only one class is inherited


# 1st program -single inheritance

class Person:                #parent class/base class/super class
    def pdetails(self,name,age,address):
        self.name=name
        self.age=age
        self.add=address
        print(self.name,self.age,self.add)
class Student(Person):        #child class/sub class/derived class
    def sdetails(self,rollno,department,mark):
        self.rollno=rollno
        self.dep=department
        self.mark=mark
        print(self.rollno,self.dep,self.mark)
        print(self.name,"mark is :",self.mark)
        print(self.name,"age is :",self.age)

st=Student()
st.pdetails("anu",24,"ABC")
st.sdetails(12,"cs",80)


# 2nd program-single inheritance

# class Person:
#     def pdetails(self,name,age,address):
#         self.name=name
#         self.age=age
#         self.add=address
#         print(self.name,self.age,self.add)
# class Employee(Person):
#     def edetails(self,empid,designation,salary,company):
#         self.empid=empid
#         self.designation=designation
#         self.sal=salary
#         self.company=company
#         print(self.empid,"employee",self.name,"age is :",self.age)
#         print(self.name,self.designation,self.sal,self.company,"address of",self.add)
# emp=Employee()
# emp.pdetails("neethu",23,"ABC")
# emp.edetails(123,"Manager",60000,"TCS")

