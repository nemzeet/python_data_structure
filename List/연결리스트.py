class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedList:
    def __init__(self):
        self.head=Node('head')
        self.count=0

    def append(self,data):
        newNode = Node(data)
        curr=self.head
        for i in range(self.count):
            curr=curr.next
        curr.next = newNode
        self.count+=1

    def insert(self,idx,data):
        newNode=Node(data)
        curr=self.head
        for i in range(idx):
            curr=curr.next
        newNode.next=curr.next
        curr.next=newNode
        self.count+=1

    def delete(self,idx):
        curr=self.head
        for i in range(idx):
            curr=curr.next
        curr.next=curr.next.next
        self.count-=1










