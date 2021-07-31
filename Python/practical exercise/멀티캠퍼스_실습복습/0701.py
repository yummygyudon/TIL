'''
[ 실습 1 ]
1. forLab1.py 라는 소스를 만든다.
2. for문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. print() 함수로 숫자를 하나만 출력해야 한다.

    1 2 3 4 5 6 7 8 9 10
'''
for num in range(1,11) :
    print(num, end= '')
print()


'''
[ 실습 2 ]
1. forLab2.py 라는 소스를 만든다.
2. for 문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. print() 함수로 숫자를 하나만 출력해야 한다.

    0
    1
    2
    3
    4
'''
for num2 in range(5) :
    print(num2)
print()


'''
[ 실습 3 ]
1. forLab3.py 라는 소스를 만든다.
2. for 문을 사용해서 다음과 같은 결과가 출력되도록 구현한다. ‘@’ 기호문자 하나를 출력하는 print() 함수 호출을 5번 반복한다.
    @
    @
    @
    @
    @
'''
for i in range(5) :
    print("@")
print()


'''
[ 실습 4 ]
1. forLab4.py 라는 소스를 만든다.
2. 다음과 같은 결과가 출력되도록 구현한다.

    9 : 홀수
    8 : 짝수
    7 : 홀수
    6 : 짝수
    5 : 홀수
    4 : 짝수
'''
for a in range(9,4,-1) :
    if a % 2 != 0 :
        print(f"{a} : 홀수")
    else :
        print(f"{a} : 짝수")



'''
[ 실습 5 ]
1. forLab5.py 라는 소스를 만든다.
2. 1부터 10사이의 난수를 추출하여 start 변수에 저장한다.
3. 30부터 40사이의 난수를 추출하여 end 변수에 저장한다.
4. start 부터 end 까지의 숫자들 중에서 짝수의 합을 구해 다음 형식으로 출력한다.

    X 부터 Y 까지의 짝수의 합 : ZZ
'''
import random
start = random.randint(1,10)
end = random.randint(30, 40)

sum = 0
for i in range(start, end+1) :
    if i % 2 == 0 :
        sum += i
print(f"{start} 부터 {end} 까지의 짝수의 합 : {sum}")



'''
[ 실습 6 ]
1. forLab6.py 라는 소스를 만든다.
2. evenNum 변수와 oddNum 변수의 값을 0으로 대입한다.
3. 1 부터 100 까지의 값 중에서 
   짝수의 합은 evenNum 에 누적하고 
   홀수의 합은 oddNum 에 누적한다.
4. 수행 결과는 다음과 같이 출력한다.

    1부터 100까지의 숫자들 중에서 
    짝수의 합은 XXX 이고 
    홀수의 합은 YYY 이다.
'''
evenNum = 0
oddNum = 0
for num in range(1,101) :
    if num % 2 == 0 :
        evenNum += num
    else :
        oddNum += num
print(f"1부터 100까지의 숫자들 중에서 \n짝수의 합은 {evenNum}이고 \n홀수의 합은 {oddNum}이다.")
