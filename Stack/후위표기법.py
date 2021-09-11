#후위표기법.py
#'문자열'.isdigit()
#'문자열'[0] : 문자열의 0번째 글자
#from 연결스택 import *
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
            data = curr.next.data
            curr.next = None
            self.top=curr
            return data
    def is_empty(self):
        return self.head.next is None


def getPriority(oper):
    if oper == '+' or oper == '-':
        return 1
    elif oper == '*' or oper == '/':
        return 2
    else:
        return 0

operList = LinkedStack()
#괄호 없는 수식
'''
while True:
    eq = input('수식 입력 : ')
    for i in range(len(eq)):
        if eq[i].isdigit():
            print(eq[i],end='')

        else:
            if operList.is_empty():
                operList.push(eq[i])
            else:
                while getPriority(operList.top.data)>=getPriority(eq[i]):
                    operList.pop()
                    if operList.is_empty():
                        break
                operList.push(eq[i])

    while not operList.is_empty():
        operList.pop()
    print()
'''
#괄호 있는 수식
while True:
    eq = input('수식 입력 : ')
    for i in range(len(eq)):
        if eq[i].isdigit():
            print(eq[i],end='')

        else:
            if operList.is_empty() or eq[i] == '(':
                operList.push(eq[i])
            else:
                if eq[i]==')':
                    while not operList.top.data == '(':
                        print(operList.pop(),end="")
                    operList.pop()
                else:
                    while getPriority(operList.top.data)>=getPriority(eq[i]):
                        print(operList.pop(),end="")
                        if operList.is_empty():
                            break
                    operList.push(eq[i])
    while not operList.is_empty():
        print(operList.pop(),end="")
    print()




    
