# 퀵정렬.py

dataList = [10,8,1,4,9,3,5,6,2,7]
size = 10

def partition(ar, left, right):
    pivot = ar[right]
    idx = left - 1
    for i in range(left, right):
        if ar[i] <= pivot:
            idx += 1
            ar[i], ar[idx] = ar[idx], ar[i]
            print('SWAP: ',ar)
    ar[idx+1], ar[right] = ar[right], ar[idx+1]
    return idx + 1


def quickSort(ar, left, right):
    if left < right:
        q = partition(ar,left,right)
        quickSort(ar, left, q-1)
        quickSort(ar,q+1,right)


quickSort(dataList,0,size-1)
print(dataList)
