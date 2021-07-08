# IF문

> 참, 거짓을 기준으로 각 경우에 따라 명령 실행

*# [ <u>들여쓰기</u> ] 매우매우 중요*

- <참> 조건만 주고 실행 가능
  - 거짓인 경우 무시하고 지나침

```python
age = int(input("너 몇살이니? "))
if age < 19:
    print("애들은 가라")
```



- 비교 연산자
  - 두 값의  *상등여부* 나 *대소관계*  비교

```python
a = 10
if a == 3:
    print("3이다")
if a > 5:
    print("5보다 크다")
if a < 5:
    print("5보다 작다")
if a != 3:
    print("3이 아니다")
```



- Data 타입 별 기본 논리값 조건

  - 비교연산식 대신 변수 바로 쓸 수 있음

    | 타입                   | 참                  | 거짓    |
    | ---------------------- | ------------------- | :------ |
    | 숫자                   | 0이 아닌 숫자       | 0       |
    | 문자열                 | 비어 있지 않은 상태 | ""      |
    | 리스트, 튜플, 딕셔너리 | 비어 있지 않은 상태 | 빈 상태 |

```python
energy = 1
if energy:
    print("열심히 싸운다")
```



- *문자의 대소* 비교 조건

```python
 if ("korea" > "japan"):
    print("한국이 더 크다")
if ("korea" < "japan"):
    print("일본이 더 크다")
    
>>> 한국이 더 크다
```



- <블록구조>
  - 한꺼번에 실행되는 명령들의 묶음
  - 한 조건 내부에 있는 여러명령 모두 실행
  - <u>*"들여쓰기"*</u> 주의

```python
age = 16
if age < 19:
    print("1 - 애들은 가라")
    print("1 - 공부 열심히 해야지")

age = 22
if age < 19:
    print("2 - 애들은 가라")
print("2 - 공부 열심히 해야지")

>>>2 - 공부 열심히 해야지
##########################################
age = 22
if age < 19:
    	print("2 - 애들은 가라")
    print("2 - 공부 열심히 해야지")

>>> 들여쓰기 오류
###########################################

if age < 19:
    print("3 - 애들은 가라")
else:
    print("3 - 어서 옵쇼")

age = 12
if age < 19:
    print("4 - 애들은 가라")
    print("4 - 공부 열심히 해야지")
else:
    print("4 - 어서 옵쇼")
    print("4 - 즐거운 시간 되세요")
```

- *else문 / elif*  개수 제한 없음

```python
age = 23
if age < 19:
    print("애들은 가라")
elif age < 25:
    print("대학생입니다")
else:
    print("어서 옵쇼")



if age < 19:
    print("애들은 가라")
if age >= 19 and age < 25:
    print("대학생입니다")
if age >= 25:
    print("어서 옵쇼")

```



```python
money = 6500
if money >= 20000:
    print("탕수육을 먹는다")
elif money >= 10000:
    print("쟁반 짜장을 먹는다")
elif money >= 6000:
    print("짬뽕을 먹는다")
elif money >= 4000:
    print("짜장면을 먹는다")
else:
    print("단무지를 먹는다")
print("뭐든 맛있다!!")

# >= 6000에서 참으로 처리됨
#맨 아래 print는 if와 같은 라인이라 생략 X
짬뽕을 먹는다
뭐든 맛있다!!
```



```python
man = True
age = 22
if man == True:
    if age >= 19:
        print("1 - 성인 남자입니다.")


if man == True:
    if age >= 19:
        print("2 - 성인 남자입니다.")
    else:
        print("2 - 소년입니다.")

if man == True:
    if age >= 19:
        print("3 - 성인 남자입니다.")
else:                                   #맨위에 있는 IF와 짝꿍
    print("3 - 소년입니다.")             #잘못된 구성(여자까지 소년입니다로 출력됨)

```



```python
import random
num = random.randint(1, 20)
if num % 2 == 0 :
    print(num, "은 짝수", sep="")
else :
    print(num, "은 홀수", sep="")
print("-"*50)

if num % 2 == 0 :
    print(num)
    print("은 짝수")
else :
    print(num)
    print("은 홀수")
print("-"*50)

if num % 2 == 0 :
    print(num, end="")
    print("은 짝수")
else :
    print(num, end="")
    print("은 홀수")
print("-"*50)
```



