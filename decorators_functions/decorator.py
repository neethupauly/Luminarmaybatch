# decorators_functions are used to modify or add changes to the functions

def check(func):
    def wrapper(name,age):
        if age<18:
            print("not eligible")
        else:
            return func(name,age)
    return wrapper

@check          #should declare before function
def vaccine(name,age):
    print(name,"eligible for vaccination")
vaccine("anu",19)

# we can use different functions to check eligibility
@check
def eligible(name,age):
    print(name,age)
eligible("Neethu",23)

