# multi_level inheritance/hierarchical inheritance

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child(Person):
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Student(Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print("roll no is : ",self.rollno,"and mark is",self.mark)
ch=Child()
ch.pvalue("anu",24)
ch.cvalue("abc",12)


st=Student()
st.svalue(4,80)
st.svalue(5,70)
st.cvalue("XYZ",12)
st.pvalue("Neethu",25)


# 2nd program-multilevel

# class Person:
#     def pvalue(self, name, age):
#         self.name = name
#         self.age = age
#         print(self.name, self.age)
#
#
# class Parent(Person):
#     def cvalue(self, adrs, phnno):
#         self.adrs = adrs
#         self.phnno = phnno
#         print(self.adrs, self.phnno)
#
#
# class Employee(Parent):
#     def Edetails(self, Eid, company, salary):
#         self.eid = Eid
#         self.comp = company
#         self.sal = salary
#         print(self.eid, self.comp, self.sal, self.phnno)
#
#
# p = Parent()
#
# p.pvalue("Amal", 27)
# p.cvalue("Kochupurakkal house", 9089776543)
#
# e = Employee()
#
# e.cvalue("Alukkaparambil house", 9087665432)
# e.pvalue("Anu", 25)
# e.Edetails(2, "TCS", 50000)

# work
# person,child,parent,student 4 classes
# child,parent -person
# student-child

# 3rd program

# class Person:
#     def pvalue(self,name,age):
#         self.name=name
#         self.age=age
#         print(self.name,self.age)
#
#
# class Child(Person):
#     def cvalue(self,address,cls):
#         self.address=address
#         self.cls=cls
#         print(self.address,self.cls)
#
#
# class Parent(Person):
#     def avalue(self, phnno):
#         self.phnno = phnno
#         print(self.phnno)
#
#
# class Student(Child):
#     def svalue(self,mark,rollno):
#         self.mark=mark
#         self.rollno=rollno
#         print(self.mark,self.mark)
#
# c=Child()
# c.cvalue("ABC","MCA")
# c.pvalue("Neethu",24)
#
# p=Parent()
# p.pvalue("anu",23)
# p.avalue(9895345678)
#
# s=Student()
# s.cvalue("xyz","BCA")
# s.svalue(78,304)

