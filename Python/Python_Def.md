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

```python
def func1(p1, p2, p3, p4) :
    global a, b, d
    a = p1
    b = p2
    c = p3
    d = p4
    print('[지역] a=', a, ' b=', b, ' c=', c, ' d=', d, sep='', end='\n\n')

a = 10
b = 20
c = 30
print('[전역(함수호출전)] a=', a, ' b=', b, ' c=', c, sep='', end='\n\n')
func1('A', 'B', 'C', 'D')
print('[전역(함수호출후)] a=', a, ' b=', b, ' c=', c, ' d=', d, sep='', end='\n\n')            #함수에선 global을 a,b,d만 선언했기때문에 c는 30 유지
```





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
  - 뒤의 **'나머지'**를 모두 취급한다는 의미

```python
def Func(name, * names) : 
    print(name)		#가인수 : "홍길동" 출력
    print(names)	#가변인수 "('이순신', '유관순')" 출력
    
Func("홍길동", "이순신", "유관순")
```




```python
def sumall(*p) :
    sum = 0
    for data in p :
        sum += data
    return sum

print(sumall(1,2,3,4,5))
15
print(sumall(100, 200, 300))
600
```

```python
<변수명>(a, *args)		#가능
<변수명>(*args, a)		#Error
<변수명>(*a, *args)	#Error
```

```python
def printdeco(*p, deco="@") : #지정 인수는 기본값
    for data in p :
        print(deco, data, deco)
    print()

printdeco("가", "나")
@ 가 @
@ 나 @

printdeco(True, "A", 10, deco="$")
$ True $
$ A $
$ 10 $
```



## 키워드 인수

> 인수 이름을 지정하여 전달

- 앞쪽에 키워드 인수 ▶ 뒤쪽엔 위치 인수 불가



- 정의 위치에 따라 매개변수에 전달됨
- 실인수 앞에 매개변수 지정하면 위치 관계없이 전달 가능


```python
def normalfn(p1, p2, p3) :		#기본값 지정이없음
    print(p1)
    print(p2)
    print(p3)

#포지션 Argument
normalfn(10,20)
# 오류 : 기본값 지정 없기때문에 인수 맞춰야함
normalfn(p3=10,p1=20,p2=30)
20
30
10

#키워드 Argument
normalfn(p1=10, p3=40, p2=20)
10
20
40					#기본값이 지정되었기때문에 40이 나옴
```



- 기본값이 지정되어 있으면 실인수가 없을 때, 기본값 출력

```python
#디폴트(default)_ 기본값 Argument
def defaultfn1(p1=10, p2="abc", p3=True) :
    print(p1)
    print(p2)
    print(p3)
    
defaultfn1()
10
abc
True

defaultfn1(10,20,30)
10
20
30

defaultfn1("abc", "xyz")
abc
xyz
True

defaultfn1(p2="가", p1="xyz", p3="P")
xyz
가
P

```




- 구조 설정 및 데이터 삽입

```python
def getlist1(times, *nums) :
    newnums = []						#새로운 출력값 리스트 구조 설정 / len() 가능
    for data in nums :
        newnums.append(data * times)	#기존 값 * *nums 요소들 각각 곱해서
    return newnums						#새로 만든 리스트형 변수에 삽입

print(getlist1(2, 1,2,3,4,5))			#times =2 , *nums = 나머지 수
[2, 4, 6, 8, 10]

print(getlist1(3, 1,2,3,4,5,6,7))
[3, 6, 9, 12, 15, 18, 21]
```



## 키워드 가변 인수

- **'* *'기호**를 인수 목록에 붙여서 가변 개수 전달
  - Dictionary 형식으로 전달됨( {키(워드) : Value} )
  - (a= ..., b=..., c=..., .....) 키워드 할당 값들을 제한없이 적을 수 있음
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

- 함수 선정시의 **매개변수명** 을 **키워드**로 사용

```python
def calcstrp(**args) :			#모든 인수들(위치는 언제든 바뀔 수 있다고 선언)
    begin = args['begin']		#변수명 자체에 이름에 해당하는 구성값들을
    end = args['end']			#따로 모아놓는 설정
    step = args['step']			#Dict 키값을 불러 해당 키워드로 저장된 Value 호출
    
    sum = 0
    for num in range(begin, end, step) :
        sum += num
    return sum

print("2 ~ 5 = ", calcstep(begin = 2, end = 5, step = 1))
print("2 ~ 5 = ", calcstep(step = , end = 5, begin = 1))	#순서 바꿔서 키워드 입력해도 됨
```



