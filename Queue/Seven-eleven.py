#편돌이
from 연결큐 import *
#안녕하세요 세븐일레븐 입니다
#1. 냉동식품
#   1. 냉동식품 추가하기
#   2. 폐기물 빼기
#   3. 뒤로가기
#2. 음료수
#   1. 음료수 추가하기
#   2. 음료수 빼기
#   3. 뒤로가기
#3. 나가기

food = LinkedQueue()
drink = LinkedQueue()

print("☆★☆⑦안녕하세요 세븐일레븐 입니다⑪★☆★")
while True:
    print("1. 냉동식품 관리하기\n2. 음료수 관리하기\n3. 나가기")
    choice = int(input())

    if choice==1:
        #냉동식품
        while True:
            print("===========냉동식품 냉장고===========")
            food.show()
            print("====================================")
            
            
            
            choice=int(input())

            if choice==1:
                #추가
                food.enQueue(input("추가할 상품 : "))
            elif choice==2:
                #빼기
                print(food.deQueue()+"을(를) 폐기합니다")
            elif choice==3:
                break
            else:
                print("잘못 입력하셨습니다.")

    elif choice==2:
        #음료수
        while True:
            print("===========음료수 냉장고===========")
            drink.show()
            print("====================================")
            print("1. 음료수 추가하기\n2. 음료수 빼기\n3. 뒤로가기")
            choice=int(input())

            if choice==1:
                #추가
                drink.enQueue(input("추가할 상품 : "))
            elif choice==2:
                #빼기
                print(drink.deQueue()+"을(를) 꺼냅니다")
            elif choice==3:
                break
            else:
                print("잘못 입력하셨습니다.")

    elif choice==3:
        #나가기
        print("프로그램을 종료합니다.")
        break

    else:
        print("잘못 입력하셨습니다")
