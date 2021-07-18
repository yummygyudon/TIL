# 컬렉션 관리 함수



### enumerate

> 순서값을 부여하여 순서값과 요소값 둘을 한꺼번에 구해 주는 내장 함수

- 순서값과 요소값을 **튜플(Tuple)**로 묶은 컬렉션 리턴

  - 순서대로 읽는 것은 for 반복문이 가장 편리하지만 순서값을 알 수 없음

  ```python
  score = [ 88, 95, 70, 100, 99 ]
  for s in score : 
      print("성적 : ", s)
      
  성적 : 88 
  성적 : 95
  성적 : 70
  성적 : 100
  성적 : 99
  ```

- 순서값은 0부터 시작하기 때문에 enumerate의 두 번째 함수에 **시작값** 지정

```python
score = [ 88, 95, 70, 100, 99 ]
for no, s in enumerate(score, 1):
    print(str(no) + "번 학생의 성적 :", s)
    
1번 학생의 성적 : 88
2번 학생의 성적 : 95
3번 학생의 성적 : 70
4번 학생의 성적 : 100
5번 학생의 성적 : 99
```



```python
#포맷팅 활용
names = "둘리,고길동,희동이,마이콜,또치,도우너"	#긴 문자열
namelist = names.split(",")	# 쉼표 기준으로 단어 분할
namelist.sort()	#이름 정렬

for num, name in enumerate(namelist) :
    print(f"이름순으로 {name}는 {num+1}번입니다.")
    
이름순으로 고길동는 1번입니다.
이름순으로 도우너는 2번입니다.
이름순으로 둘리는 3번입니다.
이름순으로 또치는 4번입니다.
이름순으로 마이콜는 5번입니다.
이름순으로 희동이는 6번입니다.

for data in enumerate(namelist) :
    print(f"enumerate를 적용한 결과 : {data}")	#두 값이 짝을 이룬 구조이기때문에 튜플 형태 호출
    
enumerate를 적용한 결과 : (0, '고길동')	#시작값은 0이기 때문에
enumerate를 적용한 결과 : (1, '도우너')
enumerate를 적용한 결과 : (2, '둘리')
enumerate를 적용한 결과 : (3, '또치')
enumerate를 적용한 결과 : (4, '마이콜')
enumerate를 적용한 결과 : (5, '희동이')
    
for num, name in enumerate(namelist, 100) :		#시작값 지정
    print(f"이름순으로 {name}는 {num}번입니다.")
    
이름순으로 고길동는 100번입니다.
이름순으로 도우너는 101번입니다.
이름순으로 둘리는 102번입니다.
이름순으로 또치는 103번입니다.
이름순으로 마이콜는 104번입니다.
이름순으로 희동이는 105번입니다.
```



### zip

> 여러 개의 컬렉션을 합쳐 하나로 만드는 함수
>
> 대응되는 요소끼리 짝을 지어 **튜플**의 리스트 생성

- *1회성 함수*이기 때문에 한 번 묶어서 사용하면 재사용을 위해선 다시 변수에 선언
  - zip 결과변수를 print하면 메모리 주소 출력

```python
yoil = ["월", "화", "수", "목","금", "토", "일"]
food = ["갈비탕", "순대국", "칼국수", "삼겹살"]
menu = zip(yoil, food)	#어떤 리스트의 값이 어느 위치에 출력될 것인지 지정

print(menu, type(menu))
<zip object at 0x0000025116044F80> <class 'zip'>
#zip되어 메모리에 저장됨

for y, f in menu:
    print("%s요일 메뉴 : %s" % (y, f))

월요일 메뉴 : 갈비탕
화요일 메뉴 : 순대국
수요일 메뉴 : 칼국수
목요일 메뉴 : 삼겹살
```



- 합쳐지는 두 리스트는 **길이가 달라도** 상관없음
  - 긴 쪽의 남는 요소는 사용하지 않음



- zip함수가 생성하는 튜플을 **dict함수**로 변환 가능
  - 앞 요소 : **Key** / 뒤 요소 : **Value**

```python
menu = zip(yoil, food)
d2 = dict(menu)
for y, f in d2.items():
    print("%s요일 메뉴 : %s" % (y, f))
    
월요일 메뉴 : 갈비탕
화요일 메뉴 : 순대국
수요일 메뉴 : 칼국수
목요일 메뉴 : 삼겹살
    
print(d2)
{'월': '갈비탕', '화': '순대국', '수': '칼국수', '목': '삼겹살'}
```