```python
import random
num = random.randint(1, 20)

print("num(", num, ") : ", sep="", end="")  #sep=""로 출력될 값사이의 간격 없애기, end=""로 개행되지않고 붙여주기
if num < 10 :
    print("10보다 작은 수-", end="")
    if num < 5 :
        print("5보다 작은 수-", end="")
    else :
        print("5보다 큰 수-", end="")
else :
    print("10보다 큰 수-", end="")
print("OK?")
```



```python
data = input("데이터를 입력하세용 : ")
print("[" + data + "]")
if len(data) == 0:
    print("입력한 내용이 없네요")        
    #공백(스페이스바) 또한 1자로 취급해서 값은 없고 공백만 넣어도 data라고 인식
else:
    print("입력한 내용 :", data)
```







## 실습

### 문제

```
[ 실습 1 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 코딩(구현)하고 conditionLab1.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
2. 입력받은 숫자가 10보다 큰 경우에만 ‘OK’ 라는 문자열을 출력한다.

###########################################################################
###########################################################################

[ 실습 2 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab2.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. color_name 이라는 변수에 사용자로부터 칼라 이름을 하나 입력받는다.
2. 입력받은 칼라명이 red 이면 ‘#ff0000’라는 문자열을 출력한다.
  입력받은 칼라명이 red 가 아니면 ‘#000000’라는 문자열을 출력한다.

###########################################################################
###########################################################################


[ 실습 3 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab3.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.  
조건 평가 시 and 연산자를 사용해서 해결한다.
2. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   x 학년은 저학년입니다.
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   x 학년은 고학년입니다.

###########################################################################
###########################################################################

[ 실습 4 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab4.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.  
조건 평가 시 or 연산자를 사용해서 해결한다.
2. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   x 학년은 저학년입니다.
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   x 학년은 고학년입니다.

###########################################################################
###########################################################################

[ 실습 5 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab5.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
(1) score 라는 변수에 0 부터 100 사이의 숫자를 랜덤으로 추출하고 저장한다.
(2) score 변수의 값의 크기에 따라서 다음의 내용을 출력한다. à print() 함수를 5개 사용하여 해결한다.
   score 변수의 값이 90~100 이면   xx점은 A등급입니다.
   score 변수의 값이 80~89 이면   xx점은 B등급입니다.
   score 변수의 값이 70~79 이면   xx점은 C등급입니다.
   score 변수의 값이 60~69 이면   xx점은 D등급입니다.
   score 변수의 값이 0~59 이면   xx점은 F등급입니다.

###########################################################################
###########################################################################

[ 실습 6 ] if 문 사용 실습
conditionLab5.py 파일을 conditionLab6.py 파일로 복사한 다음 한 개의 print() 함수로 해결한다.

###########################################################################
###########################################################################

[ 실습 7 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab7.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
  입력 받을 때의 메시지- 1부터 10사이의 숫자를 하나 입력하세요 :
2. 입력 받은 숫자가 1부터 10사이의 숫자가 아니면 다음과 같이 처리한다.
 
 
3. 입력 받은 숫자가 1부터 10사이의 숫자이면 다음과 같이 처리한다.

###########################################################################
###########################################################################


[ 실습 8 ] if 문 사용 실습
다음에 제시된 기능을 PyCharm으로 구현하고 conditionLab8.py 파일명으로 저장한 후 수행시키고 테스트한 다음 소스 파일을 제출한다.
1. oper_num 이라는 변수에 1부터 10사이의 랜덤값을 추출하여 대입한다.
2. 추출된 값이 1이거나 6이면 300 과 50 의 덧셈 연산을 처리한다.
  추출된 값이 2이거나 7이면 300 과 50 의 뺄셈 연산을 처리한다.
  추출된 값이 3이거나 8이면 300 과 50 의 곱센 연산을 처리한다.
  추출된 값이 4이거나 9이면 300 과 50 의 나눗셈 연산을 처리한다.
  추출된 값이 5이거나 10이면 300 과 50 의 나머지 연산을 처리한다.
3. 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.)
    결과값 : XX
```

