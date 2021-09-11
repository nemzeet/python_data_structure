# 이중 해싱

MAX = 7
c = 13
j = 1

dataList = ['' for i in range(MAX)]

def h(x):
    return x%MAX

def d(x):
    return x%c+j

def digitFolding(s):
    tot = 0
    for ch in s:
        tot += ord(ch)
    return tot

def insertData(s):
    global j
    idx = h(digitFolding(s))
    while True:
        if dataList[idx%MAX] == '':
            dataList[idx%MAX] = s
            print("INSERT: ",idx%MAX,'-',s)
            break
        else:
            idx = h(digitFolding(s))*d(digitFolding(s))%MAX+j
            j+= 1

def printData():
    for i in range(MAX):
        print(i,':',dataList[i])

insertData('apple')
insertData('banana')
insertData('cherry')
insertData('durian')
insertData('hello')
insertData('test')
insertData('hello')

printData()