#### enumerate & zip 활용

```python
numList = [0, 1, 2]
engList = ['zero', 'one', 'two']
espList = ['cero', 'uno', 'dos']
print(list(zip(numList, engList, espList)))
[(0, 'zero', 'cero'), (1, 'one', 'uno'), (2, 'two', 'dos')]

for num, eng, esp in zip(numList, engList, espList):
    print(f'{num} is {eng} in English and {esp} in Spanish.')

0 is zero in English and cero in Spanish.
1 is one in English and uno in Spanish.
2 is two in English and dos in Spanish.


upperCase = ['A', 'B', 'C', 'D', 'E', 'F']
lowerCase = ['a', 'b', 'c', 'd', 'e', 'f']

for i, (upper, lower) in enumerate(zip(upperCase, lowerCase), 1):	#zip 형태 맞추어 튜플을 for문 인수로 지정
    print(f'{i}: {upper} and {lower}.')

1: A and a.
2: B and b.
3: C and c.
4: D and d.
5: E and e.
6: F and f.
```



### any / all

#### any

> 리스트를 순회하며 **참**인 요소가 **하나라도** 있는지 조사



#### all

> 리스트를 순회하며 **모든 요소** 가 **참인지** 조사



### filter

> 리스트 요소 중 조건에 맞는 것만 골라내는 함수

- Bool(True / False) 기준으로 분류
- **사용자 지정 def 함수**도 조건으로 사용 가능
  - 단 조건으로 지정할 때, **함수명**만 기재 ( filter ( sumall**( )**, [리스트명] ) 불가능 )

```python
def flunk(s):
    return s < 80

score = [ 45, 89, 72, 53, 94 ]
for s in filter(flunk, score):
    print(s)

45
72
53
```



### map

> 모든 요소에 대해 **변환 함수**(return) 를 호출하여 새 요소값으로 구성된 리스트 생성

```python
def half(s):
    return s / 2

score = [ 45, 89, 72, 53, 94 ]
for s in map(half, score):
    print(s)
    
22.5 
44.5 
36.0 
26.5 
47.0
```



- 두 개 이상의 리스트를 받아 각 리스트의 요소를 조합할 수도 있음

```python
def total(s, b):
    return s + b

score = [ 45, 89, 72, 53, 94 ]
bonus = [ 2, 3, 0, 0, 5 ]
for s in map(total, score, bonus):
    print(s)
    
47
92
72
53
99
```





## Lambda 람다 함수

> 함수명을 정의 안하고도 특정 연산식을 작성하여 입력과 출력만으로 결과값 도출하는 함수

- 구조

**lambda 인수(Arguments) : 식(Expression)**

- 식으로 다양한 연산식 구현 가능 (비교연산 / 산술연산 등)



- 함수명을 작성하지 않는 경우, *무명 함수*이기 때문에 **1회성**으로만 사용한다

```python
#위 filter함수 예제
def flunk(s):
    return s < 80

score = [ 45, 89, 72, 53, 94 ]
for s in filter(flunk, score):
    print(s)

#Lambda 변환
score = [ 45, 89, 72, 53, 94 ]
for s in filter(lambda x : x < 80, score)
	print(s)

45
72
53
```



```python
#위 map 함수 예제
def half(s):
    return s / 2

score = [ 45, 89, 72, 53, 94 ]
for s in map(half, score):
    print(s)
    
#Lambda 변환
score = [ 45, 89, 72, 53, 94 ]
for s in map(lambda x : x / 2, score)
	print(s)
    
22.5 
44.5 
36.0 
26.5 
47.0
```



- **변수 에 lambda 함수** 선언 가능

````python
func1 = lambda n1, n2 : n1 + n2

print(func1(10, 20))
30

result = func1(100, 200)
print(result)
300
======================================================
func2 = lambda s: len(s)

print(func2('simple'))
6
======================================================
func3 = lambda : print("no argument, no return")	#인수 없이 콜론 이후 단순 작업 명령
func3()
no argument, no return
======================================================
func4 = lambda p1, p2, p3 : print(p1, p2, p3)		#위치인수 지정
print(func4(10, 20, 30))

10 20 30
None
======================================================
func5 = lambda *p : print(sum(p))					#가변 인수 지정
func5(1,2,3,4,5)
func5(11,22)

15
33
````



- **함수 리턴값에 Lambda 함수**

