   # 예외 처리 (Exception)

> 프로그램 코드는 이상이 없지만 실행 중 불가피하게 발생하는 문제 처리

- 본래 에러 발생 직후 잔여 구문 여부 상관없이 프로그램 종료

```
try :
	<실행할 명령>
except [오류/예외] (as 변수) :
	<오류 처리문>
else :
	<예외가 발생하지 않을 때의 처리>
```

*#간단하게 "**try : except :**"까지만 사용 가능*



- **try 블록**의 코드를 실행하다가 "*예외* "가 발생하면 **except 블록**으로 점프하는 형식
  - *"예외가 발생하지 않는다 "*면 except블록은 무시됨

- 예외 처리 구문을 **루프(Loop)**로 감싸면 발생한 문제점 파악 용이
  - 예외 발생 시 다시 루프 선두로 복귀

```python
while True : 							#Error는 False
    str = input("점수를 입력하세요 : ")
    try :
        score = int(str)
        print("입력한 점수 : ", score)
        break							#예외 없이 조건에 맞는 구문을 갖추었을 때 종료
    except :
        print("점수 형식이 잘못되었습니다.")
print("작업 완료")      
```



## 예외의 종류

| 예외              | 설명                                                         |
| ----------------- | ------------------------------------------------------------ |
| NameError         | 초기화하지 않은 변수를 사용할 때 ( 명칭이 발견되지 않는다.)  |
| ValueError        | 값의 형식이 잘못되었다                                       |
| ZeroDivisionError | 0 으로 나누었다                                              |
| IndexError        | 범위를 벗어났다                                              |
| TypeError         | 타입이 맞지 않다.(ex. int값이 필ㅇ한 곳에 str 등을 사용했을 때) |

- except 뒤에 처리할 예외 명칭을 지정
  - 내부 처리명령은 지정된 예외에 대해서만 적용



```python
str = "89"
try : 
    score = int(str)
    print(score)
    a = str[5]		#89는 index 0(8), 1(9) 밖에 없음	▶ IndexError 예외 발생
except ValueError : 
    print("점수의 형식이 잘못되었습니다.")
except IndexError :
    print("첨자 범위를 벗어났습니다.")
print("작업완료")

89
첨자 범위를 벗어났습니다.
작업완료
```



- except 블록 **제한없음** , <u>*먼저 발생한 예외*</u> 에 맞는 하나만 선택

```python
# 두 개 이상 괄호로 묶어 동시에 받기 가능
except (ValueError, IndexError) :
    print("점수의 형식이나 첨자가 잘못되었습니다.")
```



- `as`를 통해 변수 지정 및 객체를 활용하여 *에러메세지*  출력 가능

```python
except ValueError as e :
    print(e)
#ValueError문 출력
```





## Raise 명령

> 고의적으로 예외 발생

- 작업 위한 **선결조건 맞지 않거나 문제 발생할 경우** 호출원으로 사용

```python
#1부터 지정한 정수까지의 합계를 구하는 함수

def calcsum(n) : 
    if n < 0 :
        raise ValueError	#except와 블록라인이 맞지 않아도 음수값이 입력되었을 때 바로 except블록으로 이동
    sum = 0 
    for i in range(n+1) : 
        sum += i
    return sum

try : 
    print("~10 = ", calcsum(10))
    print("~-5 = ", calcsum(-5))
except ValueError :
    print("입력값이 잘못되었습니다.")
    
~10 = 55
입력값이 잘못되었습니다.
```



※ 예외를 던지는 대신 **특이값**을 **리턴**하여 보고 하는 법

​	: Return값을 받아if문으로 점검해야하는 불편함이 있지만 None이 출력될뿐 다운은 되지않음

```python
def calcsum(n) : 
    if n < 0 :
        return -1
    sum = 0 
    for i in range(n+1) : 
        sum += i
    return sum

result = calcsum(10)
if result == -1 :
    print("입력값이 잘못되었습니다.")
else :
    print("~10 = ", result)
    
result = calcsum(-5)
if result == -1 :
    print("입력값이 잘못되었습니다.")
else :
    print("~10 = ", result)
    
~10 = 55
입력값이 잘못되었습니다.
```





## Finally

> 예외 발생 여부와 상관없이 **반드시 실행**해야하는 **강제 실행 명령**

*#sys 모듈의 `sys.exit()`를 사용해도 finally블록 명령은 수행함*

