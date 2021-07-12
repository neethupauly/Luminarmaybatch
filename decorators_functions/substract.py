# interchanged and substracted elements

def interchange(func):

    def wrapper(num1,num2):
        if num1<num2:       #swapping simple way
            (num1,num2)=(num2,num1)
            return func(num1,num2)
        else:
            return func(num1,num2)
    return wrapper
@interchange
def sub(no1,no2):
    return no1-no2
print(sub(3,8))