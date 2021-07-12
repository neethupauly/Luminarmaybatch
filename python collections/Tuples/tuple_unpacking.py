# unpacking tuple

my_tuple=3,4.5,"dog"
print(my_tuple)

a,b,c=my_tuple   #unpacking tuple

print(a)    #3
print(b)    #4.5
print(c)    #dog


tu=1,2,3,4,5
a,b,c,d,e=tu
sum=a+b+c+d+e
print(sum)


# tuple slicing
print(tu[1])
print(tu[-2])
print(tu[::-1])   #reverse
print(tu[1:5:2])


