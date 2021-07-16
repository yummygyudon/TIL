# 딕셔너리 (Dictionary)

- 키와 값의 쌍을 저장하는 대용량 자료구조
- **맵** / **연과배열**
- **키(Key)** 와 **값(Value)** 형태로 데이터 저장

```python
{키 1:값 1, 키 2:값 2, 키 3:값 3, ....}
```

- **값** 추출하는 방법 : 해당 값의 **키**를 **대괄호`[]`** 안에 넣어 호출

```python
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }

print(dic['boy'])
소년
print(dic['book'])
책

##삽입
dic['girl'] = '소녀'  
{'boy': '소년', 'school': '학교', 'book' : '책', 'girl' : '소녀'}'

##수정
dic['boy'] = '남자애'
{'boy': '남자애', 'school': '학교', 'book' : '책', 'girl': '소녀'}

##삭제
del dic['book']
{'boy': '남자애', 'school': '학교', 'girl': '소녀'}

```



- 찾는 키가 없을 경우 예외 발생
  - *예외 처리 구문* 이나 *get* method로 처리

```python
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }

print(dic.get('student'))   #.get 메서드로 val
print(dic.get('student', '사전에 없는 단어')) #새로운 key:Value 로서 'student'로 검색하면 '사전에 없는 단어'라는 값을 연결
```



- **특정 값**들만 **추출**
  - Key만 : `.keys()`
  - Value만 : `.values()`
  - 둘 다 : `items()` (단, for문에서 각 각 사용할 땐 두 가지 변수를 설정 해야함)

```python
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }

#for문에 직접 dictionary를 불러올 수는 없음
keylist = dic.keys()
for key in keylist:
    print(key)
boy
school
book

valuelist = dic.values()
for value in valuelist:
    print(value)
소년
학교
책

itemlist = dic.items()
for item in itemlist:
    print(item)
('boy', '소년')
('school', '학교')
('book', '책')

itemlist = dic.items()
for key,value in itemlist:      #For문과 쉼표로  key와 value를 각자 Unpacking
    print(key, value, sep="-")
boy-소년
school-학교
book-책

##구조 역변환
#키값만 모은 리스트
keylist = list(dic.keys())
['boy', 'school', 'book']
```



```python
score_of_class = {
    "class1": (77, 85, 67, 80, 90),
    "class2": (60, 80, 75, 98, 82),
    "class3": (72, 77, 65, 83, 95),
    "class4": (92, 70, 85, 67, 88)
}

for key, value in score_of_class.items() :     #, 구분자를 통해 key, value값 각각 할당
    print("[", key, "반]")
    print("총점 :", sum(value))
    print("최고점 :", max(value))
    print("최저점 :", min(value))
    
[ class1 반]
총점 : 399
최고점 : 90
최저점 : 67
[ class2 반]
총점 : 395
최고점 : 98
최저점 : 60
[ class3 반]
총점 : 392
최고점 : 95
최저점 : 65
[ class4 반]
총점 : 402
최고점 : 92
최저점 : 67
```



- **특정 값 추출** 메서드 활용

  ```python
  maria = {'korean': 94, 'english': 91, 'mathematics': 89, 'science': 83}
  
  average = sum(maria.values()) / len(maria)      #len이 값의 개수로 취급
  print(average)
  89.25
  ```

  

- **구조 변환**(list, tuple)

```python
list1 = [ ['boy', '소년'], ['school', '학교'], ['book', '책'] ]
dic = dict(list1)
print(dic)

{'boy': '소년', 'school': '학교', 'book': '책'}


list2 = [ ('boy', '소년'), ('school', '학교'), ('book', '책') ]   #튜플 리스트라도 첫째값을 key값으로
dic = dict(list2)
print(dic)

{'boy': '소년', 'school': '학교', 'book': '책'}


list3 = dict(boy= '소년', school='학교', book='책')  #키워드 Argument

#함수인수를 키워드 가변인수 (**v)로 위와 같이 아무이름으로나 key& value 에 부여
dic = dict(list3)
print(dic)

{'boy': '소년', 'school': '학교', 'book': '책'}

```



- 딕셔너리 **합병**
- **같은 키값**이 있으면 update할 Value로 기존 Value 데이터 **덮어씀**

```python
dic = { 'boy':'소년', 'school':'학교', 'book':'책' }
dic2 = { 'student' : '학생', 'teacher' : '선생님', 'book' : '서적'}

dic.update(dic2)	#같은 키값이 있으면 update할 Value로 기존 Value 데이터 덮어씀
print(dic)

{ 'boy':'소년', 'teacher' : '선생님', 'student' : '학생', 'school':'학교', 'book':'서적' }
```



- 사전 활용
  - Dictionary는 검색하기 편한 위치에 저장하기 때문에 **순서가 없는 컬렉션**

```python
#특정 알파벳 갯수 세기

song = """by the rivers of babylon, there we sat down
yeah we wept, when we remember zion.
when the wicked carried us away in captivity
required from us a song
now how shall we sing the lord's sonf in a strange land"""

alphabet = dict()
for c in song :	#문자열 → 한글자 한글자씩
    if c.isalpha() == False :	#공백, 쉼표 등
        continue				#무시
    c= c.lower()		#소문자로 바꾸기
    if c not in alphabet :	
        alphabet[c] = 1		#dict의 특정 키값(c) 의 value([c])로 1   
    else :
        alphabet[c] += 1	#dict에 키값이 있으면 1씩 더하기
        
print(alphabet)

{'b' : 4, 'y' : 5, 't' :9, 'h' : 9,......}

key = list(alphabet.keys())	#리스트로 변환하여 정렬해 보기 편하게
key.sort()
for c in key :
    num = alphabet[c]
    print(c, '=', num)
    
a = 12
b = 3
c = 3
d = 6
.
.
.
```





