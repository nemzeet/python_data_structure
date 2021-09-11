#이중연결리스트.py
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None
        
class DoubleLinkedList:
    def __init__(self):
        self.head = Node('head')
        self.tail = Node('tail')
        self.head.next = self.tail
        self.tail.prev = self.head
        self.count=0

    #추가
    def append(self,data):
        newNode = Node(data)

        #추가하는 노드의 next는 무조건 tail일 수밖에 없다
        #newNode의 next에 self.tail 주소값 넣기
        newNode.next = self.tail

        #newNode의 prev은 기존의 가장 마지막 노드를 담아주어야 한다
        #현재 tail의 prev이 기억하고 있는 노드로 넣어주면 된다
        newNode.prev = self.tail.prev

        #기존의 가장 마지막 노드는 더이상 next가 tail이 아니고
        #새로 추가되는 노드이므로 그 노드의 next를 newNode로 바꾸어준다
        self.tail.prev.next = newNode

        #새로운 노드가 추가되었으므로 tail의 prev을 newNode로 바꾸어준다
        self.tail.prev = newNode
        self.count+=1

    #삽입
    def insert(self,idx,data):
        newNode = Node(data)
        if idx<=self.count/2:
            #head부터 next로 접근
            curr=self.head
            #추가하려는 위치 전까지 이동하기 위해 idx만큼 for문 반복
            for i in range(idx):
                curr=curr.next
            #newNode 세팅
            #추가하는 노드의 prev은 추가하는 위치 이전노드(curr)
            newNode.prev = curr
            #추가하는 노드의 next는 추가하는 위치 다음노드(curr.next)
            newNode.next = curr.next

            #이전노드(curr)의 next는 추가한 노드로 바꾸기
            curr.next=newNode
            #다음노드(newNode.next)의 prev은 추가한 노드로 바꾸기
            newNode.next.prev = newNode

        else:
            #tail부터 prev으로 접근
            curr=self.tail
            for i in range(self.count-idx):
                curr=curr.prev
            newNode.next = curr
            newNode.prev = curr.prev

            curr.prev=newNode
            newNode.prev.next = newNode            
        self.count+=1
    #수정
    def update(self,idx,newData):
        find = self.findNode(idx)
        find.data=newData

    #삭제
    def delete(self,idx):
        if idx<=self.count/2:
            curr=self.head
            for i in range(idx):
                curr=curr.next
            #curr : 삭제하려는 위치 이전노드
            #curr.next : 삭제하려는 위치
            #curr.next.next : 삭제하려는 위치 다음노드
            curr.next.next.prev = curr
            curr.next = curr.next.next

        else:
            curr = self.tail
            for i in range(self.count-idx-1):
                curr=curr.prev
            #curr : 삭제하려는 위치 다음노드
            #curr.prev : 삭제하려는 위치
            #curr.prev.prev : 삭제하려는 위치 이전노드
            curr.prev.prev.next = curr
            curr.prev = curr.prev.prev
        self.count-=1

    def findNode(self,idx):
        curr=None
        if idx<=self.count/2:
            curr = self.head
            for i in range(idx+1):
                curr=curr.next
        else:
            curr = self.tail
            for i in range(self.count-idx):
                curr=curr.prev
        return curr

    #조회
    def get(self,idx):
        curr=None
        if idx<=self.count/2:
            curr=self.head
            for i in range(idx+1):
                curr=curr.next
        else:
            curr=self.tail
            for i in range(self.count-idx):
                curr=curr.prev
        return curr.data

    #목록
    def ascShow(self):
        #인덱스 오름차순(head부터 next)
        curr = self.head
        for i in range(self.count+1):
            print(curr.data,end=">>")
            curr=curr.next
        print(curr.data)

    def descShow(self):
        #인덱스 내림차순(tail부터 prev)
        curr = self.tail
        for i in range(self.count+1):
            print(curr.data,end = ">>")
            curr=curr.prev
        print(curr.data)

    def show(self,order=True):
        if order:
            self.ascShow()
        else:
            self.descShow()

'''
li=DoubleLinkedList()
li.append('A')
li.append('B')
li.append('C')
li.insert(0,'D')
li.insert(4,'E')
#li.ascShow()
#li.descShow()
li.show()
'''





