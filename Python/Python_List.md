# 리스트(List)

- **요소**(Element)

  - 리스트에 소속되는 각각의 값
  - 리스트에는 주로 같은 타입 요소
- 개별 요소 읽기 = `print(<리스트명>[요소 Index값])`
- **범위** 지정

```python
#형식
[begin : end : step]

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(nums[2:5])
[2, 3, 4]
print(nums[:4])
[0, 1, 2, 3]
print(nums[5:])
[5, 6, 7, 8, 9]
print(nums[1:7:2])
[1, 3, 5]
print(nums[::2])
[0, 2, 4, 6, 8]

```

- **Unpacking**

```python
list = ['p', 'y', 't', 'h', 'o', 'n']

v1, v2, v3, v4, v5,v6 = list

print(v1)	#p
print(v2)	#y
print(v3)	#t
print(v4)	#h
print(v5)	#o
print(v6)	#n

print(*list, sep='') 		# *을 통해 각값들을 붙여서 괄호없이 출력
python
```



### 삽입

1. **인덱싱(Indexing)**

   - 범위를 지정해서 요소/리스트를 그 범위에 삽입

   ``` python
   nums = [1, 2, 3, 4, 5]
   nums[2:2] = [90, 91, 92]	#3번째 값 앞에 삽입됨
   print(nums)
   
   [1, 2, 90, 91, 92, 3, 4, 5]
   
   nums = [1, 2, 3, 4, 5]
   nums[2] = [90, 91, 92]	#3번째 값 교체_ 리스트가 들어감
   print(nums)
   
   [1, 2, [90, 91, 92], 4, 5]
   #★ len(nums) 는 5로 그대로임.
   ```

   

2. **Append**

   - 리스트 **끝**에 추가됨

   ```nums = [1, 2, 3, 4, 5]

   nums = [1, 2, 3, 4, 5]
   nums.append(6)
   
   [1, 2, 3, 4, 5, 6]
   ```

   

3. **Insert**

   - *(삽입할 위치 , 요소값)* 형식으로 **중간**에 삽입

   ```python
   nums = [1, 2, 3, 4, 5]
   nums.insert(2, 10)
   
   [1, 2, 10, 3, 4, 5]
   ```

   

4. **Extend**

   - **병합**

   ```python
   <기준 리스트>.extend(<병합될 리스트>)
   
   list1 = [1, 2, 3, 4, 5]
   list2 = [10, 11]
   list1.extend(list2)
   
   #list3 = list1 + list2 처럼 리턴할 새로운 변수 만들지 않아도 됨.
   
   [1, 2, 3, 4, 5, 10, 11]
   ```





### 삭제

1. **remove**
   - 전달받은 요소값 **찾아** 삭제
2. **del**
   - **순서값 지정**하여 삭제
3. **clear**
   - 리스트 **모든 요소** 삭제
4. **빈 대괄호**
   -  **일정 범위** 요소 다수 삭제

```python
nums = [10, 20, 30, 50, 40, 70,80, 95, 100]

nums.remove(40)
[10, 20, 30, 50, 70, 80, 95, 100]

del(nums[3])		#del도 범위 지정 가능
[10, 20, 30, 70, 80, 95, 100]

nums[1:4] = []
[10, 80, 95, 100]

#전체 삭제
del nums[:]
nums[:] = []

```

*※ `.pop()` 은 끝 값 삭제하지만 그와 동시에 **해당 값 리턴**

​		→ `.pop()` = `.pop(-1)` = 마지막 요소 추출





### 검색

1. **Index**

   - 해당 **인데스 값**을 반환

   ``` python
   score = [60, 80, 90, 90, 75, 100]
   median = score.index(75)
   print(median)
   
   3
   ```

   

2. **Count**

   - 지정 단어 입력 획수(반복 횟수)

   ```python
   score = [60, 80, 90, 90, 75, 100]
   score.count(90)
   
   2
   ```

   

3. **Len**

   - 리스트 "요소 **개수**"

   ```python
   score = [60, 80, 90, 90, 75, 100]
   len(score)
   
   6
   ```

   

4. **Min** / **Max**

   - 최소 / 최댓값

5. **In** / **not In**

   - 입력 여부

   ```python
   if ~ in/not in <리스트> 형식
   ```

   



### 정렬

1. **Sort**

   - **오름차순** 정렬
   - `sorted(<리스트명>)` : 정렬된 결과 별도의 변수에 대입 받는 것
     - 새로운 리스트 반환

2. **Reverse**

   - **역순 정렬**

     

*# `.sort( reverse = True)`하면 **내림차순** 정렬*

*# "Sort 이후에 Reverse" 하면 **내림차순** 정렬*



3. **Key**

   - 잠깐의 비교를 위한 변환

   ```python
   coutry = ["Korea", "japan", "CHINA", "america"]
   country.sort()
   ["CHINA", "Korea", "america", "japan"]	#자동대소문자 크기 비교
   
   country.sort(key = str.lower)
   ["america", "CHINA", "japan", "Korea"] # 잠깐 변환
   ```

   

- **Choice**

  ```python
  .choice(<리스트/튜플>)
  ```

  ```python
  surname = ['김', '이', '박', '최', '강', '윤', '장', '임', '오']
  import random
  for x in range(20):
      print(random.choice(surname) + '서방')
  #위 리스트 요소값들 중 하나 고르는 명령
  ```

  

