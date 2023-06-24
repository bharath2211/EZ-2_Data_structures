queue=[]
def enqueue():
    if len(queue)==n:
        print("queue is full")
    else:
        element=input("Enter the element ")
        queue.append(element)
        print(queue)
def dequeue():
    if not queue:
        print("stack ia empty")
    else:
        element=queue.pop()
        print(element,"removed")
        print(queue)
        
n=int(input("Enter the size  of stack"))
while True:
    print("Select the operation 1.push 2.pop 3.exit")
    choice= int(input())
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")
