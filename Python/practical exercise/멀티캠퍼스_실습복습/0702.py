'''
[ 실습1 ]
1. whileLab1.py 라는 소스를 생성한다.
2. 5부터 10사이의 난수를 추출한다.
3. 1부터 추출된 숫자값까지의 각 숫자들의 제곱값을 행단위로 출력한다.
   ===>  7이 추출되면
 1 -> 1
     	2 -> 4
     	3 -> 9
     	4 -> 16
     	5 -> 25
     	6 -> 36
     	7 -> 49
'''
import random
num = random.randint(5, 10)
i = 1
while i <= num :
    print(f"{i} -> {i*i}")
    i+=1


'''
[ 실습2 ]
1. whileLab2.py 라는 소스를 생성한다.
2. 다음 기능을 반복해서 수행하는 프로그램을 구현하며 반복문으로 while 문을 사용한다.
3. 반복 처리해야 하는 기능은 다음과 같다.

    1부터 6사이의 두 개 난수를 추출하여 각각 pairNum1, pairNum2 에 저장한다.
    추출된 두 개의 숫자가 서로 다르면 값의 크기를 비교하여 
    "pairNum1이 pairNum2 보다 크다." 또는 "pairNum1이 pairNum2 보다 작다." 
    출력한다.
    
    추출된 두 개의 숫자가 동일하면 "게임 끝"이라는 메시지를 출력하고 종료한다
'''
pairNum1 = random.randint(1, 6)
pairNum2 = random.randint(1, 6)

while True:
    pairNum1 = random.randint(1, 6)
    pairNum2 = random.randint(1, 6)
    if pairNum1 > pairNum2 :
        print("pairNum1이 pairNum2보다 크다.")
        continue
    elif pairNum1 < pairNum2:
        print("pairNum1이 pairNum2보다 작다.")
        continue
    else:
        print("게임 끝")
        break

'''
[ 실습3 ] - while 문으로 무한루프 처리
1. whileLab3.py 라는 소스를 생성한다.
2. 0부터 30사이의 난수를 추출한다.
    추출된 숫자가 1이면 'A', 2 이면 'B', ... 26이면 'Z' 를 출력하는데
    계속 난수 추출과 출력을 반복하다가 난수가 0이 추출되거나
    27~30이 추출되면 반복을 끝낸다.

    반복하는 동안 출력형식 :  	
            B(2)
    		A(1)
			D(4)
			  :
    마지막에는 "수행횟수는 x 번입니다"를 출력하고 종료한다. 수행 횟수는 출력을 기준으로 계산한다
'''
i = 0
while True:
    num2 = random.randint(0, 30)
    if 27 > num2 > 0 :
        print(f"{chr(64+num2)}({num2})")
        i += 1
    elif num2 == 0 or num2 >= 27 :
        print(f"수행횟수는 {i} 번입니다.")
        break


'''
[ 실습4 ] - while 문으로 무한루프 처리
1. whileLab4py 라는 소스를 생성한다.
2. 반복 처리해야 하는 기능은 다음과 같다.
	사용자로부터 월에 해당하는 숫자를 하나 입력 받는다.
	입력된 숫자가 1~12 사이의 값이면
       	12, 1, 2의 경우엔 x월은 겨울
	3, 4, 5의 경우엔 x월은 봄
	6, 7, 8의 경우엔 x월은 여름
	9, 10, 11의 경우엔 x월은 가을
       을 출력한다.
       입력된 숫자가 1~12 사이가 아니면 1~12 사이의 값을 입력하세요! 를 출력하고
       종료한다.
'''
while True:
    month = int(input("월 : "))
    if month >12 or month < 0 :
        print("1~12 사이의 값을 입력하세요!")
        break
    elif month <= 2 or month == 12 :
        print(f"{month}월은 겨울")
    elif month <= 5 and month >= 3 :
        print(f"{month}월은 봄")
    elif month <= 8 and month >= 6 :
        print(f"{month}월은 여름")
    else :
        print(f"{month}월은 가을")