```python
def calcscore(name, *score, **option):	
    print(name)
    sum = 0
    for s in score:
        sum += s
    print("총점 :", sum)	
    if (option['avg'] == True ):			#**option 중 'avg'키 value값 유효하면
        print("평균 :", sum / len(score))

calcscore("김상형", 88, 99, 77, avg = True)
calcscore("김한슬", 99, 98, 95, 89, avg = False)
김상형
총점 : 264
평균 : 88.0
김한슬
총점 : 381
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





## 실습

```
[ 실습 1 ]
<구현해야 하는 함수 사양>
   함수명 : print_book_title
   매개변수 : 없음
   리턴값 : 없음
   기능 : 파이썬 교재명을 화면에 출력
   함수명 : print_book_publisher
   매개변수 : 없음
   리턴값 : 없음
   기능 : 파이썬 교재의 출판사명을 화면에 출력
- print_book_title() 함수를 3회 호출하고 
	print_book_publisher() 함수를 5회 호출한다.


[ 실습 2 ]
<구현해야 하는 함수 사양>
   함수명 : get_book_title
   매개변수 : 없음
   리턴값 : 있음
   기능 : 파이썬 교재명을 리턴한다.
   함수명 : get_book_publisher
   매개변수 : 없음
   리턴값 : 있음
   기능 : 파이썬 교재의 출판사명을 리턴한다.
- get_book_title() 함수를 호출하고 리턴되는 결과를 name 변수에 저장한 다음
												name 변수의 값을 2회 출력한다. 
	get_book_publisher() 함수를  호출하고 리턴되는 결과를 화면에 출력한다.


[ 실습 3 ]
1. 파일명 : funcLab3.py
2. 구현해야 하는 함수 사양
   함수명 : expr
   매개변수 : 숫자 2개와 연산자 1개
   리턴값 : 연산 결과 또는  None
   기능 : 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
            연산자는 +, -, *, / 만 처리하며 그 외의 연산자는 연산을 하지 않고 None 을 리턴한다.
3. 숫자 2개와 연산자 1개를 전달하여 expr() 이라는 함수를 호출한 다음 리턴 결과가 None 이면
   수행 불가 를 출력하고 그렇지 않으면 연산결과 : XX 를 출력한다.


[ 실습 4 ]
<구현해야 하는 함수 사양>
   함수명 : print_triangle
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         2 전달시
         *
         * *
         5 전달시
         *
         **
         ***
         ****
         *****
         전달되는 아규먼트 값은 1~10으로 제한한다. 
         1~10 이외의 값이 전달된 경우에는 처리하지 않고 그냥 리턴한다.

- 숫자를 다양하게 지정해서 print_triangle() 함수를 호출해 본다.


[ 실습 5 ]
<구현해야 하는 함수 사양>
   함수명 : print_triangle
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         2 전달시
         @@
         @ 
         5 전달시
         @@@@@
         @@@@
         @@@
         @@
         @
         전달되는 아규먼트 값은 1~10으로 제한한다.
         1~10 이외의 값이 전달된 경우에는 처리하지 않는다.

- 숫자를 다양하게 지정해서 print_triangle() 함수를 호출해 본다.


[ 실습 6 ]
<구현해야 하는 함수 사양>
   함수명 : print_gugudan
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자의 구구단을 출력한다.
         - 전달된 아규먼트가 int 타입인지 채크하고 int 타입이 아니면 그냥 리턴한다.
         - 전달된 아규먼트가 1~9 사이인지 채크하고 아니면 그냥 리턴한다.
         - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.\\
- 숫자를 다양하게 지정해서 print_ gugudan() 함수를 호출해 본다.


[ 실습 7 ]
<구현해야 하는 함수 사양>
   함수명 : differtwovalue

   매개변수 :  2개
   리턴값 : 연산 결과
   기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴 두 값이 동일하면 0 을 리턴한다.
           10, 20 이 전달되면 ---> 10 리턴
           20, 5 가 전달되면 ---> 15 리턴
           5, 30 이 전달되면 ---> 25 리턴
           6, 3 이 전달되면  ---> 3 리턴

- 1부터 30 사이의 난수 2 개를 추출하여 2번에서 구현된 함수를 호출하고 
	결과를 다음 형식으로 출력한다.
   
   "X 와 Y 의 차는 W 입니다."
  (----> 5 회 반복)
  
  
