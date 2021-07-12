def admin_required(func):
    def wrapper(user,pin):
        if user!='admin':
            raise Exception("you are not allowed")
        else:
            return func(user, pin)
    return wrapper

@admin_required
def change_pin(user,pin):
    mypin=pin
    return mypin
@admin_required
def delete_ac(user,acno):
    return str(acno)+"deleted"
print(change_pin("admin",1000))
print(delete_ac('user',10034567685))