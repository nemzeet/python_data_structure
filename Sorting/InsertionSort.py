# 삽입 정렬.py

dataList = [10,8,1,4,9,3,5,6,2,7]
size = 10

for i in range(1, size):
    tmp = dataList[i]
    idx = -1
    for j in range(i-1,-1,-1):
        if tmp < dataList[j]:
            dataList[j+1] = dataList[j]
        else:
            idx = j
            break

    dataList[idx+1] = tmp

print(dataList)
