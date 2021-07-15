# 튜플(Tuple)

> 불변 자료 집합
>
> **읽기 전용**

- 읽기 전용인 만큼 제공 함수는 리스트에 비해 적지만 *속도가 빠름*
  - 제공 메소드 : count, index



- 리스트와 동일하게 **'+'** & **'*'**로  **연산**과 **인덱싱**, **슬라이싱** 가능
  - 요소 **변경 / 삭제** 불가능

```python
tu = 1, 2, 3, 4, 5		#자동 튜플
print(tu[1])		#Indexing 조회
2
print(tu[-1])
5
print(tu[1:4])
(2,3,4)
print(tu[0] + tu[2] + tu[5])
9
print(tu + (6, 7))
1, 2, 3, 4, 5, 6, 7
print(tu * 2)
1,2,3,4,5,1,2,3,4,5
tu[1] = 100 	#불가
del tu[1] 		#불가
```



- 각 구성 요소 사이에 `,`를 붙임
  - "하나의 요소로 튜플 생성" ▶ 요소 뒤에 `,` 붙이기

```python
tu = 2,
value = 2
print(tu)
(2, )		#쉼표를 찍지 않으면 value 값과 구분되지 않음 / ()를 통해 튜플임을 알림
```



- `( )`로 둘러쌓인 구조



- 함수 ▶ **'함수 인자'** 들은 튜플로 전달



- 주로 *다른 종류의 데이터형의 항목을 변수에 바로 풀어쓰는_Unpacking / Indexing 용도*

```python
tu = "이순신", "김유신", "강감찬"
lee, kim, kang = tu 	#각 튜플의 인덱스 순으로 들어감
print(lee)
이순신
print(kim)
김유신
print(kang)
강감찬
```



- 정의할 때 **소괄호 없이** 값만 나열해도 무관



- **변수 연산**으로 값 교환 가능

```python
a, b = 10, 20
print("a:", a)
a: 10
print("b:", b)
b: 20

# 값을 교환합니다.
a, b = b, a

print("a:", a)
a: 20
print("b:", b)
b: 10
```



### 출력

```python
import time
def gettime():
    now = time.localtime()
    print(now, type(now))
    
    #time.struct_time(tm_year=2021, tm_mon=7, tm_mday=15, tm_hour=9, tm_min=55, tm_sec=48, tm_wday=3, tm_yday=196, tm_isdst=0)
    
    #<class 'time.struct_time'>
    
    return now.tm_hour, now.tm_min  #"",로 묶어서 나열"하여 자동으로 "튜플"로 형성(Unpacking)



result = gettime()
print("지금은 %d시 %d분입니다" % (result[0], result[1]))	#Indexing으로 포맷 출력

hour, minute = gettime()
print("지금은 %d시 %d분입니다" % (hour, minute))	# time 함수 자체 인수명 'hour' , ' minute' 으로 출력

# =============== divmod  ===============
d, m = divmod(7, 3)
#divmod(7,3) -> (2,1)
#각각 순서대로 d,m에 입력
print("몫", d)
print("나머지", m)
```

