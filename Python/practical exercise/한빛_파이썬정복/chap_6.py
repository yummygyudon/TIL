#6단원 1번문제
#while문을 사용하여 1에서 200까지 모든 3의 배수 합계를 계산해라.

num = 3
sum = 0
while num <= 200 :
    sum += num
    num += 3
print(sum)

#6단원 5번문제
#for문으로 1에서 10까지 출력하되 3의 배수는 건너뛰는 예제를 작성해라.

for num in range(1,11) :
    if (num % 3 != 0) :
        print(num)
    else :
        pass

for num in range(1, 11) :
    if num % 3 == 0 :
        continue
    print(num)

#6단원 6번문제
#이중루프로 직각삼각형을 출력하라.

for i in range(1, 11) :
    print("*" * i)

for i in range(1, 11) :
    print(" " * (10-i), end="")
    print("*" * i, )

for i in range(1, 11) :
    for a in range(10-i) :
        print(" ", end="")
    for b in range(i) :
        print("*", end="")
    print("")

#6단원 7번문제
#이중루프로 이등변 삼각형을 출력하라

for i in range(1, 11) :
    for a in range(10-i) :
        print(" ", end="")
    for b in range(i*2 -1) :
        print("*" , end="")
    print("")