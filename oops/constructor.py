# constructor:to initialize instance variable
# constructor automatically invoke when creating object
class Person:
    def __init__(self,name,age,address):  #__init__  constructor creation
        self.name=name
        self.age=age
        self.add=address
    def printv(self):
        print(self.name,self.age,self.add)
pe=Person("anu",24,"abc")
pe.printv()