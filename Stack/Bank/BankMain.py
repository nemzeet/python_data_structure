#BankMain.py
#1. 대기번호 발급
#   1. 입출금 관련업무
#   2. 예금, 대출 관련업무
#2. 순서 확인
#   대기번호 : 
#3. 다음 번호 부르기
#   1. 입출금 관련업무
#   2. 예금, 대출 관련업무
#4. 나가기
from BankManager import *
while True:
    print("안녕하세요 국민은행입니다.")
    print("1. 대기번호 발급\n2. 순서 확인\n3. 다음 번호 부르기\n4. 나가기")
    choice = int(input())
    if choice==1:
        choice=int(input("1. 입출금 관련업무\n2. 예금, 대출 관련업무"))
        numIssue(choice)
    elif choice==2:
        num = int(input("대기번호 : "))
        numFind(num)
    elif choice==3:
        choice=int(input("1. 입출금 관련업무\n2. 예금, 대출 관련업무"))
        callNum(choice)
    elif choice==4:
        print("안녕히가세요")
        break
