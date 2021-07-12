# writing into a file

# f=open("abc",'w')    #opening a file in writing mode
# f.write("hi hello luminar")     #writing data into the file

# the file will be written if there is a filename exists or it will automatically create a file

# copying a file content  into a different file
f1=open("write","r")
f = open("newf",'w')
for i in f1:
    f.write(i)







