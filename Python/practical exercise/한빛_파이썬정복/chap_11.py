#11단원 1번문제
#1~10 정수의 리스트 a와 각 정수의 제곱의 리스트 b를 만든 후
#두 리스트를 합쳐 사전으로 만들고 6의 제곱을 검색하여 출력하라
num=[]
double_num =[]
for i in range(1,11) :
    num.append(i)
for int in num :
    double_num.append(int*int)

num_lst = dict(zip(num, double_num))

print(num_lst[6])


#11단원 2번문제
#price 리스트에 상품 가격 다섯 개가 저장되어 있다. 모든 상품의 가격을 20% 세일한 값으로 출력하라.
import random
price = []
for i in range(5) :
    product = random.randint(1000,3000)
    sell_price = round(product)
    price.append(sell_price)

sale_price = [round(before*0.8) for before in price]
for num in sale_price :
    print(f"세일가 : {num} 원", end=' / ')
print()
