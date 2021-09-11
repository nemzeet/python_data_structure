#LibraryView.py
#View : 사용자의 입출력만 담당하는 파일
#입력, 출력, 기능이 구현된 함수 또는 메소드 호출

from LibraryManager import *
print("역삼 도서관 입니다")
while True:
    print('1. 도서등록\n2. 도서삭제\n3. 도서검색\n4. 도서목록\n5. 끝내기')
    choice = int(input())
    if choice==1:
        #도서등록
        booknum = input("도서번호 : ")
        bookname = input('도서명 : ') 
        author = input('저자명 : ')
        print(addBook(booknum,bookname,author))
        print('도서 등록 완료!')
        
    elif choice==2:
        #도서삭제
        deleteNum=input("삭제할 도서번호 : ")   
        if deleteBook(deleteNum):
            print(deleteNum+"번 도서가 삭제되었습니다.")
        else:
            print("찾는 번호가 없습니다.")
            
    elif choice==3:
        #도서검색
        keyword = input('검색할 키워드 : ')
        result = searchBook(keyword)
        for book in result:
            print(book)
        
    elif choice==4:
        #도서목록
        print(showList())
        
    elif choice==5:
        print("안녕히가세요")
        break
    else:
        print("잘못 입력하셨습니다")








        