'''
[ 실습5 ] - while 문으로 무한루프 처리
1. whileLab5py 라는 소스를 생성한다.
2. 반복 처리해야 하는 기능은 다음과 같다.
	- 사용자로부터 문자열을 하나 입력받아 word 라는 변수에 저장한다.
	- word 변수에 저장된 데이터의 길이를 추출하여(문자열 길이는 len() 이라는 함수를 사용한다.) 
	  wordlength 라는 변수에 저장한다.
         - wordlength 라는 변수에 할당된 값에 따라서 다음 기능을 수행한다.
         - wordlength 라는 변수의 값이 0 이면 반복을 종료한다.
         - wordlength 라는 변수의 값이 5 이상이고 8 이하이면 아무 기능도 수행하지 않고 입력받는 
           기능부터 다시 수행한다.
         - wordlength 라는 변수의 값이 5 미만이면 문자열의 앞과 뒤에 “*” 기호를 붙여서 result 변수에 
           저장한다.
         - wordlength 라는 변수의 값이 8 초과이면 문자열의 앞과 뒤에 “$” 기호를 붙여서 result 변수에 
           저장한다.
         result 변수의 값을 다음 형식으로 출력한다. 
		유효한 입력 결과 : ........
       
3. 다음은 이 프로그램의 수행 결과이다.

문자열을 입력하시오 : abc
유효한 입력 결과 : 
문자열을 입력하시오 : abcdef
유효한 입력 결과 : 
문자열을 입력하시오 : abcdefghi
유효한 입력 결과 : 
문자열을 입력하시오 : a
유효한 입력 결과 : 
문자열을 입력하시오 : 가나다라
유효한 입력 결과 : 
문자열을 입력하시오 : ㅋㅋㅋㅋㅋㅋ
문자열을 입력하시오 : 파이썬공부를열심히합시다
유효한 입력 결과 : 
문자열을 입력하시오 :

'''
while True:
    word = input("문자열을 입력하시오 : ")
    wordlength = len(word)
    if wordlength == 0 :
        break
    elif 5 <= wordlength <= 8 :
        continue
    elif wordlength < 5 :
        result = f"*{word}*"
    elif wordlength > 8 :
        result = f"${word}$"
    print("유효한 입력 결과 : ", result)

'''
[ 실습6 ] - while 문으로 무한루프 처리
1. whileLab6py 라는 소스를 생성한다.
2. 반복 처리해야 하는 기능은 다음과 같다.
- 숫자를 하나 입력받는다.
- 입력된 숫자가 0 이면 “종료”라는 메시지를 출력하고 수행을 종료한다.
- 입력된 숫자가 -10 보다 작거나 10보다 크면 입력 받는 것부터 다시 시작한다.
- 입력된 숫자가 양수이면 “입력값 : x” 행을 출력한 다음 행에 1부터 입력된 숫자 값까지의 곱한 
  결과를 출력한다.
- 입력된 숫자가 음수이면 양수로 변경하여 “입력값(부호변경) : x” 를 출력한 다음 행에 1부터 입력된 
  숫자 값까지의 곱한 결과를 출력한다.

5 가 입력되면 
	입력값 : 5 
	120

-3 이 입력되면
	입력값(부호변경) : 3
    6

0 이 입력되면
	종료
'''
while True :
    num3 = int(input("숫자를 입력하시오 : "))
    if num3 == 0 :
        print("종료")
        break
    elif num3 > 10 or num3 < -10 :
        continue
    elif num3 > 0 :
        print(f"입력값 : {num3}")
        i = 0
        for i in range(1, num3) :
            i *= i
        print(i)
    elif num3 < 0 and num3 >= -10:
        print(f"입력값(부호변경) : {abs(num3)}")
        i = 0
        for i in range(1, abs(num3)):
            i *= i
        print(i)