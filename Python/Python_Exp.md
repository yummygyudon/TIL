# 파이썬 (Python)

> 1991년 *귀도 반 로섬(Guido van Rossum)*이 개발한
>
> 프로그래밍 언어의 일종

> 인터프리터 방식으로 동작하는 *스크립트(Script) 언어*

![img](md-images/01.png)

- 파이썬 추구하는 가치

```
파이썬 선(禪)(Zen of Python)

-아름다움이 추함보다 좋다.(Beautiful is better than ugly.)
-명시가 암시보다 좋다.(Explicit is better than implicit.)
-단순함이 복잡함보다 좋다.(Simple is better than complex.)
-복잡함이 꼬인 것보다 좋다.(Complex is better than complicated.)
-수평이 계층보다 좋다.(Flat is better than nested.)
-여유로운 것이 밀집한 것보다 좋다.(Sparse is better than dense.)
-가독성은 중요하다.(Readability counts.)
-특별한 경우라는 것은 규칙을 어겨야 할 정도로 특별한 것이 아니다.
(Special cases aren't special enough to break the rules.)
-허나 실용성은 순수성을 이긴다.(Although practicality beats purity.)
-오류는 절대 조용히 지나가지 않는다(Errors should never pass silently.)
-명시적으로 오류를 감추려는 의도가 아니라면.(Unless explicitly silenced.)
-모호함을 앞에 두고, 이를 유추하겠다는 유혹을 버려라.
(In the face of ambiguity, refuse the temptation to guess.)
-어떤 일에든 명확한 - 바람직하며 유일한 - 방법이 존재한다.
(There should be one— and preferably only one —obvious way to do it.)

-비록 그대가 우둔하여 그 방법이 처음에는 명확해 보이지 않을지라도.
(Although that way may not be obvious at first unless you're Dutch.)
-지금 하는게 아예 안하는 것보다 낫다.(Now is better than never.)
-아예 안하는 것이 지금 당장보다 나을 때도 있지만.
(Although never is often better than right now.)
-구현 결과를 설명하기 어렵다면, 그 아이디어는 나쁘다.
(If the implementation is hard to explain, it's a bad idea.)
-구현 결과를 설명하기 쉽다면, 그 아이디어는 좋은 아이디어일 수 있다.
(If the implementation is easy to explain, it may be a good idea.)
-네임스페이스는 대박 좋은 아이디어다 -- 더 적극적으로 이용해라!
(Namespaces are one honking great idea—let's do more of those!)


<출처 : [네이버 지식백과] 파이썬 [Python] - 간결하고 생산성 높은 프로그래밍 언어 (용어로 보는 IT, 이지현)>
```



- 특징
  - 독립적 플랫폼
  - 공개된 언어 & 소스 공개
  - 객체지향적
  - 클래스(Class) 지원
  - C 언어와 접착 가능
- 장점
  - 문법이 간결하고 표현 구조가 인간의 사고 체계와 닮음 ▶ 학습 용이성
  - 유지 보수 및 관리 용이 
  - 풍부한 라이브러리를 통한 용도 확장 가능
  - 높은 생산성 ▶ 개발 기간이 짧음
  - 어느 운영체제에서나 사용 가능

## 설치

