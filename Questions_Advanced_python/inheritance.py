# 1.Create a child class Car that will inherit all of the variables and methods of Vehicle class?

# class Vehicle:
#     def setval(self,model,year,colour):
#         self.model=model
#         self.year=year
#         self.colour=colour
#     def printval(self):
#         print("Vehicle model:",self.model)
#         print("Vehicle Released year:",self.year)
#         print("Vehicle Colour:",self.colour)
# class Car(Vehicle):
#     def printvalue(self,RC_num):
#         self.RC_num=RC_num
#         print("Vehicle model:", self.model,"Vehicle Released year:", self.year)
#         print("Vehicle Colour:", self.colour,"Registration number:",self.RC_num)

# c1=Car()
# c1.setval("R15",2019,"Blue")
# c1.printval()
# c1.printvalue("KL-12BC3478")



# 2.Create an example for three types of inheritance in one program by using College as main class?
class College:
    def setval(self,cname,place):
        self.cname=cname
        self.place=place
        print("College name:",self.cname,"College place:",self.place)
class Teacher:
    def detail(self,tname,salary):
        self.tname=tname
        self.sal=salary
        print("Teacher name",self.tname,"Teacher salary",self.sal)
class Student(College):
    def value(self,sname,sid,sdepartment):
        self.sname=sname
        self.sid=sid
        self.sdep=sdepartment
        print("Student name: ",sname,"Student id: ",sid,"Student Department: ",sdepartment,"College name :",self.cname)
class Library(Student):
    def book(self,bname,author):
        self.bname=bname
        self.author=author
        print("Book name =",self.bname,"Book's Author =",self.author,"Book taken by :",self.sname)
class Office(College,Teacher):
    def print(self):
        print("College name",self.cname)
        print("Teacher name",self.tname)

s=Student()
s.setval("DonBosco College","Thrissur")
s.value("Neethu",12,"MCA")

l=Library()
l.setval("DonBosco College","Ekm")
l.value("anu",16,"MSC")
l.book("C++","Pearson")

of=Office()
of.setval("Hindusthan","Chennai")
of.detail("Anu",30000)
of.print()


