#7단원 6번문제
#세 개의 정수를 전달받아 평균값을 구해 리턴하는 함수를 작성해라.
def num_mean (a, b, c) :
    sum = int(a)+int(b)+int(c)
    return sum / 3

#7단원 7번문제
#임의 개수의 인수를 전달받아 가장 큰 숫자를 찾아 리턴하는 함수를 작성하라.
def biggest_num(*args) :
    num = max(args)
    return num

print(biggest_num(1, 10, 8, 12, 98))

