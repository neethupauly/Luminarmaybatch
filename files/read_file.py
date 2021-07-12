# adding text file to python file
f1=open("firstf","r")    #opening the file in reading mode
# print(f1)              #if we are printing the file directly we will only get the location of the file
# we need to iterate the file to get the data
for i in f1:               #iterating the file
    print(i)               #printing the data in the file