# SchoolSchool.py
studentList = []

class Student:
    def __init__(self, stunum, stuname, stumajor):
        self.stunum = stunum
        self.stuname = stuname
        self.stumajor = stumajor
        self.scores = {}

    def __repr__(self):
        return self.stuname+'('+self.stunum+')' + ' - ' + self.stumajor

def bubbleSort(stuList): # 학번 정렬
    for i in range(len(stuList)):
        for j in range(len(stuList)-1-i):
            if int(stuList[j].stunum) > int(stuList[j+1].stunum):
               stuList[j], stuList[j+1] = stuList[j+1], stuList[j]

while True:

    print('1. 학생 정보 기입\n2. 학생 점수 기입\n3. 학생 점수 조회\n4. 전체 학생 목록\n5. 나가기')
    choice = int(input('항목 선택: '))
    if choice == 1:
        stunum = input('학번: ')
        stuname = input('이름: ')
        stumajor = input('전공: ')

        newStudent = Student(stunum, stuname, stumajor)
        studentList.append(newStudent)
        bubbleSort(studentList)
        print(stuname,'님 정보 기입 완료!')

    elif choice == 2:
        stunum = input('학번: ')
        for s in studentList:
            if stunum == s.stunum:
                subject = input('과목: ')
                score = input('점수: ')
                s.scores[subject] = score

    elif choice == 3:
        stunum = input('학번: ')
        for s in studentList:
            if stunum == s.stunum:
                for k,v in s.scores.items():
                    print(k+' : '+v)

    elif choice == 4:
        print('전체 학생 목록')
        '''
        for s in studentList:
            print(s.stuname+'('+s.stunum+')' + ' - ' + s.stumajor)
        '''
        t = ''
        for student in studentList:
            if student.stunum[:2]:
                t = student.stunum[:2]
                print('=========='+t+'학번==========')
            print(student)
    elif choice == 5:
        break

    else:
        print('잘못된 입력 \n')


'''
1. 학생 정보 기입
    학번: 
    이름:
    전공:
    남지수님 정보 기입 완료!

2. 학생 점수 기입
    학번:
    과목:
    점수:
3. 학생 점수 조회
    학번:
    C언어 : a-
    Java : b+
    Python : a0
4. 전체 학생 목록
    홍길동 - 컴퓨터공학과
    이순신 - 해양조선학과
5. 나가기
'''