- [파이썬](https://www.python.org/downloads/)
  - 설치 후 패스(Path) 설정이 잘되어있는지 확인

- [파이참(PyCharm)](https://www.jetbrains.com/pycharm/download/)

### IDEL 모드

- 짧고 간단한 연산 가능
- 길고 복잡한 프로그램은 불가능
- 명령 저장 불가
- 에러 수정 번거로움

### Script 모드

- IDEL모드 창에서 `File` - `New File`
- 구조화한 명령문 입력창
- 입력 후 `Run` - `Run Module` 실행
- 결과는 IDEL모드 창에 표시
- 함수/명령을 사용해야 출력





## 기본 구조

- 들여쓰기 (Indent)

  - `>>>`프롬포트 첫 칸부터 입력
  - 쓸데없이 한 칸 띄우면 에러(Unexpected indent) 발생
  - 함수 입력 시, 자동으로 들여쓰기 적용

  

- 한 줄에 하나의 명령 작성 (세미콜론[;]으로 가능하긴 하지만 지양)



- '대문자'와 '소문자' 구분 가능

  - num / Num / NUM 변수명으로 지정 시 각자 다르게 인식

  

- [#]문자로 '주석' 



- [`l-value` = `r-value`] 구조

### 출력

#### print()

```python
print(출력내용 [, sep =''][, end =''])
```

- `sep = ` : 구분자 (여러 개의 출력값 사이를 구분짓는 문자)
- `end =` : 끝 문자
  - `''` 빈 문자열 사용 시 '이어 붙이기'



### 입력

#### input()

> 자료 입력을 요구하는 명령

```python
<변수> = input('[질문 내용]')
```



#### int()

> ''정수'' 형식 변환 명령

```python
#보통 문자열이나 실수형 데이터를 정수로 변환할 때 사용
<변수> = int()
<변수> = int(input('[질문내용]'))
```





## 변수

- 명칭(Identifier) : 변수가 다른 것과 구분 되도록 이름 붙이는 것

```python
#키워드나 내장함수, 표준 모듈명은 사용 불가
#규칙 조회
>>> import keyword
>>> keyword.kwlist
```



- *공백, 특수문자* 사용 불가
  - 보통 `_`(밑줄 문자) 사용
- <첫 글자> 숫자 사용 불가
- *''한글''*이나 *''한자'*' 사용 가능

- [동적타입_Dynamic Type] 언어
  - 실행 중에 변수 타입 바꿀 수 있음 
  - 현재 할당 값에 의해 변수 타입 정해짐

- 만들어진 후, 계속 존재하며 값 유지
  - del 명령으로 삭제





## 타입(Type)

```python
#타입 확인
print(type(<변수>/데이터값))
```



### 수치형(Integer/Float)

- 가수 E지수 활용 가능

#### 정수형(Integer type)

> 자연수를 포함해 값의 영역이 정수로 한정된 값

```python
>>>int()
```



| 진법                  | 접두 | 사용문자 | 예     |
| --------------------- | ---- | -------- | ------ |
| 16진법(he_x_adecimal) | 0x   | 0~9, a~f | 0x2f   |
| 8진법(o_ctal)         | 0o   | 0~7      | 0o17   |
| 2진법(b_inary)        | 0b   | 0, 1     | 0b1101 |

- 진법은 ASCII코드 등을 불러올 때 용이

#### 실수형(Floating-point type)

> 소수점이 포함된 값

```python
>>> float()
```



#### Round

> 반올림 명령
>
> 수치 데이터와 유효 자릿수 입력

```python
print(round(3.141592, 1))
3.1
print(round(3.141592, 4))
3.1416
print(round(123456, -3))
123000
```



### 문자형(String)

>문자로 출력되는 자료형

```python
>>> str()
```



- 따옴표는 따옴표 안에 적지 못함

  - `' "" '` (o) / `" '' "`(o) / `' " ' "`(x)

- 확장열(Escape Sequence)

  - 따옴표(인용부호) 안에 작성

  - `\`(Back Slash)와 조합하여 표기

    | 확장열 | 설명                                        |
    | ------ | ------------------------------------------- |
    | \n     | 개행                                        |
    | \t     | 탭 간격                                     |
    | \\"    | 큰 따옴표                                   |
    | \\'    | 작은 따옴표                                 |
    | \\     | 긴 문자열 연결(*코드 입력시에도 사용 가능*) |
    | \\\    | \ (문자)                                    |

- 긴 문자열 = 따옴표 3개("""[긴문자열]""")

- 전체를 '괄호'로 묶어 여러개 문자열 개행한 것을 긴 문자열로 만듦



### 논리형(Bool)

> 참(True)/거짓(False)

- Integer / Float 타입
  - 0이 아니면 - True
  - 0이면 - False



- String / Tuple / List / Dictionary 타입 
  - "비어있지 않으면" - True
  - "비어있으면" - False



### 리스트(List) / 튜플(Tuple)

> 내부 구조 생성

- 리스트 : [''문자열1" , "문자열2", "문자열3", ...]
- 튜플 : (''문자열1" , "문자열2", "문자열3", ...)

*# 튜플(Tuple)은 내부 구조 단순 & 실행 중 값 변경 불가*

*#리스트(List)는 요소 삽입, 삭제, 추가 가능*





## 대입 및 산술

### 대입 연산자

> <변수> `=` {수식} 형식



### 산술 연산자

| 연산자 | 설명                       |
| ------ | -------------------------- |
| +      | 더하기                     |
| -      | 빼기                       |
| *      | 곱하기                     |
| /      | 나누기                     |
| **     | 제곱                       |
| //     | 정수 나누기(Only 정수값만) |
| %      | 나머지                     |

- `+` 와 `*` 은 문자열에도 사용 가능

```python
#문자열 덧셈
print("대한민국" + "만세")
대한민국만세
print(str(2002) + "월드컵")
print('2002' + '월드컵')
2002월드컵
```

```python
#문자열 곱셈
#반복출력
print('만세' * 3)
만세만세만세
print('2002' * 3)
200220022002
```



### 비교연산자

| 연산자 | 설명        |
| ------ | ----------- |
| ==     | 같다        |
| !=     | 같지 않다   |
| >      | 크다        |
| <      | 작다        |
| >=     | 크거나 같다 |
| <=     | 작거나 같다 |

- 문자열의 비교

  - 알파벳순이 뒤일수록 큰 값 (첫 글자가 서로 같으면 두번째 글자로 비교_ 앞→뒤)

  ```
  apple < application < banana
