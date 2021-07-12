# multiple inheritance

class Person:
    def pvalue(self,name,age):
        self.name=name
        self.age=age
        print(self.name,self.age)
class Child:
    def cvalue(self,adrs,cls):
        self.adrs=adrs
        self.cls=cls
        print(self.adrs,self.cls)
class Student(Person,Child):
    def svalue(self,rollno,mark):
        self.rollno=rollno
        self.mark=mark
        print(self.name,"roll no is : ",self.rollno," class is",self.cls,"and mark is",self.mark)
st=Student()
st.pvalue("Neethu's",25)
st.cvalue("ABC","B.COM")
st.svalue(304,90)