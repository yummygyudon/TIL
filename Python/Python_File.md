# 파일(File)



## 입출력

### 1. 파일 쓰기

```python
open("[파일경로]", "[모드]", encoding= "[코드]")
```

디렉토리 경로를 포함할 수 있되 *<u>파일명만 있으면</u>*  **현재 디렉토리**에서 해당 파일 탐색



| 모드          | 설명                                         |
| ------------- | -------------------------------------------- |
| **r**(read)   | 파일을 읽는다_*파일이 없으면* **예외처리**   |
| **w**(write)  | 파일에 **기록**한다_*이미 있으면* **덮어씀** |
| **a**(append) | 파일에 데이터를 **추가**                     |
| **x**         | 파일에 **기록**하되 *이미 있으면* 실패       |

- 모드 뒤에는 파일의 **종류**를 지정하는 문자
  - **t**  : **텍스트**파일 ( "**rt**"가 **기본값**)
  - **b** : **이진**파일(사진, 오디오 등)

- 불러온 파일을 사용한 후, **close** 메소드 필수

```python
f = open("live.txt", "wt", encoding="UTF-8")	#기록 & 중복 시 덮어씀
print(f, type(f))
f.write("""삶이 그대를 속일지라도
슬퍼하거나 노하지 말라!
우울한 날들을 견디면
믿으라, 기쁨의 날이 오리니""")     #적은대로 그대로 개행 처리되어서 입력됨
f.close()

```

*#`try : except:` 에서 읽을 파일이 없을 경우, "FileNotFoundError"*

*# 예외처리구문에선 `close`메서드가 "Finally" 블록에 위치*





### 2. 파일 읽기

- **read**메서드
  - 변수에 할당하여 임시 복사 기능 가능



```python
f = None    		#빈 문자열(False) :  "" , '', None, (), [], {}

try:
    f = open("live.txt", "rt", encoding="UTF-8")        #encoding 안하면 UnicodeDecodeError(cp949) 발생
    print(f, type(f))
    text = f.read() #'text'변수에 해당 live.txt의 내용이 들어감
    
except FileNotFoundError as e:
    print("파일이 없습니다. - ", e)
finally:
    if f:    #혹 열고자 하는 파일 없을 경우 FileNotFoundError가 발생하는데
        print("파일 닫습니다")    #finally는 에러가 나도 수행되기때문에 .close를 쓰면 open 된 것도 없어서 오류남
        f.close()
    else :                      #f 변수가 없다(해당파일이 오픈안된다)의 경우의 출력값도 지정해줘야함
        print("열리지 않습니다..")
```



- While 루프문 활용

```python
f = open("live.txt", "rt", encoding="UTF-8")
while True:
    text = f.read(10)   # 10문자씩 읽기
    if len(text) == 0: break    #마지막 읽을 때 10문자가 안되면 반복 멈추고
    print(text, end = '$')  #10문자 마다 "$" / 마지막 부분이 몇 문자던지 동일하게 $ 붙여줌
f.close()
```



- **readline** 메서드 : 줄 단위로 **한 줄씩**읽음 / 마지막에 도달하면 *<u>빈 문자열</u>* 반환
  - 한 줄씩 문자열로 만들어 **리스트** 반환하는 형태 → *<u>Indexing</u>* 활용 가능
  - 각 줄을 자유롭게 조작 가능

```python
f = open("live.txt", "rt", encoding="UTF-8")
text = ""
line = 1
while True:
    row = f.readline()  # 한 행씩 읽기
    if not row: break	#한 행도 없을 경우 "끝"(break)
    text += str(line) + " : " + row     #행 번호 붙이기 1 : ~~ 2 : ~~. ...
    line += 1
f.close()
```



각 줄 끝에 **개행문자가 포함**되어 있으므로 (txt파일 내에서 enter를 통해 개행하였을 때 자동으로 입력됨)

