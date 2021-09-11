#Library.py
from 이중연결리스트 import *
#이중연결리스트 이용

#책
#도서번호(4자리 숫자)
#도서명
#저자명
class Book:
    def __init__(self,booknum,bookname,author):
        self.booknum=booknum
        self.bookname=bookname
        self.author=author

    #객체 출력시 나올 문자열 설정
    def __repr__(self):
        return self.booknum+'. '+self.bookname+"("+self.author+")"

#1. 도서등록
#2. 도서삭제
#3. 도서검색
#4. 도서목록
#5. 끝내기
bookList = DoubleLinkedList()
print("역삼 도서관 입니다")
while True:
    print('1. 도서등록\n2. 도서삭제\n3. 도서검색\n4. 도서목록\n5. 끝내기')
    choice = int(input())
    if choice==1:
        #도서등록
        booknum = input("도서번호 : ")
        bookname = input('도서명 : ') 
        author = input('저자명 : ')
        newBook = Book(booknum,bookname,author)
        bookList.append(newBook)
        print(newBook)
        print('도서 등록 완료!')
    elif choice==2:
        #도서삭제
        deleteNum=input("삭제할 도서번호 : ")
        flag = False
        for i in range(bookList.count):
            if bookList.get(i).booknum == deleteNum:
                bookList.delete(i)
                print(deleteNum+"번 도서가 삭제되었습니다.")
                flag=True
                break
        if not flag:
            print("찾는 번호가 없습니다.")
            
    elif choice==3:
        #도서검색
        result = set()
        keyword = input('검색할 키워드 : ')
        for i in range(bookList.count):
            if keyword in bookList.get(i).author:
                result.add(bookList.get(i))
            if keyword in bookList.get(i).bookname:
                result.add(bookList.get(i))

        for book in result:
            print(book)
        
    elif choice==4:
        #도서목록
        for i in range(bookList.count):
            print(bookList.get(i))
        pass
    elif choice==5:
        print("안녕히가세요")
        break
    else:
        print("잘못 입력하셨습니다")








        
