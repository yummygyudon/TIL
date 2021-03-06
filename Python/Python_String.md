# 문자열

- 문자열 변환 메소드 = `str()`
- 문자열은 메모리상 개별 문자들이 일렬로 늘어선 형태
  - 개별 문자를 읽을 때 : `[ ]`(대괄호)와 문자의 위치인 **'첨자'**를 적음
  - 앞으로 셀 때 = 0~ / 뒤에서 셀 때 =  -1 ~ -n (음수 값은 점점 작아짐)



- `[ ]`괄호에 첨자 하나만 적으면 해당 위치 문자를 읽지만 Range함수 같이 시작, 끝, 증가값 지정 가능


```python
for i, name in enumerate(['body', 'foo', 'bar']):
 print(i, name)

0 body		#앞에 첨자
1 foo
2 bar
```

*# enumerate : 첨자 같이 출력*




### 슬라이스

```python
[begin : end : step]
```

```python
s = "python"
print(s[2:5])
tho
print(s[3:])	#생략 가능(양 끝값이 기준)
hon
print(s[:4])
pyth
print(s[2:-2])	#2번째 t 부터 -2인 o 직전(h) 까지
th
```



```python
#파일 이름 형식 활용
file = "20171224-104830.jpg"
print("촬영날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영시간 : " + file[9:11] + "시 " + file[11:13] + "일")
print("확장자 : " + file[-3:])

촬영날짜 : 12월 24일
촬영시간 : 10시 48분
확장자 : jpg
```



```python
#Step 역순
day = "월화수목금토일"
print(day[::2])
월수금일
print(day[::-1])
일토금목수화월
print(day[::-2])
일금수월
```



## 문자열 메서드

### 검색

- `.find('(찾을 문자)')`
  - 대상 문자 없을 경우 : **- 1** 반환
  - `.rfind`는 역순으로 찾을 때
- `.count()`
  - 문자열 내에서 단어가 몇 개 들어갔는지



### 조사

- `in`구문 사용

  ```python
  <단어> in / not in <문자열>
  ```

  - 포함 = True / 미포함 = False 반환 ( not in 은 반대)

  ```python
  s = "python programming"
  print('a' in s)
  print('z' in s)
  print('pro' in s)
  print('x' not in s)
  
  True
  False
  True
  True
  ```

  

- `.startswith()` / `endswith()`
  - 시작 글자 확인 / 끝 글자 확인
  - 기준 문자열 길이 제한 없음
  
  ```python
  name = "김한결"
  if name.startswith("김"):
      print("김가입니다.")
  if name.startswith("한"):
      print("한가입니다.")
  
  김가입니다.
      
      
  file = "girl.jpg"
  if file.endswith(".jpg"):
      print("그림 파일입니다.")
  
  그림 파일입니다.    
   
  ```
  
  
  
- `.isalpha` / `.islower` / `.isupper` / `.isalnum` = 모든 문자의 알파벳 여부 / 소문자 여부 / 대문자 여부 /알파벳&숫자 여부

- `.isnumeric` / `.isdigit` = 모든 문자의 숫자 여부

- `.isspace` = 공백인지



### 변경

- `.lower()` / `.upper()` = 소문자화 / 대문자화

- `.swapcase()` = 대소문자 **뒤집기**

- `.capitalize()` = 문장의 **첫 글자 대문자**

- `.title` = 모든 단어의 **첫 글자 대문자**

- `.strip()` = **공백 제거**
  - `.rstrip` : 오른쪽 공백 제거 / `.lstrip` : 왼쪽 공백 제거

    ```python
    s = "  angel   "	#양쪽 공백
    print(s + "님")
    print(s.lstrip() + "님")
    print(s.rstrip() + "님")
    print(s.strip() + "님")
    
    
      angel   님
    angel   님
      angel님
    angel님
    ```

- `sorted()` : 정령_오름차순

```python
str1 = ['p','r','e','t','t','y','f','l','o','w','e','r']

print("sorted: ", sorted(str1))# reverse=True
sorted:  ['e', 'e', 'f', 'l', 'o', 'p', 'r', 'r', 't', 't', 'w', 'y']
```



### 분할

- `.split(<구분자>)` = 구분자 넣으면서 단어 분할
  
  - 인수 없이 호출 ▶ "공백" 기준으로 분할
  - 구분자는 *출력되지 않음*
  
- `.splitlines()` = "개행문자" / "파일구분자" / "그룹구분자" 등을 기준으로 **문자열 분할**

- `(삽입문자).join(삽입될 문자열)`

  ```python
  s = "._."
  print(s.join("대한민국"))
  
  대._.한._.민._.국
  
  #split & join 으로 대체작업
  s2 = "서울->대전->대구->부산"
  city = s2.split("->")		#우선 구분자 말고 도시명만 빼오기
  print(" 찍고 ".join(city))
  
  서울 찍고 대전 찍고 대구 찍고 부산
  ```

  

### 대체

- `.replace(<기존문자>, <바꿔질 문자>)` = 문자 바꾸기

  ```python
  s = "독도는 일본땅이다. 대마도도 일본땅이다"
  print(s.replace("일본", "한국"))
  
  독도는 한국땅이다. 대마도도 한국땅이다.
  ```

- `.center()` = 특정 폭에 맞춰서 가운데 정렬

  - `.ljust` / `.rjust`  = 좌/우 정렬

  ```python
  message = "안녕하세요"
  print(message.center(30))		#공백이 들어가는 양
  print(message.ljust(30))
  print(message.rjust(30))
  
  			안녕하세요		
  안녕하세요				
  						안녕하세요
  ```

  



