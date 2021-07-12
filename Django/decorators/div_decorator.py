def zero_not_required(func):
    def wrapper(num1,num2):
        if (num1==0) | (num2==0):
            raise Exception("invalid parameter")
        else:
            func(num1,num2)
    return wrapper

def decorator_div(func):
    def wrapper(num1,num2):
        if num1<num2:
            (num1,num2)=(num2,num1)
            return func(num2,num1)
        else:
            return func(num1,num2)
    return wrapper


@zero_not_required
@decorator_div
def div(num1,num2):
    return num1/num2
try:
    print(div(10,0))
except Exception as e:
    print(e.args)

# print(div(2,20))
