stc=[]
def push_element():
    if len(stc)==n:
        print("Stack is full")
    else:
        element=input("Enter the element ")
        stc.append(element)
        print(stc)
def pop_element():
    if not stc:
        print("stack ia empty")
    else:
        element=stc.pop()
        print(element,"removed")
        print(stc)
        
n=int(input("Enter the size  of stack"))
while True:
    print("Select the operation 1.push 2.pop 3.exit")
    choice= int(input())
    if choice==1:
        push_element()
    elif choice==2:
        pop_element()
    elif choice==3:
        break
    else:
        print("Enter the correct operation")
