# data structures....store data
# stack
# stack operations : 1.push-adding elements to the stack
#                  : 2.pop-remove elements
# lifo-last in first out


# 1st method
l1=[]
a=True
size=int(input("enter the size"))
while a:
    ch=input(("enter the operation you want to perform \n 1)push  2)pop  3)display"))

    if ch=="1":
        if len(l1)<size:
            b = int(input("enter the element you want to push"))
            l1.append(b)
        else:
            print("size of stack is exceeded")
    elif ch=="2":
        if len(l1)==0:
            print("stack is empty")
        else:
            l1.pop()
            print("element popped")
    elif ch=="3":
        print(l1)
# elif ch=="2":
#     p=int(input("enter the element you want to pop"))
#     pop1(p)
# elif ch=="3":
#     display(l1)
#     print(l1)
#



# 2nd method
# stk=[]
# size=int(input("enter the stack size"))
# top=0
#
#
# n=0
# def push():
#     global top,size
#     if(top>size):
#         print("stack is full")
#     else:
#         p=int(input("enter the element you want to push"))
#         stk.append(p)
#         top+=1
# def pop():
#     global top,size
#     if(top<=0):
#         print("stack is empty")
#     else:
#         stk.pop()
#         top-=1
# def display():
#     print(stk)
#
while n!=1:
    print("enter the operation want to perform")
    opt=int(input("press 1)push 2)pop 3)display"))
    if opt==1:
        push()
    elif opt==2:
        pop()
    elif opt==3:
        display()
    n=int(input("do you want to continue press 1 for exit"))
