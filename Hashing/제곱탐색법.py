# 제곱탐색법
# 충돌시 제곱만큼 건너뛴 주소에 데이터를 삽입
# 100에서 충돌발생 > 101 > 104 > 109

MAX = 7
move = 1
dataList = ['' for i in range(MAX)]

def h(x):
    return x%MAX

def digitFolding(s):
    tot = 0
    for ch in s:
        tot += ord(ch)
    return tot

for i in range(MAX):
    s = input('문자열: ')
    idx = h(digitFolding(s))
    temp = idx

    while True:
        if dataList[temp] == '':
            dataList[temp] = s
            move = 1

            for j in range(MAX):
                print(j,':',dataList[j])

            break
        else:
            temp = (idx+move**2)%MAX
            move += 1

s = input('찾을 문자열: ')
idx = h(digitFolding(s))
temp = idx
move = 1
while True:
    if dataList[temp] == s:
        print(temp,'위치에 존재합니다.')
        break
    else:
        temp = (idx+move**2)%MAX
        move += 1