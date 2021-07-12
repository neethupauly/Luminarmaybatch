eng=int(input("enter english marks"))
hindi=int(input("enter hindi marks"))
soc=int(input("enter social marks"))
total=eng+hindi+soc
print("total marks of the student is:",total)
avg=total/3
print("avg",avg)
if total>=230:
    print("you have secured grade A")
elif total>=200 and total<151:
    print("you have secured grade B")
elif total>=150 and total<101:
    print("you have secured grade c")
elif total>=100:
    print("you have secured grade D")
else:
    print("failed")

