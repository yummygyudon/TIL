#9단원 1번문제
#score 리스트에 성적값 8개를 저장하고 총점과 평균을 구해 출력하라.
score = [91, 82, 73, 84, 100, 67, 88, 92]

sum = 0
num = 0
for i in score :
    sum += i
    num += 1
print(f"총점 : {sum}")
print(f"평균 : {sum/num}")


#9단원 2번문제
#score = [88, 95, 70, 100, 99] 리스트에서 2번 학생의 성적을 0점으로 변경하라
score = [88, 95, 70, 100, 99]
score[1] = 0
print(score)


#9단원 3번문제
#리스트 컴프리헨션 문법을 사용하여 1에서 100 사이의 짝수로 구성된 리스트를 생성하라.
even_num = [i for i in range(1,101) if i % 2 ==0]
print(even_num)


#9단원 4번문제
#[n*n for n in range(1, 10) if n % 3 == 0] 구문을 평이한 루프와 조건문, 연산식으로 풀어서 작성하라.
num = []
for n in range(1, 10) :
    if n % 3 != 0 :
        continue
    else :
        num.append(n*n)
print(num)
for i in num :
    print(i, end=' ')
print()


#9단원 7번문제
#사용자로부터 5개의 성적을 입력받아 리스트에 저장한 후 오름차순으로 정렬하여 출력하라.
score = []
for i in range(5) :
    num = int(input("성적을 차례대로 입력하시오. : "))
    score.append(num)
score.sort()
print(score)