```python
f = open("live.txt", "rt", encoding="UTF-8")

rows = f.readlines()  # 모든 행을 읽어서 리스트로 리턴
print(type(rows))
#<class 'list'>

for row in rows:    #리스트로 만들어서 for문 적용 / row에 개행문자도 원소 하나로 읽음
    print(row, end = '') #end = ''를 주지 않으면 행 사이에 \n 빈 줄이 하나씩 들어감
f.close()                
#txt파일 만들때 enter(행나누기)까지 적용되어서 자연스럽게 \n이 들어가기때문에 또 행을 나누면 개행문자가 2개가 되는 꼴

===========================================================================


f = open("live.txt", "rt", encoding="UTF-8")
for line in f:        # _io.TextIOWrapper 객체도 리터러블함!!
    print(line, end = '')   #개행문자는 위와 동일하게 각 행 끝에 추가적으로 들어가있어서 end=''
f.close()
```

따라서 위 두번째 방법처럼 **txt**파일은 **줄의 집합**이므로 단순히 *<u>"For 루프"</u>* 를 돌면 *<u>"한번에 한줄씩"</u>* 차례대로 읽혀짐.





### 3. 입출력 위치 지정

- 접근 방법
  - **순차** 접근 : 파일을 순서대로 읽음
  - **임의** 접근 : 입출력 위치를 **바꿔가며** 원하는 부분을 자유롭게 읽음



#### 1) tell 함수

: **현재** 입출력 위치를 조사할 때 호출



#### 2) seek 함수

: 출력 위치를 **변경**할 때

- [위치]
  - **바이트**로 계산하여 건너뜀
  - ***한글*** : **2**Byte



- [기준]
  - **0** : **처음**부터
  - **2** : **끝**부터
  - **1** : **현재 위치**

```python
seek(위치, 기준)
```

*#**Print**함수 내에서도 If~Else 조건문 사용 가능*

```python
f = open("live.txt", "rt", encoding="UTF-8", errors='ignore')  #에러무시
print("[seek기능 처리가능]" if f.seekable() else "[seek기능 처리불가]" ) 
#If문 / 참인 경우의 출력식 : 맨앞에 , 거짓인 경우의 출력식 : 맨 else 뒤에

f.seek(12,0)	#기준 0 으로 처음을 기준으로 12바이트(Byte) 건너뛴 자리로 위치 이동
text = f.read()	#6자 건너뛴 자리부터 읽음
f.close()

```



*# 파일 위치를 마음대로 옮겨가는 것도 가능하며 **음악**이나 **동영상**파일 재생위치 건너뛸 때도 **Seek함수** 사용*





### 4. 내용 추가

위에서 언급했듯이

**"a"**모드는 파일에 내용을 **추가**하는 모드로

**"w"**모드(파일이 이미 있으면 덮어쓰고 새로 만드는 모드) 에 비해 

*<u>기존 내용을 그대로 유지</u>*하고 뒤에 덧붙이며 이를 위해 파일 열자마자 *<u>입출력 위치는 가장 끝으로</u>* 감

(가장 *끝으로 가기* 때문에 **개행(\n)**문자를 활용해야 함)



```python
f = open("live.txt", "at", encoding="UTF-8")
f.write("\n\n[추가]예수의 말씀이었습니다.")			#개행문자 2개_기존 내용 사이에 빈줄 추가
f.close()

```

위 명령들은 실행할 때마다 계속 추가됨



#### with

> 파일을 확실히 닫을 때 사용

- `as` 구문으로 파일을 열어 지정 객체에 대입한 후 사용하여 **`close`** 메서드를 사용하지 않아도 *<u>with 블록</u>* 을 벗어나면 자동으로 닫힘.



```python
with open("live.txt", "rt", encoding="UTF-8") as f:
   text = f.read()
print(text)		#close 메서드를 사용하지 않아도 됨
```

- with의 사전적 의미처럼 *<u>"이 속성을 장착한 채  함께 내부명령 수행"</u>*

