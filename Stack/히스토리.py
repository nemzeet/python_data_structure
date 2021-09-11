#히스토리.py
from 연결스택 import *
#현재 페이지 : ??????
#1. 페이지 이동
#2. 뒤로가기
#3. 앞으로가기
#4. 나가기
page = "빈 페이지"
history = LinkedStack()
back = LinkedStack()
while True:
    if page=='head':
        page = '빈 페이지'
    print("현재 페이지 : "+page)
    print("1. 페이지 이동\n2. 뒤로 가기\n3. 앞으로 가기\n4. 나가기")
    choice = int(input())

    if choice==1:
        #페이지 이동
        page = input("이동할 페이지 : ")
        history.push(page)
        back = LinkedStack()
        
    elif choice==2:
        #뒤로 가기
        if history.is_empty():
            print("이동할 페이지가 없습니다.")
        else:
            back.push(page)
            history.pop()
            print()
            page = history.top.data
            
    elif choice==3:
        #앞으로 가기
        if back.is_empty():
            print("이동할 페이지가 없습니다.")
        else:
            page = back.top.data
            back.pop()
            print()
            history.push(page)
        
    elif choice==4:
        print("안녕히가세요")
        break



