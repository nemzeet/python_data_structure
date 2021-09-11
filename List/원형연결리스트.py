#원형연결리스트.py
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class CircularLinkedList:
    def __init__(self):
        self.head=Node('head')
        self.count=0

    def append(self,data):
        newNode = Node(data)
        curr=self.head
        for i in range(self.count):
            curr=curr.next

        curr.next=newNode
        newNode.next=self.head
        self.count+=1

    def insert(self,idx,data):
        newNode=Node(data)
        curr=self.head

        for i in range(idx):
            curr=curr.next

        newNode.next = curr.next
        curr.next=newNode
        self.count+=1

    def update(self,idx,newData):
        curr=self.head
        for i in range(idx+1):
            curr=curr.next
        curr.data=newData

    def delete(self,idx):
        curr=self.head
        for i in range(idx):
            curr=curr.next
        curr.next=curr.next.next
        self.count-=1

    def get(self,idx):
        curr=self.head
        for i in range(idx+1):
            curr=curr.next
        return curr.data

    def show(self):
        curr=self.head
        for i in range(self.count):
            print(curr.data, end='→')
            curr=curr.next
        print(curr.data)

li=CircularLinkedList()
li.append('A')
li.append('B')
li.append('C')
li.insert(1,'D')
li.show()
li.update(1,'E')
li.show()
li.delete(1)
li.show()














        
