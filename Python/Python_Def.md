# 함수_Def

> 일련의 코드 블록에 이름을 붙여 정의

> "호출문"으로 실행

- **소문자**로 입력

```python
#선언
def <함수이름>(인수 목록) :		#띄어쓰기 : '_'(Under bar)사용
    """(Docstring)"""
    [수행문 1]
    [수행문 2]
    return <반환값>
```

- **Docstring**(설명문)
  - 실행에는 영향 없음
  - 선언문-수행문 사이에 작성하는 문자열



```python
#중간에 IF~ elif 활용
def coffee_machine(button) :
     print()
     print("#1. (자동으로) 뜨거운 물을 준비한다.");
     print("#2. (자동으로) 종이컵을 준비한다.");

     if button == 1 :
          print("#3. (자동으로) 보통커피를 탄다.")
     elif button == 2 :
          print("#3. (자동으로) 설탕커피를 탄다.")
     elif button == 3 :
          print("#3. (자동으로) 블랙커피를 탄다.")
     else :
          print("#3. (자동으로) 아무거나 탄다.\n")

     print("#4. (자동으로) 물을 붓는다.");
     print("#5. (자동으로) 스푼으로 젓는다.");
     print()

coffee = int(input("A손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("A손님~ 커피 여기 있습니다.")

coffee = int(input("B손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("B손님~ 커피 여기 있습니다.")

coffee = int(input("C손님, 어떤 커피 드릴까요?(1:보통, 2:설탕, 3:블랙)"))
coffee_machine(coffee)
print("C손님~ 커피 여기 있습니다.")


#타입(Type) 함수 활용
def isType(p) :
    if type(p) == int :
        result = "정수를 전달했네요"
    elif type(p) == float :
        result = "실수를 전달했네요"
    elif type(p) == str :
        result = "문자열을 전달했네요"
    elif type(p) == bool :
        result = "논리값을 전달했네요"
    else :
        result = "I don't know"
    return result
```



- 재귀함수 (reculsive function)

```python
def Func(a):
    z=0						
    n = a
    z += n
    print('5! = ', z)		
    if n = 0
        exit()
    z = 함수1(n-1)		#숫자가 1씩 감소시킨 값 구함 → 팩토리얼 구성 출력
    return z


```





### 전역 변수(Global Variable)

> 함수 바깥에 선언

- 어디에서나 참조 가능
  - 주의_ 초기화하는 장소에 따라 변수의 범위가 결점됨
  - 내부에서 전역 변수 대입하여 초기화 → '새로운 지역 변수' 생성됨





### 지역 변수(Local Variable)

> 함수 내부에서 선언

- 함수 내부에서만 사용되고 밖으로는 사용 불가





### Pass 명령

- 그냥 무시하고 건너뛰기
  - 만들다 만 함수가 있을 때 사용하기도 함(밑에 실행할 것들이 있을 때 그냥 넘기도록)

*# continue는 '반복문'에서만 사용하는 것*



### Return 값

- 실해 결과를 호출원으로 돌려주는 값
- 무조건 있어야 하는 요소는 아님
  - No 리턴값 ▶ 자동 **None** 리턴





## 인수

- 매개변수를 통해서 전달받음
  - 형식 인수 = 함수 **정의문 인수** (**매개변수**)
  - 실인수 = 함수 호출문서 **전달하는 인수** (**Argument**)

- 값이 매개변수에 **순서대로** 전달됨.(일반적으로 많으 쓰임_위치 인수[positional argrment])



## 가변 인수

> 고정되지 않은 임의 개수의 인수를 받음

- **' * '기호**를 인수 이름 앞에
- 인수 목록의 **마지막**에 와야함

```python
def Func(name, * names) : 
    print(name)		#가인수 : "홍길동" 출력
    print(names)	#가변인수 "('이순신', '유관순')" 출력
    
Func("홍길동", "이순신", "유관순")
```




```python
def intsum(*ints) :
    sum = 0
    for num in ints :
        sum += num
    return
```

```python
<변수명>(a, *args)		#가능
<변수명>(*args, a)		#Error
<변수명>(*a, *args)	#Error
```



## 키워드 인수

> 인수 이름을 지정하여 전달

- 앞쪽에 키워드 인수 ▶ 뒤쪽엔 위치 인수 불가

```python
def calcstep(begin, end, step) :
    sum = 0
    for num in range(begin, end + 1, step) :
        sum += num
    return sum

print("2 ~ 5 = ", calcstep(begin = 2, end = 5, step = 1))
print("2 ~ 5 = ", calcstep(begin = 2, end = 5, step = 1))
```



## 키워드 가변 인수

- **'* *'기호**를 인수 목록에 붙여서 가변 개수 전달
- 위치 인수 & 키워드 인수 **동시**에 가변으로 취할 수 있음

```python
def emp_func(name, age, **other):
    print(name)
    print()
    print(age)
    print()
    print(other)  # {'addre': '서울시', 'height': 175, 'weight': 65}


emp_func('홍길동', 35, addre='서울시', height=175, weight=65)

#홍길동
#
#35
#
#{'addre': '서울시', 'height': 175, 'weight': 65}
```



```python
def calcstrp(**args) :			#모든 인수들(위치는 언제든 바뀔 수 있다고 선언)
    begin = args['begin']		#변수명 자체에 이름에 해당하는 구성값들을
    end = args['end']			#따로 모아놓는 설정
    step = args['step']
    
    sum = 0
    for num in range(begin, end, step) :
        sum += num
    return sum

print("2 ~ 5 = ", calcstep(begin = 2, end = 5, step = 1))
print("2 ~ 5 = ", calcstep(step = , end = 5, begin = 1))	#순서 바꿔서 키워드 입력해도 됨
```





## 특수 함수

- Lambda : 축약함수

```python
#형식
<변수> = (lambda [인수] : [리턴값])(<실인수>).<명령>
```



```python
def func(x, y) : 
    z = x + y
    return z

#서로 동일

lambda x, y : z= x + y
```



- Pandas : 데이터 추출, 병합, 가공 등에 유용한 패키지
- Numpy : 행렬 취급 시 유용한 패키지
- Matplotlib, Seaborn : 그래프 패키지



## 내장 함수(Built-in)

> 파이썬 시스템 내부 안의 사전 정의되어있는 함수

**enumerate() : 스스로 내부 요소들을 세며 순서대로 숫자를 매김*

**upper(문자/문자열) : 대문자로 바꾸기*

**split(문자열,sep=) : 구분자 기준으로 문자열 내 각 단어들 나누기*

