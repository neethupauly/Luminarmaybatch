# **kwargs is accepted as dictionary (key value pairs)

def login_required(func):
    def wrapper(self,acno,*args,**kwargs):
        if (self.session["user"]==acno):
            func(self,acno,*args,**kwargs)
        else:
            raise Exception("login required")
    return wrapper


class Bank:
    users = {
        1000: {"accoun_num": 1000, "password": "user1", "balance": 3000},
        1001: {"accoun_num": 1001, "password": "user2", "balance": 4000},
        1002: {"accoun_num": 1002, "password": "user2", "balance": 5000},
        1003: {"accoun_num": 1003, "password": "user3", "balance": 6000}
    }
    session={}   #to store account number of logged in user
    session["user"]=0
    def validate_account(self,accno):
        if accno in self.users:
            return  True
        else:
            return False
    def authenticate(self,**kwargs):  #kwargs={acc_no:1000,password:test}
        acc_no=kwargs["acc_no"]
        password=kwargs["password"]
        user=self.validate_account(acc_no)
        if user:
            if (password==self.users[acc_no]["password"]):
                self.session["user"]=acc_no     #session={user:1000}
                return acc_no
            else:
                return -1   #invalid password
        else:
            return 0     #print("invalid account number or password")

    @login_required
    def balance_enquiry(self,acc_no,*args,**kwargs):
        if acc_no==self.session["user"]:
            print(self.users[acc_no]["balance"])
        else:
            print("you must login")

    def fund_transfer(self,user,to_acno,amt):
        if self.validate_account(to_acno):
            balance=self.users[user]["balance"]
            if balance<amt:
                print("insufficient balance")
            else:
                self.users[user]["balance"]-=amt
                self.users[to_acno]["balance"]+=amt
    def logout(self):
        self.session["user"]=0
# obj=Bank()
# user=obj.authenticate(acc_no=1000,password="user1")
# obj.balance_enquiry(user)
# print(user)

obj1=Bank()
user=obj1.authenticate(acc_no=1001,password="user2")
if (user==1)  | (user==0):
    print("failed")
else:
    obj1.balance_enquiry(user)

obj1.balance_enquiry(user)
obj1.fund_transfer(user,1000,3000)
obj1.logout()

# users={
#         1000:{"accoun_num":1000,"password":"user1","balance":3000},
#         1001:{"accoun_num":1001,"password":"user2","balance":4000},
#         1002:{"accoun_num":1002,"password":"user2","balance":5000},
#         1003:{"accoun_num":1003,"password":"user3","balance":6000}
#     }
# def authenication(**kwargs):
#     user=kwargs["accno"]
#     password=kwargs["password"]
#     if user in users:
#         if password==users[user]["password"]:
#             print("success")
#         else:
#             print("invalid password")
#     else:
#         print("invalid account umber")
#
# def get_balance(accno):
#     if accno in users:
#         print(users[accno]["balance"])
#     else:
#         print("invalid account number")
# get_balance(1000)
# authenication(accno=1000,password="user1")
#



# class Bank
# authenticate(acno,password)
# balance enquiry(accno)
# fund transfer(accno,toaccno,amt)
#- underscore -snake notation

