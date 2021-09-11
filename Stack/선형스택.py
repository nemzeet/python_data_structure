#선형스택.py
MAX_SIZE = 5
class Node:
    def __init__(self,data):
        self.data=data

class Stack:
    def __init__(self):
        self.stackList = list()
        self.top = 0

    def push(self,data):
        if not self.is_full():
            newNode = Node(data)
            self.stackList.insert(self.top,newNode)
            self.top+=1
        else:
            print('stack is full!')

    def pop(self):
        if not self.is_empty():
            print(self.stackList[self.top-1].data)
            del self.stackList[self.top-1]
            self.top-=1
        else:
            print('stack is empty!')

    #메소드의 이름에 is, has가 있다면 보통 리턴은 Bool타입(True,False)
    def is_empty(self):
        return self.top==0
        
    def is_full(self):
        return self.top == MAX_SIZE

sl = Stack()
sl.push('A')
sl.push('B')
sl.push('C')
sl.push('D')
sl.push('E')
sl.push('E')#stack is full!
sl.push('E')#stack is full!

sl.pop()#E
sl.pop()#D
sl.pop()#C

sl.push('F')
sl.pop()#F
sl.pop()#B
sl.pop()#A
sl.pop()#stack is empty!











