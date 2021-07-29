#13장 3번문제
#두 개의 정수를 입력받아 나눈 결과를 출력하되 0으로 나누기 예외를 처리하라.
try:
    num1 = int(input("첫 번째 숫자 : "))
    num2 = int(input("두 번째 숫자 : "))
    div = num1 / num2
except ZeroDivisionError :
    print("0으로는 나눌 수 없습니다.")
else:
    print("첫 번째 값을 두 번째 값으로 나누겠습니다.")
    print(f"결과값 : {div}")