*[출처] : multicampus_ 김정현 강사님 



### 풀이

- 문제 1

```python
#[실습 1]
##정답 1
num = int(input("숫자 하나를 입력하세요 : "))

if num > 10 :
    print("OK")
    
    
##정답 2
input_data = input("숫자를 입력하세요 : ")
num = int(input_data)

if num > 10 :
    print("OK")
```

- 문제 2

```python
#[실습 2]
##정답 1
color_name = input("색을 입력하세요 : ")

if color_name == "red":
    print("#ff0000")
else :
    print("#000000")
    
    
##정답 2 
color_name = input("색을 입력하세요 : ")

if color_name == "red" :
    print("'#ffOOOO'")
if color_name != "red" :
    print("'#OOOOOO'")
```

- 문제 3


```python
#[실습 3]
import random					#난수 추출 random 모듈 가져오기
grade = random.randint(1, 6)	#.randint(x, y) : x와 y 사이의 정수 무작위 추출
								#rand(무작위)int(정수)

print("grade ", grade, ": ", sep="", end="")
if grade >=1 and grade <=3 :
    print(grade, " 학년은 저학년입니다.")
else :
    print(grade, " 학년은 고학년입니다.")
```

- 문제 4


```python
#[실습 4]
import random
grade = random.randint(1, 6)

##정답 1
print("grade (", grade, ") : ", sep="")
if grade == 1 or grade == 2 or grade == 3 :
    print(grade, " 학년은 저학년입니다.")
elif grade == 4 or grade == 5 or grade == 6 :
    print(grade, " 학년은 고학년입니다.")
    
    
##정답 2
print("grade(", grade, ") : ", sep="")
if grade == 1 or grade == 2 or grade == 3 :
    print (grade, "학년은 저학년입니다.")
else :
    print (grade, "학년은 고학년입니다.")
```

- 문제 5


```python
#[실습 5]
import random
score = random.randint(0, 100)

if score >=90 :
    print(score, "점은 A등급입니다.")	#[, sep = ""]으로 간격 줄여주기
elif score >=80 :
    print(score, "점은 B등급입니다.")
elif score >=70 :
    print(score, "점은 C등급입니다.")
elif score >=60 :
    print(score, "점은 D등급입니다.")
else :
    print(score, "점은 F등급입니다.")
```

- 문제 6


```python
#[실습 6]
import random
score = random.randint(0, 100)

##정답 1
if score >=90 :
    credit = "A"
elif score >=80 :
    credit = "B"
elif score >=70 :
    credit = "C"
elif score >=60 :
    credit = "D"
else :
    credit = "F"

print(score, "점은 ", credit, "등급입니다.", sep = "")


##정답 2
if score >= 60 and score <= 100 :
    level = "D"
    if score >= 70 and score <= 79 :
        level = "C"
    if score >= 80 and score <= 89:
        level = "B"
    if score >= 90 and score <= 100 :
        level = "A"
else :
    level = "F"
print (score, "점은 ",level,"등급입니다.", sep="")
```

- 문제 7


```python
#[실습 7]
num = int(input("1부터 10사이의 숫자를 하나 입력하세요 : "))

if num >0 and num <10 :			#1 <= num <=10 도 가능
    if num % 2 == 0 :			#num % 2 == 1로 참 조건을 홀수 출력으로 바꿔도 됨
        print(num, " : 짝수")
    else :
        print(num, " : 홀수")
else :
    print("1부터 10사이의 값이 아닙니다.")
```

- 문제 8


```python
#[실습 8]
import random
oper_num = random.randint(1, 10)

if oper_num == 1 or oper_num == 6 :
    calcul = 300+50
elif oper_num == 2 or oper_num == 7 :
    calcul = 300-50
elif oper_num == 3 or oper_num == 8 :
    calcul = 300*50
elif oper_num == 4 or oper_num == 9 :
    calcul = 300/50
else :									#oper_num == 5 or oper_num == 10 가능
    calcul = 300%50

print("결과값 : ", calcul, sep = "")
```