# 반복문_For

## For 반복문

> 컬렉션(Collection)_(Range / Tuple / List 등) 요소 순서대로 반복하면서 루프 명령 실행

> "Range() 함수에서 결정 후", 그 휫수만큼 반복 (While문과의 차이)



*#범위 요소 각자의 계산 값 출력 ▶ 개행되어 출력됨(→ end = '' 로 붙여줄 수 있음)*

```python
for n in range(3) :    #n 대신 _ 써도 됨
    print("PYTHON")
    
PYTHON
PYTHON
PYTHON

##구구단 
import random
dan = random.randint(1,9)
print(dan, "단")
for num in range(2, 10):    #시작값 1로 주면 *1 부터 시작
    print(dan, "*", num, "=", dan * num, end="\t")  # \t는 탭 기준 간격

```



- <누적합> 명령

```python
# 누적합 명령
<변수명> = 0 선언
for i range()
	..........
	<변수명> = <변수명> + i
(or)i += 1
```



- [IF 문] 활용

```python
## IF문 활용
for x in range(1, 51) : 
    if x % 10 == 0 :
        print('+', end = '')
    else : 
        print('-', end = '')

---------+--- .....

# While문 ver        
x=1
while x <= 50 :
    if x % 10 :
        print('-', end = '')
    else : 
        print ('+', end = '')
    x += 1
```



- Range (범위) 의 원칙

  ```python
  range([start,] end[, step])
  # start : 시작값 _ 지정되지 않으면 0부터 시작
  # end : 끝 값 _ 0부터 시작이기 때문에 'end+1'로 지정
  # step : 증가값 _ 음수 : 역으로 줄어듦
  
  range(0, 3, 1) ▶ [0,1,2]
  range(3) ▶ [0,1,2]
  range(1, 4) ▶ [1,2,3]
  range(5, 1, -1) ▶ [5,4,3,2]
  ```

  - '오프셋' - 기준에서의 상대적 거리
  - 0부터 시작
  - Step 값을 통해 홀/짝수들의 합 구할 수 있음

  ```python
  # 짝수 합
  sum_value = 0
  for num in range(2, 101, 2):        # 시작값 2를 넣어야 간격값 2에 맞춰 짝수만 가지고 옴
      sum_value += num                
  print (sum_value)
  
  # 홀수 합
  sum_value = 0
  for num in range(1, 101, 2):        
      sum_value += num                
  print (sum_value)
  ```

  

- IF 조건식 & FOR 문

```python
startNum = int(input("시작 숫자 : "))
endNum = int(input("종료 숫자 : "))
incNum = int(input("증가치 숫자 : "))

if incNum == 0 :
    print("증가치는 0을 입력할 수 없으므로 기본값인 1로 처리함...")
    incNum = 1  # print명령 아랫 줄에 넣어서 print 처리 후 incNum에 1을 넣게끔
for num in range(startNum, endNum-1, incNum) :
    print(num, end=" ")
```





### 중첩 For문

>루프 안 '명령 자리'에 또 다른 루프로 중첩

*#들여쓰기*  특히 "주의"

```python
# 형식
for i in range() :
    for k in range() : 
        print('')
        
# 필요에 따라 IF
```



```python
# 구구단 예시
for dan in range(1,16) :					#1단부터 15단까지
    print(dan, "단")							#각 단마다 먼저 몇 단인지 출력
    for num in range(2, 10):				
        print(dan, "*", num, "=", dan * num) #dan*num은 특정변수 선언해서 길이 줄여도 됨. 
```



### Break

> 반복문 끝내는 명령

```python
## 구구단 결과값 제한
for dan in range(1, 10):
    for num in range(1, 10):
        result = dan * num
        if result > 30 :    # 30보다 크면 중지  → result<=30
            break           # 내어쓰기 들여쓰기 주의(가장 가까운 반복문 중단 명령)
        print(dan, "*", num, "=", result, end="\t")
    print()
```



