#연결스택.py
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

class LinkedStack:
    def __init__(self):
        self.head=Node('head')
        self.top=self.head

    def push(self,data):
        newNode = Node(data)
        self.top.next=newNode
        self.top = newNode

    def pop(self):
        if not self.is_empty():
            curr = self.head
            while curr.next.next is not None:
                curr = curr.next
            print(curr.next.data,end = '')
            curr.next = None
            self.top=curr

    def is_empty(self):
        return self.head.next is None

'''
s = LinkedStack()
s.push('A')
s.push('B')
s.push('C')
s.pop()
s.push('D')
s.push('E')
s.pop()
s.pop()
s.pop()
s.pop()
'''











