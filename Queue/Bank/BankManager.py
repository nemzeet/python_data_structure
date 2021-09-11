#기능 구현
from BankModule import *
waitNum=1
bw1 = LinkedQueue("입출금 관련업무")
bw2 = LinkedQueue("예금, 대출 관련업무")
def numIssue(num):
    global waitNum
    if num==1:
        #입출금
        bw1.enQueue(waitNum)
        print(waitNum,"번 손님 ",bw1.task," 창구에 대기 등록 되었습니다.",sep="")
    elif num==2:
        #예금, 대출
        bw2.enQueue(waitNum)
        print(waitNum,"번 손님 ",bw2.task," 창구에 대기 등록 되었습니다.",sep="")
    waitNum+=1
    
def numFind(num):
    curr = bw1.front
    cnt = 0
    while curr is not None:
        cnt+=1
        if curr.data == num:
            print(bw1.task," 창구에서 ",cnt,"번째 입니다.",sep="")
            return
        curr=curr.next
        
    curr = bw2.front
    cnt = 0
    while curr is not None:
        cnt+=1
        if curr.data == num:
            print(bw2.task," 창구에서 ",cnt,"번째 입니다.",sep="")
            return
        curr=curr.next
    print("찾으시는 대기번호는 잘못된 번호입니다.")

def callNum(num):
    if num==1:
        print(bw1.deQueue(),"번 손님 ",bw1.task," 창구로 와주세요",sep='')
    elif num==2:
        print(bw2.deQueue(),"번 손님 ",bw2.task," 창구로 와주세요",sep='')









        