- 특정 변수에 True/False 값 활용

  - Global Variable 에 False값 선언

  - Break 조건이 들어있는 내부에 True값을 배치

  - 내부 for문의 종료 명령을 IF조건문으로 달아서 내부에서 변수가 True가 된걸 이용해 

    ​			참일 때, Break하라는 명령 → 내부 For문 종료

```python
endFlag = False                 #끝낼 곳에 깃발 꼳을꺼에요. 여긴 아님ㅋ
for dan in range(1, 10):
    for num in range(1, 10):
        result = dan * num
        if result > 30 :
            endFlag = True      #조건에 해당하는 최초값 "여기에요" / True로 바뀜
            break               #"여기야? 오케이 스탑" / endFlag를 True로 바꾼 채 종료
        
        print(dan, "*", num, "=", result, end="\t") #일단 지금까지 나온건 출력할게요
    
    if endFlag :        #만약에 거기 끝나면(endFlag) 밖에도 끝낼게 ? / endFlag 참이면
        break           #나왔네? 나도 첫번째 for문 끝냄 / break → 종료(endFlag 참이라서)
    print()
```



- 특정 값 반복 출력 / 외부For문 Range 값들에 할당

```python
for y in range(1, 10) :
    for x in range(y) :
        print('*', end = '')
    print()
    
*
**
***
****
*****
******
*******
********
*********

#ASCII 코드 등과 같은 고유값들 활용 가능
munja = int(input("원하는 ASCII 문자번호 입력 : "))
for y in range(1, 10) :
    for x in range(y) :
        print(chr(munja), end = '')
        munja += 1
    print()
# 48 입력시
0
12
345
6789
:;<=>
?@ABCD
EFGHIJK
LMNOPQRS
TUVWXYZ[\
```



### Continue

> ''현재 루프(Loop)'만 건너뛰고 나머지는 계속 반복 수행

- 특정 조건에 따라 루프를 끝내고 다음 명령으로 이동하게끔

  → '특정 조건' 제시



## 실습

```
[ 실습 1 ]
1. forLab1.py 라는 소스를 만든다.
2. for문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. print() 함수로 숫자를 하나만 출력해야 한다.

    1 2 3 4 5 6 7 8 9 10



[ 실습 2 ]
1. forLab2.py 라는 소스를 만든다.
2. for 문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. print() 함수로 숫자를 하나만 출력해야 한다.

    0
    1
    2
    3
    4



[ 실습 3 ]
1. forLab3.py 라는 소스를 만든다.
2. for 문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. ‘@’ 기호문자 하나를 출력하는 print() 함수 호출을 5번 반복한다.
    @
    @
    @
    @
    @



[ 실습 4 ]
1. forLab4.py 라는 소스를 만든다.
2. 다음과 같은 결과가 출력되도록 구현한다.

    9 : 홀수
    8 : 짝수
    7 : 홀수
    6 : 짝수
    5 : 홀수
    4 : 짝수



[ 실습 5 ]
1. forLab5.py 라는 소스를 만든다.
2. 1부터 10사이의 난수를 추출하여 start 변수에 저장한다.
3. 30부터 40사이의 난수를 추출하여 end 변수에 저장한다.
4. start 부터 end 까지의 숫자들 중에서 짝수의 합을 구해 다음 형식으로 출력한다.

    X 부터 Y 까지의 짝수의 합 : ZZ



[ 실습 6 ]
1. forLab6.py 라는 소스를 만든다.
2. evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
3. 1 부터 100 까지의 값 중에서 
   짝수의 합은 evenNum 에 누적하고 
   홀수의 합은 oddNum 에 누적한다.
4. 수행 결과는 다음과 같이 출력한다.

    1부터 100까지의 숫자들 중에서 
    짝수의 합은 XXX 이고 
    홀수의 합은 YYY 이다.

```

