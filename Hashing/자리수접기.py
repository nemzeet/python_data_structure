# 자리수 접기.py

'''
107 --> 1 + 7 ---> 8 % 7 ---> 1
'''

MAX = 7
dataList =  ['' for i in range(MAX)]

def h(x):
    return x%MAX

def digitFolding(s):
    tot = 0
    for ch in s:
        # ord = 하나의 문자를 받으면 ASCII 코드로 변환
        tot += ord(ch)
    return tot

while True:
    s = input('저장할 문자열: ')
    saveIdx = h(digitFolding(s))
    dataList[saveIdx] = s
    print('-------------------')
    for i in range(MAX):
        print(i, ':' , dataList[i])
