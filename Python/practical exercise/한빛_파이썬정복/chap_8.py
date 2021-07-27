#8단원 2번문제
#s="universe" 일 때 한 행에 한글자씩 출력하는 코드를 작성하라.
s="universe"

for i in range(len(s)) :
    print(s[i])

#8단원 5번문제
#domain 변수는 임의의 웹 주소를 가지고 있다. 이 도메인이 .kr로 끝나는 한국 도메인인지 확인하는 코드를 작성하라.

domain = input("사이트 주소 : ")

'''if ".kr" in domain :
    print("한국 도메인 입니다.")
else :
    print("한국 도메인이 아닙니다.")
'''
if domain.endswith("kr") :
    print("한국 도메인입니다.")

#8단원 6번문제
#sosi문자열에 "태연, 서연, 수영" 이름이 저장되어 있다. 각 가수의 이름을 추출하여 "사랑해와 함께 출력하라.

sosi = "태연, 서연, 수영"
sosi_mem = sosi.split(", ")
for mem in sosi_mem :
    print(mem + " 사랑해")

#8단원 7번문제
#"아침에 커피로 시작하고 밥 먹고 커피 마시고 자기 전에도 커피를 마신다." 문자열에서 모든 커피를 우유로 바꾸어 출력하라.
daily ="아침에 커피로 시작하고 밥 먹고 커피 마시고 자기 전에도 커피를 마신다."
daily_milk = daily.replace("커피", "우유")
print(daily_milk)

#8단원 8번문제
#임의의 주민등록번호 901231-1914983 에서 생년과 성별을 추출하여 "90년생 남자" 라는 결과를 출력하라.
p_num = "901231-1914983"
birth = p_num[0:2]
if int(p_num[7]) % 2 == 0 :
    print(birth + "년생 여자")
else:
    print(birth + "년생 남자")

if int(p_num[7]) % 2 == 0 :
    gender = "여자"
else :
    gender = "남자"

print(f"{birth}년생 {gender}")

#8단원 9번문제
#sum변수에 총점 356이 저장되어 있고, avg변수에 평균 89.2785가 저장되어 있다.
#두 변수의 값을 한 문자열로 조립하여 출력하되 평균은 반올림하여 소수점 2자리만 출력하라.
sum = 356
avg = 89.2785
print(f"총점 : {sum}, 평균 : {avg:.2f}")