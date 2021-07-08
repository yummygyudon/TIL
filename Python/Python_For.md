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
```

- 누적합 명령

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



### Break



### Continue



## 이중 루프

```python
# 형식
for i in range() :
    for k in range() : 
        print('')
        
# 필요에 따라 IF
```



