# def check(func):




employees={
    1000:{"eid":1000,"ename":"ajay","salary":34000,"designation":"developer"},
    1001:{"eid":1001,"ename":"arun","salary":38000,"designation":"developer"},
    1002:{"eid":1002,"ename":"akhil","salary":21000,"designation":"hr"},
    1003:{"eid":1003,"ename":"anu","salary":45000,"designation":"analyst"}
}

# print(employees[1002]["ename"])
# print(employees[1002])
emp=int(input("enter a key"))
value=input("enter a value")
if emp in employees  and value in employees[emp]:
    print(employees[emp][value])
else:
    print("invalid key or value")

