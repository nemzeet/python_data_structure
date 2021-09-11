# List (리스트)
### 정의
> 유한한 원소의 나열된 묶음 <br/>
<br/>

### 노드
> 데이터, 다른 노드와의 관계를 저장할 공간 등을 포함하고 있는 클래스로 구현한다. <br/>
> 데이터 필드 : 데이터 값 <br/>
> 링크 필드 : 주소 값 (idx) <br/>

<br/>

### 순차리스트 (인접리스트)
> 데이터의 순서와 같게 메모리에 저장이 된다. <br/>
> 논리적 순서와 같게 물리적인 위치도 정해진다. <br/>
> 물리적 순서와 논리적 순서가 같다.
> <br/>
> 
> #### 순차 자료구조의 문제점
>     삽입 연산이나 삭제 연산 후에 연속적인 무리 주소를 유지하기 위해 원소들을 이동시키는 추가적인 작업이나 시간이 소요된다.
>     -> 성능 저하로 직결된다.
<br/>

### 연결 리스트
> 자료의 논리적 순서와 물리적 순서가 일치하지 않는 구조 <br/>
> 각 원소에 저장되어 있는 다음 원소의 주소값에 의해 순서가 연결된다. <br/>
> 따라서 물리적인 순서를 맞출 필요가 없다. <br/>
> 여러개의 작은 공간들을 연결하여 전체의 구조를 표현한다. <br/>
> 
> #### 종류 
> 단순연결리스트, 원형연결리스트, 이중연결리스트 .... <br/>
> 
> #### 장단점
> * 장점 : 필요시에만 메모리를 사용하기 때문에, 메모리 누수가 발생하지 않는다.
>   <br/> 삽입, 수정 삭제 등에 용이하다.
> * 단점 : 구현이 어렵다.
> 
> #### 연결리스트의 노드
> 데이터필드 : 데이터 값 <br/>
> 링크 필드 : next (다음 노드의 주소를 저장) <br>
> 
> #### 연결리스트의 구조
> head -> 0번노드 -> 1번노드