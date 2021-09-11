MAX = 7
move = 2 # MAX의 서로수로 충돌이 일어나지 않게 고정폭 추가

dataList = ['' for i in range(MAX)]

def h(x):
    return x%MAX
def digitFloding(s):
    tot = 0
    for ch in s:
        tot += ord(ch)
    return tot
'''
cnt = 0
for i in range(3):
    data = int(input('데이터: '))
    idx = h(data)
    while True:
        if cnt == MAX+1:
            print('메모리가 가득 찼습니다.')
            break

        if dataList[idx] == '':
            dataList[idx] = data
            break
        else:

            idx = (idx + move) % MAX
            cnt += 1
'''



dataList = ['' for i in range(MAX)]
cnt  = 0
for i in range(MAX):
    s = input('문자열: ')
    idx = h(digitFloding(s))
    while True:
        if cnt == MAX+1:
            print('메모리가 가득 찼습니다.')
            break

        if dataList[idx] == '':
            dataList[idx] = s
            for j in range(MAX):
                print(j,':',dataList[j])
            break
        else:
            idx = (idx+move)%MAX
            cnt += 1
