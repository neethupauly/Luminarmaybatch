# Create objects of the following file and print the details of student with maximum mark?
# anu,1,bca,200 rahul,2,bba,177 vinod,3,bba,187 ajay,4,bca,198 maya,5, bba,195

class Student:
    def __init__(self,name,sid,department,mark):
        self.name=name
        self.sid=sid
        self.dep=department
        self.mark=mark
    def printdata(self):
        print(self.name)
        print(self.sid)
        print(self.dep)
        print(self.mark)
l1=[]
f1=open("file2","r")
for i in f1:
    words=i.rstrip("\n").split(",")
    # print(words)
    name=words[0]
    rollno=words[1]
    dep=words[2]
    mark=words[3]
    s1=Student(name,rollno,dep,mark)
    # s1.printdata()
    l1.append(s1)
max_mark=[]
for j in l1:
    max_mark.append(j.mark)
    print(max_mark)
for j in l1:
    if (j.mark==max(max_mark)):
        print(j.sid,j.name,j.dep,j.mark)





