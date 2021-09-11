# Hashing (해싱)



### 정의 <br/>
> 검색 알고리즘, 원하는 데이터를 찾아오는 방법.
> 
> 메모리 낭비를 최소화 하기 위해서 저장할 값을 입력받을 때, 
연산을 통해 특정한 규칙의 주소값을 생성하고, 메모리에 저장 (매핑, mapping)하는 기법이다.
> ex)
>   rule : 들어온 정수값 -1 메모리에 저장
>   (10 -> 9번지, 109999 -> 109998 번지)
<br/>

### 해시 테이블
> Key들이 해싱을 통해 저장될 공간

<br/>

### 해싱의 구조
> 데이터 --(연산)--> 해시함수 --(저장)--> 해시테이블

<br/>

### 해싱 사용 이유
> 1. 저장된 데이터를 연산시키고, 결과로 나온 주소값으로 직접 접근하기 위해 사용
>     (빠르게 저장된 데이터를 접근하게 위해 사용)
> 2. 정수형 데이터 뿐만 아니라 다른 자료형의 데이터 (문자열, ...)또한 저장된 값을 거져올 때 빠르게 가져올 수 있기 때문에 사용

<br/>

### 해시 함수 종류
> #### 1. 나눗셈법
>>입력된 값을 일정한 크기로 나눈 나머지를 주소로 이용하는 방법. 
><br/>
>
> #### 2. 자리수 접기
>>숫자의 각 자리수를 더해 해시값으로 만드는 방법
> 
> <br/>
> 
> ##### 나눗셈 법과 자리수 접기법의 문제점
>     탐색 시간도 빠르고, 메모리의 낭비가 줄어드나 <b>충돌현상</b>과 <b>클러스터</b> 현상이 발생한다.
>   
><br/>
>
> #### 3. 개방주소법
>> 충돌 발생 시 다른 주소값에 데이터를 삽입하는 방식
>> * 선형 탐색법 : 고정폭 이동, 1차 클러스터가 발생할 확률이 높다.
>> * 제곱 탐색법 : 이동 폭이 제곱 수로 늘어난다. 2차 클러스터가 발생한다.
>> * 이중(중복) 해싱 : 해시 함수를 두개 이용하는 것. 해싱을 두번 거치는 것
>
> <br/>
>
> #### 4. 체이닝 (Chaining)
>> 각 해시값에 연결리스트를 할당하여 데이터 삽입 시 충돌이 발생하면, 그 연결리스트에 데이털르 연결하여 삽입한다.
>> 
>> 같은 해시값을 갖는 데이터가 추가되면 한 리스트에만 데이터가 추가되므로 해싱기법을 쓰는 것이 무의미해진다.

<br/>

### 해시 함수의 최종 목표
> 뛰어난 해싱 기법과 체이닝을 적절하게 사용하여 메모리를 관리한다.
