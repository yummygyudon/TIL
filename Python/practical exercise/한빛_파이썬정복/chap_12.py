#12단원 3번문제
#밑면이 8이고 높이가 5인 직각삼각형의 빗변 길이를 구하라.
from math import hypot
print(hypot(8,5))

'''
import math
print(math.hypot(8,5))
'''


#12단원 4번문제
#1994년 5월 5일 태어난 사람이 현재 며칠째 살고 있는지 계산하는 프로그램을 작성하라.
import time
now = time.localtime()
now_date = time.mktime(now)
print(now_date)


#-datetime.datetime.


#12단원 5번문제
#10에서 20사이의 난수 10개를 뽑아 출력하라.
#끝 수인 20도 포함한다.
import random
for i in range(10) :
    print(random.randint(10,20), end=' ')