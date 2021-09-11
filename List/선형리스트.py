#선형리스트.py
class Node:
    data=''
    idx=0

    def __init__(self,data):
        self.idx = Node.idx
        Node.idx+=1
        self.data=data

class LinearList:
    dataList=[]
    count=0

    def __init__(self):
        self.dataList=list()
        self.count=0

    #추가
    def append(self,data):
        newNode = Node(data)
        print('append :',data)
        self.dataList.append(newNode)
        self.count+=1
    #삽입
    def insert(self,idx,data):
        newNode=Node(data)
        print('insert :',data)
        newNode.idx=idx
        for i in range(idx,self.count):
            self.dataList[i].idx+=1
        self.dataList.insert(idx,newNode)
        self.count+=1
        
    #수정
    def update(self,idx,data):
        print('update :',idx)
        self.dataList[idx].data=data
    #삭제
    def delete(self,idx):
        print('delete :',idx)
        for i in range(idx,self.count):
            self.dataList[i].idx-=1
        del self.dataList[idx]
        self.count-=1
        Node.idx-=1
        
    #조회
    def get(self,idx):
        print('get')
        return self.dataList[idx].data
    #목록
    def show(self):
        print('show')
        for i in range(self.count):
            print("%d : %s"%(self.dataList[i].idx,self.dataList[i].data))

li = LinearList()
li.append(10)
li.append(20)
li.append(30)
li.append(40)
li.append(50)
li.insert(2,60)
li.update(5,500)
li.delete(0)

li.show()


print(li.get(3))















    