## 이차원 리스트

> 여러 개의 리스트를 하나의 변수에 할당한 리스트 집합




| 학생 | A    | B    | C    | D    |
| ---- | ---- | ---- | ---- | ---- |
| 국어 | 59   | 72   | 45   | 48   |
| 수학 | 92   | 48   | 82   | 73   |
| 영어 | 75   | 86   | 94   | 92   |

위와 같은 표를

```python
kor_score = [59, 72, 45, 48]
math_score = [92, 48, 82, 73]
eng_score = [75, 86, 94, 92]

midterm_score = [kor_score, math_score, eng_score]
print(midterm_score)
[[59, 72, 45, 48], [92, 48, 82, 73], [75, 86, 94, 92]]
		#0행				#1행					2행

#인덱싱
print(midterm_score[0][2])		# 1행 2열
45
```



- *이중 리스트 순회*하여 최종 값 도출 ▶ *루프도 이중*으로 해야함

```python
lol = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
print(lol[0])
[1, 2, 3]
print(lol[2],[1])
7

for sub in lol :
    for item in sub :				# 이중 루프
        print(item, end="@")
    print()
    
1@2@3
4@5
6@7@8@9
```



- 응용

```python
score = [
    [88, 76, 92, 98],
    [65, 70, 58, 82],
    [82, 80, 78, 88]
    ]

total = 0
totalsub = 0
for student in score:
    sum = 0
    for subject in student:
        sum += subject
    subjects = len(student)
    print("총점 :", sum, "평균 :", sum / subjects)	#각 subject마다 총점 / 평균 출력
    total += sum
    totalsub += subjects
print("전체평균 :", total / totalsub)

총점 : 354 평균 : 88.5
총점 : 275 평균 : 68.75
총점 : 328 평균 : 82.0
전체평균 : 79.75
```





## 리스트 컴프리헨션 (Comprehension)_ 지능형 리스트



- 합쳐주는 format(<리스트>)

```python
#format을 통해 삽입
numlist1 = []
numlist1.append(1)
numlist1.append(2)
numlist1.append(3)
numlist1.append(4)
numlist1.append(5)
print("list1 = {}".format(numlist1))

list1 = [1, 2, 3, 4, 5]

=============================================
numlist2 = []
for n in range(1,6) :
    numlist2.append(n)
print("list2 = {}".format(numlist2))

list2 = [1, 2, 3, 4, 5]

==============================================
numlist3 =[1,2,3,4,5]
print("list3 = {}".format(numlist3))

list3 = [1, 2, 3, 4, 5]

===============================================
numlist4 = [ num for num in range(1, 6) ]
print("list4 = {}".format(numlist4))

list4 = [1, 2, 3, 4, 5]
```



- 빈 리스트 `[]` 안에 반복문을 통한 삽입을 한 줄로 작성

> **[**<값 표현식>  **for**  <요소>  **in**  <Sequence>  **if**  <조건>**]**	(꼭 이 형식이 다 포함되어야하는 건 아님.)
>
> **[**<값 표현식>  **if**  조건식 **else** <값 표현식2> **for** <요소> **in** <Sequence> **]**

```python
nums = []
for n in range(1,11) :
    nums.append(n*2)

▶ nums = [n*2 for n in range(1,11)]

[n for n in range(1, 11) if n % 3 == 0]
[3, 6, 9]

[n*n for n in range(1,11) if n % 3 == 0]
[9, 36, 81]


#중첩 반복문
#구구단
gugulist1 = [ dan * num for dan in range(1, 10) for num in range(1, 10)]


#A~Z 대문자 알파벳 리스트
list1 = [ chr(d)  for d in range(ord('A'), ord('Z')+1) ]	#ord


#글자개수 조건 추출
flowernames = ['rose', 'sunflower', 'tulip', 'magnolia', 'goldenbell', 'lily']
newlist10 = [i for i in flowernames if len(i) == 4]
print(newlist10)

['rose', 'lily']


#홀/짝 출력
list5 = [ d   if d % 2  else  '짝수' for d in range(1, 16)  ]
▶ range(1, 16)에서 d%2 값이 있으면 그대로 출력하고 0이되어 False가 되면 '짝수'로 출력

list6 = [ '홀수'   if d % 2  else  '짝수' for d in range(1, 16)  ]
print(list6)


##리스트 생성 반복
[[i + j for i in case_1] for j in case 2]	#대괄호를 꼭 붙여줘야함

r1 = ["Black", "White"]
r2 = ["Red", "Blue", "Green"]
r3 = [ t + p for t in r1 for p in r2 ]

print(r3)

[['BlackRed', 'WhiteRed'], ['BlackBlue', 'WhiteBlue'], ['BlackGreen', 'WhiteGreen']]
```



- 일반 식과 컴프리헨션 비교

```python
r1 = ["Black", "White"]
r2 = ["Red", "Blue", "Green"]
r3 = []
for t in r1 :
    for p in r2 :
        r3.append(t+p)		#t+p 한것을 r3에 삽입
print(r3)

r3 = [ t + p for t in r1 for p in r2 ]
print(r3)

['BlackRed', 'BlackBlue', 'BlackGreen', 'WhiteRed', 'WhiteBlue', 'WhiteGreen']
```







