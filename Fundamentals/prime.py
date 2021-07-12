# 2,3,5,7,11,13....

# min=int(input("enter the num"))
# max=int(input("enter the max"))
# for a in range(min,max):
#     if a >1:
#         for i in range(2,a):
#             if (a % i)  == 0:
#                 break
#         else:
#                 print(a)

# def prime(num):
#     flg=0
#     for i in range(2,num)
#         if num%i!





# To take input from the user
# num = int(input("Enter a number: "))
#
# # define a flag variable
# flag = False
#
# # prime numbers are greater than 1
# if num > 1:
#     # check for factors
#     for i in range(2, num):
#         if (num % i) == 0:
#             # if factor is found, set flag to True
#             flag = True
#             # break out of loop
#             break
#
# # check if flag is True
# if flag:
#     print(num, "is not a prime number")
# else:
#     print(num, "is a prime number")

# str1="hello world"
# vowels="aeiou"
# for i in str1:
#     if i in vowels:
#         str1.replace(i," ")
# print(str1)

# Remove vowels from the input string given by user?
string = input("Enter any string: ")
newstr = string;
vowels ="aeiou"
for x in string.lower():
    if x in vowels:
        newstr = newstr.replace(x,"");
print("New string after successfully removed all the vowels:");
print(newstr);



