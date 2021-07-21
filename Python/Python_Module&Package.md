## 모듈

> 파이썬 코드를 저장하는 기본 단위

 편의상 스크립트를 여러 개의 파일로 나눈 것들 중 하나인데

호출될 땐, `.py`를 빼고 불림.

 자주 사용하는 기능들은 '표준 모듈'로도 제공되고 있음.



- **"직접 제작"**이 가능
  - *표준 모듈* 과 똑같은 형태로 제작 가능
  - **중복작업**을 방지하고 **재사용**이 용이한 장점

```python
#모듈 이름 = "util"
#인치(inch)를 출력 & 합계를 계산하는 함수
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

print("인치 =", INCH)	#import하자마자 위에 선언해놓은 변수 출력
print("합계 =", calcsum(10))
#import하면 "바로 인치와 합계에 대한 결과값 먼저 출력"

인치 = 2.54
합계 = 55

print(type(util.calcsum))

<class 'builtin_function_or_method'>
```

이를 모듈로서 사용한다면 이 파일은 모듈의 원본파일이라 할 수 있다.

하단의 print 함수처럼 "정상적으로 잘 작동을 하는지" 확인하거나 "import가 잘되었는지" 확인할 수 있도록 자동 실행되게 작성해 놓은 것을

​	**테스트 코드**라고 한다.



하지만 직접 사용할 땐, 변수와 함수만 가져오는 것이 효율적이고 깔끔하기 때문에

오직 원본파일 ("**____main____**")에서만 정상적으로 작동하는지만 확인하고 import 했을 땐 출력이 안되도록 if 조건문을 걸어 놓는 것이 좋다.

- 파이썬 : *<u>"먼저 실행하는 모듈"</u>*  에선 <"____name____" =  "**____main____**">
  - 어떤 모듈이던지 직접 실행이 가능하기 때문에

```python
# 원본에서만 단독으로 실행하는 환경 (main환경)에서만 출력되도록
INCH = 2.54

def calcsum(n):
    sum = 0
    for num in range(n + 1):
        sum += num
    return sum

if __name__ == "__main__" :
	print("인치 =", INCH)	
	print("합계 =", calcsum(10))
```

*#다른 모듈에서 임포트하여 사용할 때는  name은 <u>main이 아닌</u> **[모듈명]**이 된다*



#### 모듈 경로

: 모듈은 <u>*임포트하는 파일*</u>과 **같은 디렉토리**에 있어야 한다.

그래야 import문이 '이름만'으로 로드할 수 있다.

어떠한 프로젝트를 진행할 때 필요한 모듈이 다른 파일에 있을 경우, 문제가 발생한다.

 (어길시, *ModuleNotFoundError* 발생)



따라서 모듈을 사용하기 위해선 "특정 폴더"에 두어야 하고

이를 위해선 **임포트 패스(path)**에 추가시켜야 한다.



- `import sys`  +  `sys.path.append("파일 경로")`  방법 사용
  - <sys.path>sms "리스트" 형태
  - 언제든지 편집 가능





## 패키지(Package)

> 모듈을 담는 디렉토리

-  디렉토리 → "계층 구성"  ▶  모듈을 특징/기능 등에 따라 *<u>분류</u>*  가능
  - 원하는 함수 및 모듈만 콕 집어서 호출이 가능하다.



※< **[패키지] . [디렉토리] . [모듈] ** > 형태로 호출

```python
#sys모듈을 통해 모듈의 주소 등록
import sys
sys.path.append("C:/PyStudy")

#'mypack' 패키지의 'clac' 디렉토리 속 'add'모듈 호출
import mypack.calc.add
mypack.calc.add.outadd(1,2)

import mypack.report.table
mypack.report.table.outreport()
```



하지만 매번 이렇게 호출하면 번거롭다.

간략히 사용하기 위해선

- `as`를 통하여 별칭에   호출식을 저장하여  **[별칭].[함수명]** 으로 사용할 수 있음.

- `from [패키지].[디렉토리] import [모듈]`을 통해 **[모듈].[함수]**로 사용
- `from [패키지].[디렉토리].[모듈] import [함수]`을 통해 **[함수] (args)**로 사용
  - 단 함수만 호출했기 때문에 *<u>같은 모듈의 다른 함수</u>* **사용 불가**

```python
#'my1'이라는 별칭에 path 저장
import mypack.calc.add as my1
my1.outadd(1,2)

import mypack.report.table as my2
my2.outreport()

from mypack.calc import add
add.outadd(1,2)

from mypack.calc import add as abc
abc.outadd(1,2)

```





