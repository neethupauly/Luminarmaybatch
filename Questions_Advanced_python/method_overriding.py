class Teacher:
    def printval(self,tname):
        self.tname=tname
        print("inside Teacher method",self.tname)
class Student(Teacher):
    def printval(self,class1):
        self.class1=class1
        print("inside Student method",self.class1)
st=Student()
st.printval("B.COM")
