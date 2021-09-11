# 버블 정렬 .py

dataList = [10,8,1,4,9,3,5,6,2,7]
size = 10

for i in range(size):
    for j in range(size-1-i): # size-1 해도 무방함
        if dataList[j] > dataList[j+1]:
            dataList[j], dataList[j+1] = dataList[j+1], dataList[j]

print(dataList)