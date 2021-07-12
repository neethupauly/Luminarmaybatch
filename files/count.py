f1=open("new","r")

dict={}
for i in f1:
    words=i.rstrip("\n").split(" ")    #rstrip is used to eliminate \n in the output
    # print(words)                                     # if there are more than one line in the file
    for word in words:
        if word not in dict:
            dict.update({word:1})
            c=words.count(word)
            dict.update({word:c})
print(dict)

