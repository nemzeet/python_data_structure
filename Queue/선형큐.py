#선형큐.py
MAX_SIZE = 5
class Node:
    def __init__(self,data):
        self.data=data

class LinearQueue:
    def __init__(self):
        self.ql = list()
        self.front=0
        self.rear=0
        self.count=0

    def is_empty(self):
        return self.front==self.rear

    def is_full(self):
        return self.rear == MAX_SIZE

    #삽입
    def enQueue(self,data):
        if not self.is_full():
            newNode = Node(data)
            self.ql.insert(self.rear,newNode)
            self.rear+=1
        else:
            print('queue is full!')

    #삭제
    def deQueue(self):
        if not self.is_empty():
            data = self.ql[self.front].data
            self.ql[self.front] = ''
            self.front+=1
            return data
        else:
            print('queue is empty')

    #목록
    def show(self):
        if not self.is_empty():
            for i in range(self.front,self.rear):
                print(self.ql[i].data)
        else:
            print('queue is empty')
lq = LinearQueue()
lq.enQueue('A')
lq.enQueue('B')
lq.enQueue('C')
lq.enQueue('D')
lq.enQueue('E')
lq.enQueue('E')
lq.enQueue('E')

print(lq.deQueue())







    
