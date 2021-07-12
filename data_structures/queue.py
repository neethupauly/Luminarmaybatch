#queue
# insertion ...enqueue
# deletion....dequeue
# first in first out

queue=[]
front=0   #the  first or top element number
size=int(input("enter the queue size"))
n=0


def enqueue():
    global front,size
    if front>size:
        print("queue is full...!!")
    else:
        en=int(input("enter an element to insert to the queue"))
        queue.append(en)
        front=front+1
        print(queue)
def dequeue():
    global front,size
    if front<=0:
        print("queue is empty..!")
    else:
        queue.remove(queue[0])

        print("one element deleted from the queue")
        front=front-1
def display():
    print("the queue is",queue)

while n!=1:
    print("enter the function you want to perform")
    fun=input("1)enqueue  2)dequeue  3)display")

    if fun=="1":
        enqueue()
    elif fun=="2":
        dequeue()
    elif fun=="3":
        display()
    # else:
    #     print("invalid function entered")
    n=int(input("do you want to continue? press 1 for exit 0 for continue"))







