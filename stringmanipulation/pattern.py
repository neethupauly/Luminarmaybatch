# rectangle
def pattern(row):
    for i in range(0,row,1):
        for j in range(0,row):
            print("*",end=" ")
        print("\r")
pattern(5)



# increasing
def num(row):
    no=1
    for i in range(0,row,1):
        for j in range(0,i+1):

            print(no,end=" ")
            no=no+1
        print("\r")
num(5)

def num(row):
    for i in range(0,row,1):
        no=1
        for j in range(0,i):
            print(no,end=" ")
            no=no+1
        print("\r")
num(6)

# pyramid pattern

def  pyramid(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+1):
            print("*",end=" ")
        print("\r")
pyramid(5)

n=int(input("enter the number of levels :"))
for i in range(1,n):
    print(" " * (n-i),end=" ")
    for j in range(0,i):
        print("*",end=" ")
    print()

# trapizoid
def triangle(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k-1
        for j in range(0,i+5):
            print("*",end=" ")
        print("\r")
triangle(6)


# parellelogram
def  parellel(n):
    k=n
    for i in range(0,n):
        for r in range(0,k):
            print(end=" ")
        k=k+1
        for j in range(0,n):
            print("*",end=" ")
        print("\r")
parellel(5)









