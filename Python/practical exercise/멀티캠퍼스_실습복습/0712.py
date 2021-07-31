'''
1. 파일명 : funcLab1.py
2. 구현해야 하는 함수 사양
   함수명 : print_book_title
   매개변수 : 없음
   리턴값 : 없음
   기능 : 파이썬 교재명을 화면에 출력
   함수명 : print_book_publisher
   매개변수 : 없음
   리턴값 : 없음
   기능 : 파이썬 교재의 출판사명을 화면에 출력
3. print_book_title() 함수를 3회 호출하고 print_book_publisher() 함수를 5회 호출한다.
'''
def print_book_title() :
    for _ in range(3) :
        print("파이썬 정복")

def print_book_publisher() :
    for _ in range(5) :
        print("한빛 미디어")


print(print_book_title())
print(print_book_publisher())

'''
[ 실습 2 ]
1. 파일명 : funcLab2.py
2. 구현해야 하는 함수 사양
   함수명 : get_book_title
   매개변수 : 없음
   리턴값 : 있음
   기능 : 파이썬 교재명을 리턴한다.
   함수명 : get_book_publisher
   매개변수 : 없음
   리턴값 : 있음
   기능 : 파이썬 교재의 출판사명을 리턴한다.
3. get_book_title() 함수를 호출하고 리턴되는 결과를 name 변수에 저장한 다음 name 변수의 값을 2회 
  출력한다. get_book_publisher() 함수를  호출하고 리턴되는 결과를 화면에 출력한다.
'''
def get_book_title() :
    return "파이썬 정복"

def get_book_publisher() :
    return"힌빛미디어"

name = get_book_title()

for _ in range(2) :
    print(name)

print(get_book_publisher())


'''
[ 실습 3 ]
1. 파일명 : funcLab3.py
2. 구현해야 하는 함수 사양
   함수명 : expr
   매개변수 : 숫자 2개와 연산자 1개
   리턴값 : 연산 결과 또는  None
   기능 : 전달된 두 개의 숫자에 대해서 전달된 연산을 처리하고 그 결과를 리턴한다.
            연산자는 +, -, *, / 만 처리하며 그 외의 연산자는 연산을 하지 않고 None 을 리턴한다.
3. 숫자 2개와 연산자 1개를 전달하여 expr() 이라는 함수를 호출한 다음 리턴 결과가 None 이면
   수행 불가 를 출력하고 그렇지 않으면 연산결과 : XX 를 출력한다.
'''
def expr(num1, num2, cal) :
    if cal == "+" :
        return num1 + num2
    elif cal == "-" :
        return num1 - num2
    elif cal == "*" :
        return num1 * num2
    elif cal == "/" :
        return num1 / num2
    else:
        return None

expr = expr(6,2,"*")
if expr == None :
    print("수행 불가")
else :
    print("연산결과 : ", expr)

'''
[ 실습 4 ]
1. 파일명 : funcLab4.py
2. 구현해야 하는 함수 사양
   함수명 : print_triangle
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         2 전달시
         *
         * *
         5 전달시
         *
         **
         ***
         ****
         *****
         전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는 처리하지 
         않고 그냥 리턴한다.
3. 숫자를 다양하게 지정해서 print_triangle() 함수를 호출해 본다.

'''
def print_triangle(x) :
    if 10 >= x >= 1 :
        for i in range(1,x+1) :
            print(i*"*")
    else:
        return
print_triangle(10)

'''
[ 실습 5 ]
1. 파일명 : funcLab5.py
2. 구현해야 하는 함수 사양
   함수명 : print_triangle
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자 개수로 구성되는 삼각형을 출력한다. 출력 형식은 다음과 같다.
         2 전달시
         @@
         @ 
         5 전달시
         @@@@@
         @@@@
         @@@
         @@
         @
         전달되는 아규먼트 값은 1~10으로 제한한다. 1~10 이외의 값이 전달된 경우에는 처리하지 
         않는다.

3. 숫자를 다양하게 지정해서 print_triangle() 함수를 호출해 본다.
'''
def print_triangle(a) :
    if a > 10 or a < 1 :
        return
    for i in range(a, 0, -1):
        print("@" * i)

print_triangle(8)


'''
[ 실습 6 ]
1. 파일명 : funcLab6.py
2. 구현해야 하는 함수 사양
   함수명 : print_gugudan
   매개변수 : 1개
   리턴값 : 없음
   기능 : 전달된 숫자의 구구단을 출력한다.
         - 전달된 아규먼트가 int 타입인지 채크하고 int 타입이 아니면 그냥 리턴한다.
         - 전달된 아규먼트가 1~9 사이인지 채크하고 아니면 그냥 리턴한다.
         - 그 외의 경우에는 해당 단의 구구단을 행 단위로 출력한다.\\
3. 숫자를 다양하게 지정해서 print_ gugudan() 함수를 호출해 본다.
'''
def print_gugudan(gugu_num1) :
    if type(gugu_num1) != int :
        return
    elif  10 < gugu_num1 or 0 > gugu_num1 :
        return
    else :
        for i in range(1, 10) :
            print(f"{gugu_num1} * {i} : {gugu_num1*i}")

print_gugudan(9)

'''
[ 실습 7 ]
1. 파일명 : funcLab7.py
2. 구현해야 하는 함수 사양
   함수명 : differtwovalue

   매개변수 :  2개
   리턴값 : 연산 결과
   기능 : 전달받은 2개의 데이터 중에서 큰 값에서 작은 값의 차를 리턴 두 값이 동일하면 0 을 리턴한다.
           10, 20 이 전달되면 ---> 10 리턴
           20, 5 가 전달되면 ---> 15 리턴
           5, 30 이 전달되면 ---> 25 리턴
           6, 3 이 전달되면  ---> 3 리턴

3. 1부터 30 사이의 난수 2 개를 추출하여 2번에서 구현된 함수를 호출하고 결과를 다음 형식으로 출력한다.
   "X 와 Y 의 차는 W 입니다."
   ----> 5 회 반복
'''
def differtwovalue(num1, num2) :
    if num1 == num2 :
        return 0
    else :
        z = abs(num1 - num2)
        return z

import random

for i in range(5) :
    a = random.randint(1, 30)
    b = random.randint(1, 30)
    differtwovalue(a, b)
    print(a, "와 ", b, "의 차는 ", differtwovalue(a, b), " 입니다.")