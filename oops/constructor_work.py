# teacher tname,subject,departm,college-id
class Teacher:
    college="Hindusthan"
    def __init__(self,tname,subject,college_id):
        self.tname=tname
        self.sub=subject
        self.clgid=college_id
    def printval(self):
        print(self.tname,self.sub,self.clgid,Teacher.college)

n=input("enter teacher's name")
s=input("enter subject")
c=input("enter clg id")
t=Teacher(n,s,c)

t.printval()
n=input("enter teacher's name")
s=input("enter subject")
c=input("enter clg id")
r=Teacher(n,s,c)
r.printval()