## 포맷팅(String/Tuple/List/Dict 공통)

> 문자열 사이사이에 다른 정보를 삽입하여 조립하는 기법

> 문자마다 구분지어 연산할 필요 없이 문자열 내에 삽입

| 표식                    | 설명      |
| ----------------------- | --------- |
| %**d**<br />(decimal)   | 정수      |
| %**f**<br />(float)     | 실수      |
| %**s**<br />(string)    | 문자열    |
| %**c**<br />(character) | 문자 하나 |
| %**h**<br />(hexa)      | 16진수    |
| %**o**<br />(octal)     | 8진수     |
| %**%**                  | % 문자    |

★인덱스 순서대로 해당 표식에 적용되는 값들이 들어감★

- 참조값 변수는 **%**로 이어줌

  ```python
  price = 500
  print("사탕 가격은 %d 원!" % price)
  
  사탕 가격은 500원! 
  ```



- 인덱스 순 삽입

  ```python
  month = 8
  day = 15
  anni = "광복절"
  print("%d월 %d일은 %s이다." % (month, day, anni)) #튜플 인덱스 순으로 들어감
  
  8월 15일은 광복절이다.
  ```



- **정렬 조정**

  ```python
  #%와 표식문자 사이의 수 → 공백
  #양수 : 오른쪽에 자리 지정
  #음수 : 왼쪽에 자리 지정
  price = [30, 13500, 2000]
  for p in price : 
      print("가격:%d원" % p)
  
  가격:30원
  가격:13500원
  가격:2000원
      
  for p in price : 
      print("가격:%7d원" % p)
      
  가격:		   30원
  가격:		13500원
  가격:		 2000원
      
  for p in price : 
      print("가격:%-7d원" % p)
      
  가격:30		 원
  가격:13500	 원
  가격:2000		 원
      
      
  pie = 3.14159265
  
  # "%(정렬간격값).(소수이하 자릿수 값)f"%(값 가져올 변수명)
  #점 왼쪽 : 간격 / 점 아래 : 출력할 자릿수
  
  print("%10.3f"%pie)     
  #소수자릿수 표현하기때문에 'f%(변수명)'_ %f 는 실수 포맷팅 명령
  
  print("%10.6f"%pie) # 3.141593 _ 반올림되어 6자리
  
  print("%10.f"%pie) # 3 _ "".뒤로 원하는 자릿수 없다"고 명령
  
  print("%10f"%pie)# 간격 정렬(그저 정수)
  
  print("%5f"%pie) # 정렬(f 앞의 숫자를 공백구간 값으로 취급)
  ```



- **1000 단위 콤마**

``` python
num = 1000000
print('%s' % format(num, ','))
```





### 신형 포맷팅

> Python 2.6 이후

- `.format(인수목록)`
- 정보를 삽입할 위치에 `{ }`괄호를 적고 Format 매서드의 인수로 삽입할 변수를 나열한다.
  - `{ }` 괄호 자리에 차례대로 인수값이 삽입됨

```python
name = "동규"
age = 23
height = 170.5
print("이름:{}, 나이:{}, 키:{}".format(name, age, height))

이름:동규, 나이:23, 키:170.5
            

#{해당키의 Value값 호출}            
print("이름:{name}, 나이:{age}, 키:{height}".format(name = "동규", age = 23, height = 170.5))

이름:동규, 나이:23, 키:170.5
```



- 사전 저장 값 출력 시

  - **Dict**를 **인수**로 주고 `[ ]`괄호 안에 **키(Key)**를 적는다
    - Dict의 키로부터 Value 검색하여 문자열 중간에 삽입

  ```python
  boy = {"name":"동규", "age":23, "height":170.5}
  print("이름:{0[name]}, 나이:{0[age]}, 키:{0[height]}".format(boy))
  		#[키]의 0번째 값 -> {0[키]}
  이름:동규, 나이:23, 키:170.5
  ```

  
  
  -  `{ }`괄호 안의 `:`다음에 인수의 타입을 지정
    - 포맷팅 표식 문자에서 %만 뺀 알파벳
  
  ```python
  name = "동규"		#인덱스 0
  age = 23		 #인덱스 1
  height = 170.5	 #인덱스 2
  print("이름:{0:s}, 나이:{1:d}, 키:{2:f}".format(boy))
  
  이름:동규, 나이:23, 키:170.5
  
              
  name = "동규"		#인덱스 0
  age = 23		 #인덱스 1
  height = 170.5	 #인덱스 2
  print("{} 학생은 나이가 {}이고 키는 {:.2f} 입니다".format(name, age, height))
  
  동규 학생은 나이가 23이고 키는 170.50 입니다.
  ```
  
  
  
  - 폭과 정밀도를 지정하는 방식 (기존 포맷팅 방식과 동일)
    - `:`과 '타입 문자' 사이에 지정
    - 별다른 지정  없으면 **문자열**은 ***왼쪽***으로 정렬, **수치값**은 ***오른쪽***으로 정렬
      - 왼쪽(**<**) / 오른쪽(**>**) / 중앙정렬(**^**)
      - 위 정렬기호 왼쪽에 대체기호(***"@", "#", "$"** 등)  공백 대체 가능







- **f- String**

```python
<형식>
f"{인수명} ...{인수명}.."
# 폭과 정밀도 & 실수의 경우 소숫점 설정 가능

name = "동규"		#인덱스 0
age = 23		 #인덱스 1
height = 170.5	 #인덱스 2
print(f"{name} 학생은 나이가 {age}이고 키는 {height:.2f} 입니다")

동규 학생은 나이가 23이고 키는 170.50 입니다.
```

