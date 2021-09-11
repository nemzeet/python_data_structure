# 체이닝
MAX = 7
def h(x):
    return x%MAX

def digitFolding(s):
    tot = 0
    for ch in s:
        tot += ord(ch)

    return tot

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Chain:
    def __init__(self):
        self.head = None
        self.count = 0

dataList = [Chain() for i in range(MAX)]

def insertData(data):
    newNode = Node(data)
    idx = h(digitFolding(data))
    print('INSERT : ',idx,'-',data)

    if dataList[idx].head is None:
        dataList[idx].head = newNode
    else:
        curr = dataList[idx].head
        for i in range(dataList[idx].count-1):
            curr = curr.next
        curr.next = newNode

    dataList[idx].count += 1

def printData():
    for i in range(MAX):
        curr = dataList[i].head
        print(i,end =' : ')
        for j in range(dataList[i].count-1):
            print(curr.data, end=' -> ')
            curr = curr.next
        if curr is not None:
            print(curr.data)
        else:
            print()

def searchData(data):
    idx = h(digitFolding(data))
    curr = dataList[idx].head
    for i in range(dataList[idx].count):
        if curr.data == data:
            print(idx,'의 ',i,'번째에 위치')
            break
        curr = curr.next
    if curr is None:
        print('존재하지 않음..')



insertData('apple')
insertData('banana')
insertData('cherry')
insertData('durian')
insertData('hello')
insertData('test')
insertData('world')
insertData('korea')
insertData('france')
insertData('google')
insertData('naver')
insertData('kakao')
insertData('germany')
insertData('canada')

printData()

searchData('canada')
searchData('????')

def deleteData(data):
    idx = h(digitFolding(data))
    curr = dataList[idx].head

    if curr is None:
        print('삭제할 데이터 존재하지 않음.')
    else:
        flag = False
        if curr.data == data:
            dataList[idx].head == curr.next
            flag = True
        else:
            for i in range(dataList[idx].count - 1):
                if curr.next.data == data:
                    curr.next = curr.next.next
                    flag = True
                    break
                curr = curr.next
        if flag:
            dataList[idx].count -= 1

def updateData(data, newData):
    idx = h(digitFolding(data))
    nidx = h(digitFolding(newData))
    curr = dataList[idx].head
    if curr is None:
        print('수정할 데이터 없음 ')
    else:
        if idx == nidx:
        # 수정
            for i in range(dataList[idx].count):
                if curr.data == data:
                    curr.data = newData
                    break
            pass
        else:
            deleteData(data)
            insertData(newData)

