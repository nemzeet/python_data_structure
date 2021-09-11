# 해시 함수
MAX = 7
dataList = ['' for i in range(MAX)]

def h(data):
    return data%MAX

for i in range(3):
    data = int(input('저장할 값: '))
    dataList[h(data)] = data

for i in range(MAX):
    print(i, ':' , dataList[i])

findData = int(input('찾을 값 : '))

# 기존
'''
for i in range(MAX):
    if dataList[i] == findData:
        print(findData, '는', i,'번째에 있습니다.')
        break
'''

print(findData, '는', h(findData),'번째에 있습니다.')