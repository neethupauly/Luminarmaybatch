# dictionaries
# keys and value pairs
# keys should be unique not be repeatable
# values can be same
# dictionaries are mutable
# nesting is possible using keys


# dict1={'name':'neethu','age':24,'class':'first'}
# print('dict:name',dict1['name'])
# print('dict:age',dict1['age'])
# dict1['age']=23        #update existing entry
# dict1['school']='Donbosco school'   #adding new entry
# dict1.update({'location':'kochi'})
# print(dict1)
# del dict1['class'] #deleting entry with key
# print(dict1)
# dict1.clear()      #removing all entries in a dictionary
# print(dict1)
# del dict1          #deleting dictionary
# dict={} #empty dictionary creation


# a="hello world"
# b=a.split(" ")   #for splitting the string
# print(b)         #result will be of list type
# for i in b:
#     print(i)

# home work
# enter: hello hi hello world
# {'hello':2,'hi':1,'world':1}


# dict={}
# a=input("enter a string")
# words=a.split(" ")
# for i in words:
#     if i not in dict:
#         dict.update({i:1})
#     else:
#         val=int(dict[i])
#         val+=1
#         dict.update({i:val})
# print(dict)

# another method
# for i in words:
#     if i not in dict:
#          count=words.count(i)
#          dict.update({i:count})
# print(dict)


# nested dictionary
dict={'name':'neethu','class':{'hello':2}}
print(dict)

