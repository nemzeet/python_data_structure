#원형큐.py
MAX_SIZE=4
class Node:
    def __init__(self,data):
        self.data=data
#컴프리헨션
#[원소 제어문]
#[i for i in range(10)] : [0,1,2,3,4,5,6,7,8,9]


class CircularQueue:
    def __init__(self):
        self.front=0
        self.rear=0
        self.ql = [None for i in range(MAX_SIZE)]

    def is_empty(self):
        return self.rear==self.front and self.ql[self.front]==None

    def is_full(self):
        return self.rear==self.front and self.ql[self.front] is not None

    def enQueue(self,data):
        if not self.is_full():
            newNode = Node(data)
            self.ql[self.rear] = newNode
            self.rear+=1
            self.rear = self.rear%MAX_SIZE
        else:
            print('queue is full!')

    def deQueue(self):
        if not self.is_empty():
            data = self.ql[self.front].data
            self.ql[self.front] = None
            self.front+=1
            self.front = self.front%MAX_SIZE
            return data
        else:
            print('queue is empty!')

    def show(self):
        if not self.is_empty():
            currIdx = self.front
            while True:
                print(self.ql[currIdx].data)
                currIdx+=1
                currIdx%=MAX_SIZE
                if self.ql[currIdx] is None or currIdx == self.front:
                    break
        else:
            print('queue is empty!')

cq = CircularQueue()
cq.enQueue('A')
cq.enQueue('B')
cq.enQueue('C')
cq.enQueue('D')
cq.enQueue('D')
cq.enQueue('D')





    















