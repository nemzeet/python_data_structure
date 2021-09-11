#BankModule.py
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedQueue:
    def __init__(self,task):
        self.front=None
        self.rear=None
        self.task=task

    def is_empty(self):
        return self.front is None

    def enQueue(self,data):
        newNode = Node(data)
        if self.is_empty():
            self.front = newNode
        else:
            self.rear.next = newNode
        self.rear = newNode

    def deQueue(self):
        if not self.is_empty():
            data = self.front.data
            self.front=self.front.next
            return data

    def show(self):
        curr =self.front
        while curr is not None:
            print(curr.data)
            curr=curr.next











