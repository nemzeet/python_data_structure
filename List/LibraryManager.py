#LibraryManager.py
#기능 담당하는 파일
#비즈니스 로직(프로그램을 정상적으로 작동하게 하기 위한
#알고리즘들)들을 구현해 놓은 함수, 메소드, 클래스의 선언들이 있다.
#이곳에 선언되어 있는것들을 View에서 호출하여 사용한다.
from 이중연결리스트 import *
class Book:
    def __init__(self,booknum,bookname,author):
        self.booknum=booknum
        self.bookname=bookname
        self.author=author

    def __repr__(self):
        return self.booknum+'. '+self.bookname+"("+self.author+")"

bookList = DoubleLinkedList()

def addBook(booknum,bookname,author):
    newBook = Book(booknum,bookname,author)
    bookList.append(newBook)
    return newBook

def deleteBook(deleteNum):
    for i in range(bookList.count):
        if bookList.get(i).booknum == deleteNum:
            bookList.delete(i)
            return True
    return False
        
def searchBook(keyword):
    result = set()
    for i in range(bookList.count):
        if keyword in bookList.get(i).author:
            result.add(bookList.get(i))
        if keyword in bookList.get(i).bookname:
            result.add(bookList.get(i))
    return result

def showList():
    result =""
    for i in range(bookList.count): 
        result+=repr(bookList.get(i))+"\n"
    return result
















