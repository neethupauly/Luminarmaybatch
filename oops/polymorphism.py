# polymorphism - many forms
# method name can be same is called polymorphism
# two concepts
#    1...overloading  - python doesn't support overloading
#                       method name can be same but arguments can be different
#    2...overriding  -same method name and same num of arguments

# method overloading
# class Operators:
#     def num(self,n1,n2):
#         self.n1=n1
#         self.n2=n2
#         print(self.n1+self.n2)
# class Display(Operators):
#     def num(self,n3):
#         self.n3=n3
#         print(self.n3)
#
# d=Display()
# d.num(3)   #python doesn't support overloading
#             #python only supports the latest created method
#
#
# # method overriding
#
class Person:
    def printval(self,name):
        self.name=name
        print("inside person method",self.name)
class Child(Person):
    def printval(self,class1):
        self.class1=class1
        print("inside child method",self.class1)
ch=Child()
ch.printval("abc")

# method overriding overrides the parent class method
# and prints the output of child class method