- **중복** 딕셔너리
  - 다른 Structure 들과 동일하게 인데스 값으로 호출 가능
  - if 조건식 / if ~ else에선 Value값 결정 (key는 if 조건식에 대입 안됨.)

```python
terrestrial_planet = {              #중복 딕셔너리 / Value값에 새로운 Dict
    'Mercury': {
        'mean_radius': 2439.7,
        'mass': 3.3022E+23,
        'orbital_period': 87.969
    },
    'Venus': {
        'mean_radius': 6051.8,
        'mass': 4.8676E+24,
        'orbital_period': 224.70069,
    },
    'Earth': {
        'mean_radius': 6371.0,
        'mass': 5.97219E+24,
        'orbital_period': 365.25641,
    },
    'Mars': {
        'mean_radius': 3389.5,
        'mass': 6.4185E+23,
        'orbital_period': 686.9600,
    }
}

#리스트와 같은 구조의 Indexing / 단 인덱스 번호가 아닌 [키값]으로 호출
print(terrestrial_planet['Venus']['mean_radius'])

6051.8
```





## 사전 컴프리헨션 (Dictionary Comprehension)

- 구조는 이전 다른 컬렉션들과 동일한 구조

```python
{(키와 값에 대한 수식) for <변수> in <대상> if <조건식 }
```



```python
dict = {t[0] : t[1] for t in tuples}	#튜플 내 첫번째 값은 Key로, 두번째 값은 Value로

dict = {k : v for k,v in tuples}	#키워드 가변 인수들 취급할 때 많이 사용
									#중첩 컬렉션의 경우
    

dict = {k : v for k,v in tuples if len(k) > 5} #k가 5보다 크면 dict에 입력
```



- 활용(1)

  - IF 조건식 & Key-Value 도치
```python
students = dict(둘리=90, 또치=85, 도우너=95, 희동이=75, 마이콜=80)
print(students)
{'둘리': 90, '또치': 85, '도우너': 95, '희동이': 75, '마이콜': 80}


pass_students = { k : v for k, v in students.items()}
print(pass_students)
{'둘리': 90, '또치': 85, '도우너': 95, '희동이': 75, '마이콜': 80}


pass_students = { k : v for k, v in students.items() if v > 80}
print(pass_students)
{'둘리': 90, '또치': 85, '도우너': 95}


pass_students = { k : v for k, v in students.items() if len(k) > 2}
print(pass_students)
{'도우너': 95, '희동이': 75, '마이콜': 80}


pass_students = { k : v for k, v in students.items() if len(k) > 2 and v > 80}
print(pass_students)
{'도우너': 95}


swap_students = { v : k for k, v in students.items() }  #기존에 value값이 key가 되면
print(swap_students)

{90: '둘리', 85: '또치', 95: '도우너', 75: '희동이', 80: '마이콜'}
#만약 점수가 같은 key가 있으면 key는 중복이 안되기때문에 하나는 사라짐
#나중에 들어간 같은 값이 덮어버리는 대체 형식
#기존 키값의 value값을 바꾸고 싶을 때 유용
```

  

- 활용 2
  - 순번 부여 & 새로운 값으로 교체

```python
oddeven= { d : '홀수'   if d % 2  else  '짝수' for d in range(1, 16)  }
#반복횟수(d)를 이용해 1부터 시작하여 키값으로 부여했고 Value에 '홀수'/'짝수' 부여
print(oddeven)
{1: '홀수', 2: '짝수', 3: '홀수', 4: '짝수', 5: '홀수', 6: '짝수', 7: '홀수', 8: '짝수', 9: '홀수', 10: '짝수', 11: '홀수', 12: '짝수', 13: '홀수', 14: '짝수', 15: '홀수'}


scores = {'길동': 90, '순희': 60, '영희': 80, '철수': 50}
grades = { name: 'PASS' if value > 70 else 'No-PASS' for name, value in scores.items()} #value 값에 대입하기
print(grades)
{'길동': 'PASS', '순희': 'No-PASS', '영희': 'PASS', '철수': 'No-PASS'}



member = { 'name'+str(i) : i*10 if i > 5 else  i + 100 for i in range(1,11) }
print(member)
{'name1': 101, 'name2': 102, 'name3': 103, 'name4': 104, 'name5': 105, 'name6': 60, 'name7': 70, 'name8': 80, 'name9': 90, 'name10': 100}


fruits = ['apple', 'mango', 'banana','cherry']
dic_fruits = {f:len(f) for f in fruits} #for문의 f의 값에 새로운 기준값들을 대입시켜 딕셔너리 만들기

print(dic_fruits)
{'apple': 5, 'mango': 5, 'banana': 6, 'cherry': 6}

print( {v : k for k, v in member.items()})
{101: 'name1', 102: 'name2', 103: 'name3', 104: 'name4', 105: 'name5', 60: 'name6', 70: 'name7', 80: 'name8', 90: 'name9', 100: 'name10'}

print( {v : k for k, v in dic_fruits.items()})  #key : value Swap
{5: 'mango', 6: 'cherry'}

```