```python
def calc():
    num  = 100
    return lambda : num + 1    # 람다 표현식을 반환

c1 = calc()

print(c1(), c1(), c1())
101 101 101

===========================================================

def calc():
    a = 3
    b = 5
    return lambda x: a * x + b    # 람다 표현식을 반환

c2 = calc()

print(c2(1), c2(2), c2(3), c2(4), c2(5))
8 11 14 17 20
```





## Collection Copy

 기본형 변수는 서로 독립적이여서 대입 하면 일시적으로 값이 같아질 뿐

이후 둘 중 하나를 바꾸어도 다른 변수에는 영향 없음

```python
a = 3
b = a		#b에 a의 값인 3 대입
print("a = %d, b = %d" % (a, b))
a= 3, b = 3	#b는 이제 값이 3인 독립적 변수

a = 5

print("a = %d, b = %d" % (a, b))
a =5, b = 3
```



**하지만 Collection의 경우는 다름**

list의 경우 대입이 된 경우,

같은 메모리에 **공유**하고 있는 형태를 가짐

따라서 한 리스트의 값에 변동이 생기면 동일하게 대입된 리스트에도 반영이 됨

```python
list1 = [ 1, 2, 3 ]
list2 = list1
print(list1)
print(list2)
[1, 2, 3]
[1, 2, 3]


list2[1] = 100
print(list1)
print(list2)
[1, 100, 3]
[1, 100, 3]


print(id(list1),id(list2))
2336854184448 2336854184448 #같은 메모리주소를 가지는 것을 볼 수 있음
```



두 개 이상의Collection을 **독립적인 사본**으로 만들기 위해서는 **Copy 메서드**를 통해 복사본 생성해야함.

- copy메서드를 대신하여 `[:]`를 통해서도 동일한 결과
  - [:]는 전 범위를 의미하여 처음부터 끝까지 추출한 후 새로운 리스트를 만들기 때문에 독립적

```python
list1 = [ 1, 2, 3 ]
list2 = list1.copy()
#list2 = list1[:] 과 동일


list2[1] = 100
print(list1)
print(list2)
[1, 2, 3]
[1, 100, 3]

print(id(list1),id(list2))
2336854461696 2336854461632	#다른 메모리 공간에 독립적인 리스트들
```



하지만 위와 같이 copy메서드는  *얕은 복사*를 행하기 때문에 **중첩 리스트**는 사본을 뜨지 못함

```python
list0 = [ 'a', 'b' ]
list1 = [ list0, 1, 2 ]
list2 = list1.copy()

list2[0][1] = 'c'

print(list1)
print(list2)
[['a', 'c'], 1, 2]	#list1의 값까지 변한 것을 볼 수 있음
[['a', 'c'], 1, 2]
```



- **중첩 Collection** 복사 = **deepcopy**메서드

```python
list0 = [ "a", "b" ]
list1 = [ list0, 1, 2 ]
list2 = copy.deepcopy(list1)

list2[0][1] = "c"

print(list1)
print(list2)
[['a', 'b'], 1, 2]
[['a', 'c'], 1, 2]
```



### is 연산자

**`==`비교와는 다름*

- 값이 아닌 **객체** 기준으로 비교하는 방법

```python
list1 = [ 1, 2, 3 ]
list2 = list1
list3 = list1.copy()

print("1 == 2" , list1 is list2)	#같은 메모리주소를 공유하고 있기때문에_True
1 == 2 True

print("1 == 3" , list1 is list3)	#copy를 했기때문에 서로 독립적인 객체_False
1 == 3 False

print("2 == 3" , list2 is list3)
2 == 3 False

#정수형 변수 또한 동일
a = 1
b = a
print("a =", a, " b =", b, ":", a is b)
a = 1  b = 1 : True
    
b = 2

print("a =", a, " b =", b, ":", a is b)
a = 1  b = 2 : False
```



**★하지만 반전이 있다★**

```python
a = 10
b = 10	#변수 대입이 아닌 같은 값을 새로운 변수에 대입

print(a == b)
True

print(a is b)	#분명 다른 변수이지만 True가 나온다
True
```



 Python 내에서는

**-5 부터 256까지의 값**은 자체적으로 *<u>특정 메모리 주소</u>*에 저장되어

위 범위의 정수 중 하나를 서로 다른 이름의 변수에 대입을 하여도

서로 메모리 주소는 미리 Python 내부 특정 메모리 주소로 연결되어 **같은 메모리에 연결**된다.