[ 실습 8 ]
<구현해야 하는 함수 사양>
   함수명 : print_triangle_withdeco
   매개변수 : 2개
            숫자와 데코문자 
            여기에서 데코문자는 기본값을 갖는다. 기본값은 ‘%’로 정한다.
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         숫자 2 만 전달시
          	 %
         	%%
         숫자 5 와 데코문자 ‘*’ 전달시
             *
            **
           ***
          ****
         *****
        전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는 
        처리하지 않는다.
        
- 숫자를 다양하게 지정해서 print_triangle_withdeco () 함수를 호출해 본다.


[ 실습 9 ]
<구현해야 하는 함수 사양>
   함수명 : sumEven1
   매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
         아규먼트는 "1 이상의 숫자만" 온다고 정한다.
         전달된 아규먼트들에서 "짝수에 해당하는 숫자들만 합을 계산"해서 리턴한다.
         전달된 아규먼트들 중에 "짝수가 없으면 0을 리턴"한다.
         아규먼트가 "전달되지 않으면 -1"을 리턴한다.
  
- 숫자를 다양하게 지정해서 sumEven1() 함수를 호출해 본다.


[ 실습 10 ]
<구현해야 하는 함수 사양>
   함수명 : sumAll
   매개변수 : 가변형(전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 : 아규먼트가 몇 개가 전달되든 처리해야 한다.
         호출시 전달되는 아규먼트의 데이터 타입에는 제한이 없다.
         그러므로 전달된 아규먼트의 타입을 채크하여 숫자만 처리하고
         숫자가 아닌 데이터는 무시한다.
         아규먼트가 전달되지 않았거나 전달되었다 하더라도
         숫자가 없으면 None 을 리턴한다.
  
- 숫자를 다양하게 지정해서 sumAll() 함수를 호출해 본다.


[ 실습 1 ]
<구현해야 하는 함수 사양>
   함수명 : mydict
   매개변수 : 가변 키워드형(키=값 형식으로 전달받을 수 있는 아규먼트 개수에 제한이 없다.)
   리턴값 : 1개
   기능 :  아규먼트는 키=값 형식으로 전달되며 몇 개가 전달되든 처리해야 한다.
             아규먼트가 한 개도 전달되지 않으면 비어있는 딕셔너리를 리턴한다.
 	 비어있는 딕셔너리를 생성한 다음 아규먼트로 전달된 키=값 쌍을 저장하는데  
키는 앞에 my 를  붙여서 저장한다.
              생성된 딕셔너리를 리턴한다.
  
3. 다양한 구성으로 키워드 아규먼트를 전달하면서 mydic() 함수를 호출하고 리턴 결과를 
   화면에 출력한다.


[ 실습 12 ]
1. 파일명 : funcLab12.py
2. 구현해야 하는 함수 사양
   함수명 : myprint
   매개변수 : 가변 아규먼트1개, 가변 키워드 아규먼트 1개
   리턴값 : 없음
   기능 : 전달되는 아규먼트의 개수에는 제한이 없다.
         호출시 전달되는 아규먼트의 데이터 타입에도 제한이 없다. 
         아규먼트가 전달되지 않으면 “Hello Python”을 출력한다.
         출력 형식은 다음에 제시된 실행 결과 예시를 보고 처리하는데 한 번의 print() 함수로 처리한다.	
 
 	 myprint(10, 20, 30, deco="@", sep="-")  호출시
     		
     	▶	@10-20-30@ 출력
     		
	myprint("python", "javascript", "R", deco="$")  호출시
     		
     	▶	$python,javascript,R$ 출력
     		
	myprint("가", "나", "다")  호출시
	
     	▶	**가,나,다** 출력
     		
	myprint(100)  호출시
     		
     	▶	**100** 출력
     		
	myprint(True, 111, False, "abc", deco="&", sep="")  호출시
     		
     	▶	&True111Falseabc& 출력

3. 위에 제시된 호출식들을 가지고 호출했을 때 위와 같은 결과가 출력되면 완성이다.
```





 



### 풀이

```python
#[실습1]
def print_book_title() :
    return "파이썬 정복"

def print_book_publisher() :
    return "한빛 미디어"

for _ in range(3)
	print(print_book_title())

for _ in range(5)
	print(print_book_publisher())
    
```



```python
#[실습2]
def get_book_title() :
    return "파이썬 정복"

def get_book_publisher() :
    return"힌빛미디어"

name = get_book_title()

for _ in range(2) :
    print(name)

print(get_book_publisher())
```

```python
#[실습3]
#풀이 1
def expr(num1, num2, cal) :
    if cal == "+" :
        return num1 + num2
    elif cal == "-" :
        return num1 - num2
    elif cal == "*" :
        return num1 * num2
    elif cal == "/" :
        return num1 / num2
    else :
        return None

#풀이 2
def expr(num1, num2, cal) :
    z = None
    if cal == "+" :
        z = num1 + num2
    elif cal == "-" :
        z = num1 - num2
    elif cal == "*" :
        z = num1 * num2
    elif cal == "/" :
        z = num1 / num2
    return z

#풀이 3
def expr(num1, num2, cal) :
    if cal == "+" :
        z = num1 + num2
        return z
    elif cal == "-" :
        z = num1 - num2
        return z
    elif cal == "*" :
        z = num1 * num2
        return z
    elif cal == "/" :
        z= num1 / num2
        return z
    else :
        return


expr = expr(6,2,"**")

#풀이 1 출력명령
if expr == None :
    print("수행 불가")
else :
    print("연산결과 : ", expr)

#풀이 2
if expr is None : 
    print("수행 불가")
else:
    print("연산결과 : ", expr)

```



```python
#[실습4]
def print_triangle(a) :
    if a > 10 :
        return
    for i in range(1,a+1) :
        print("*" * i)
        
print_triangle(13)
```



```python
#[실습5]
def print_triangle(a) :
    if a > 10 or a < 1 :
        return
    for i in range(a, 0, -1):
        print("@" * i)


print_triangle(8)
```



```python
#[실습6]
def print_gugudan(dan) :
    if dan != int(dan) :        # type(dan) != int :
        return
    elif dan < 1 or dan >= 10 :
        return
    else :
        for num in range(1,10) :
            print(dan, "*", num, "=", dan * num)
            
print_gugudan(8)
```



```python
#[실습7]
def differtwovalue(num1, num2) :
    if num1 == num2 :
        return 0
    else :
        z = abs(num1 - num2)
        return z

import random


for i in range(5) :
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    differtwovalue(a, b)
    print(a, "와 ", b, "의 차는 ", differtwovalue(a, b), " 입니다.")
```



```python
#[실습8]
def print_triangle_withdeco(num, deco = '%') :
    if num > 10 or num < 1 :
        return
    for i in range(1,num+1) :
        print(' ' * (10-i),end='')		#공백 부여
        print(deco * i)
```



```python
#[실습9]
def sumEven1(*nums) :
    even_sum = 0
    if len(nums) >= 2 :
        for i in nums :
            if i % 2 == 0:
                even_sum += i       #홀수는 저절로 합이 0 & 홀수는 계산 포함 안됨
        return even_sum
    else :
        return -1
```



```python
#[실습10]
def sumAll(*nums):
    sum = 0
    for i in nums :
        if type(i) == int:
            sum += i
    if sum == 0 :       # 인수에 0만 들어있어도 int이긴 하지만 "sum이 0"이기때문에 None처리 됨.
        return None     #숫자가 아닌 데이터 들은 int가 아니여서 계산 안됐기 때문에 sum은 당연히 0이 되어서
    return sum

```



```python
#[실습11]
def mydict(**args) :
    myargs = {}
    for k, v in args.items():
        myargs["my" + k] = v    # myargs에 for문으로 "my"만 삽입
    return myargs    #def와 라인을 맞추어서 인수 없을 때 빈 딕셔너리 반환

print(mydict(name = "정동규", age = 23, height = 170))
print(mydict(name = "정동규", age = 23))
print(mydict())


```





```python
#[실습12]
#풀이 1
def myprint (*p, deco="**",sep=",") :
    if p is None :
        print("Hello Python")
    else :
        print(deco, end="")
        print(*p, sep=sep, end="")
        print(deco)
        
        
#풀이 2
def myprint (*str_tuple, **str_dict) :
    if len(str_tuple) == 0 :        #키워드 가변인수가 얼마나 와도 tuple값 없으면 어차피 출력 안되니까
        print("Hello Python")
        return
    str_list = [ n for n in str_tuple]      #list에 str_tuple값 삽입
    str_list[0] = str_dict.get("deco", "**") + str(str_list[0]) #list 첫번째 값 자체에 deco가 붙게끔 / .get()메서드는 첫번째 인수에 키워드명, 두번째 인수는 입력된 키워드가 없을 경우 갖게끔 할 데이터
    str_list[-1] = str(str_list[-1]) + str_dict.get("deco", "**")
    print(*str_list, sep=str_dict.get("sep", ","))  #list 언패킹 & get()메서드



```

