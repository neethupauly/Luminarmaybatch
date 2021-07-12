# exception handling
# solving unexpected errors
# try block......exceptional code
# except block.....solving code
# finally block.....anything

# zero division error
# no1=int(input("enter num1"))
# no2=int(input("enter num2"))
# try:
#     print(no1/no2)
# except Exception as w:
#     print("error occured",w)
# finally:
#     print("inside finally")

# try block works all the time
# except block works only if there is an error
# finally block works all the time

# index error index out of range

b = int(input("enter"))
a = [1, 2, 3, 4]
try:
    print(a[b])
except Exception as r:
    print("exception occured",r)
finally:
    print("solve")



