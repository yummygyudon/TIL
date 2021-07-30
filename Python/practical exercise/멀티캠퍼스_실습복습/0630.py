'''
[ 실습1 ]
1. num 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
2. 입력받은 숫자가 10보다 큰 경우에만 ‘OK’ 라는 문자열을 출력한다.
'''
num = int(input("숫자를 입력하세요 : "))

if num >10 :
    print("OK")


'''
[ 실습2 ]
1. color_name 이라는 변수에 사용자로부터 칼라 이름을 하나 입력받는다.
2. 입력받은 칼라명이 red 이면 ‘#ff0000’라는 문자열을 출력한다.
  입력받은 칼라명이 red 가 아니면 ‘#000000’라는 문자열을 출력한다.
'''
color_name = input("색을 입력하시오 : ")

if color_name != "red" :
    print("#000000")
else :
    print("#ff0000")


'''
[ 실습3 ]
1. grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.  
조건 평가 시 and 연산자를 사용해서 해결한다.
2. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   x 학년은 저학년입니다.
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   x 학년은 고학년입니다.
'''
import random
grade = random.randint(1,6)

if grade >= 1 and grade <= 3 :
    print(f"{grade}학년은 저학년입니다.")
else :
    print(f"{grade}학년은 고학년입니다.")


'''
[ 실습4 ]
1. grade 라는 변수에 1 부터 6 사이의 숫자를 랜덤으로 추출하고 저장한다.  
조건 평가 시 or 연산자를 사용해서 해결한다.
2. grade 의 값이 1 또는 2 또는 3이면 다음 결과를 출력한다.
   x 학년은 저학년입니다.
   grade 의 값이 4 또는 5 또는 6이면 다음 결과를 출력한다.
   x 학년은 고학년입니다.
'''
if grade == 1 or grade == 2 or grade == 3 :
    print(f"{grade}학년은 저학년입니다.")
elif grade == 4 or grade == 5 or grade == 6:
    print(f"{grade}학년은 고학년입니다.")


'''
[ 실습5 ]
(1) score 라는 변수에 0 부터 100 사이의 숫자를 랜덤으로 추출하고 저장한다.
(2) score 변수의 값의 크기에 따라서 다음의 내용을 출력한다.  print() 함수를 5개 사용하여 해결한다.
   score 변수의 값이 90~100 이면   xx점은 A등급입니다.
   score 변수의 값이 80~89 이면   xx점은 B등급입니다.
   score 변수의 값이 70~79 이면   xx점은 C등급입니다.
   score 변수의 값이 60~69 이면   xx점은 D등급입니다.
   score 변수의 값이 0~59 이면   xx점은 F등급입니다.
'''
score = random.randint(0, 100)

if score >= 90 :
    print(f"{score}점은 A등급입니다.")
elif score >= 80 :
    print(f"{score}점은 B등급입니다.")
elif score >= 70 :
    print(f"{score}점은 C등급입니다.")
elif score >= 60:
    print(f"{score}점은 D등급입니다.")
else :
    print(f"{score}점은 F등급입니다.")


'''
[ 실습6 ]
실습 5의 문제를 한 개의 print()로 해결하라.
'''
score2 = random.randint(0, 100)

if score2 >= 90 :
    level = "A"
elif score2 >= 80 :
    level = "B"
elif score2 >= 70 :
    level = "C"
elif score2 >= 60:
    level = "D"
else :
    level = "F"

print(f"{score2}점은 {level}등급입니다.")


'''
[ 실습7 ]
1. num2 이라는 변수에 사용자로부터 숫자 하나를 입력받는다.
  입력 받을 때의 메시지- 1부터 10사이의 숫자를 하나 입력하세요 :
2. 입력 받은 숫자가 1부터 10사이의 숫자가 아니면 다음과 같이 처리한다.
  
  1부터 10사이의 숫자를 하나 입력하세요 :
  1부터 10사이의 값이 아닙니다.
  
3. 입력 받은 숫자가 1부터 10사이의 숫자이면 다음과 같이 처리한다.
 
 1부터 10사이의 숫자를 하나 입력하세요 : 
   : 홀수 / 짝수
'''
num2 = int(input("1부터 10사이의 숫자를 입력하시오 : "))

if 10 >= num2 >= 1 :
    if num2 % 2 == 0 :
        print(f"{num2} : 짝수")
    else :
        print(f"{num2} : 홀수")
else :
    print("1부터 10사이의 값이 아닙니다.")


'''
[ 실습8 ]
1. oper_num 이라는 변수에 1부터 10사이의 랜덤값을 추출하여 대입한다.
2. 추출된 값이 1이거나 6이면 300 과 50 의 덧셈 연산을 처리한다.
   추출된 값이 2이거나 7이면 300 과 50 의 뺄셈 연산을 처리한다.
   추출된 값이 3이거나 8이면 300 과 50 의 곱센 연산을 처리한다.
   추출된 값이 4이거나 9이면 300 과 50 의 나눗셈 연산을 처리한다.
   추출된 값이 5이거나 10이면 300 과 50 의 나머지 연산을 처리한다.
3. 출력 형식(단, 결과를 출력하는 수행문장은 한 번만 구현한다.)
    결과값 : XX
'''
oper_num = random.randint(1, 10)

if oper_num == 1 or oper_num == 6 :
    cal = 300 + 50
elif oper_num == 2 or oper_num == 7 :
    cal = 300 - 50
elif oper_num == 3 or oper_num == 8 :
    cal = 300 * 50
elif oper_num == 4 or oper_num == 9 :
    cal = 300 / 50
else :
    cal = 300 % 50

print("결과값 : ", cal)

