'''
[ 실습 1 ]
파일명 : fileioLab1.py

다음 내용을 생성해서 c:/iotest/today.txt 라는 파일에 저장한다.
c:/iotest 디렉토리의 존재여부를 채크하고 존재하지 않으면 새로이 생성한다.
출력 내용은 다음과 같습니다.

오늘은 2021년 07월 19일입니다.
오늘은 월요일입니다.
나는 X요일에 태어났습니다.

파일에 위의 내용을 저장한 다음에 화면에는“저장이 완료되었습니다.”를 출력한다.
'''
import datetime
import calendar

now = datetime.datetime.now()
year = now.year
month = now.month
date = now.day

day = ["월", "화", "수", "목", "금", "토", "일"]
birtday= calendar.weekday(1999, 12, 4)

f= open("today.txt", "wt", encoding="utf-8")
f.write(f"""오늘은 {now.year}년 {now.month}월 {now.day}일입니다.
오늘은 {day[calendar.weekday(now.year, now.month, now.day)]}요일입니다.
나는 {day[birtday]}요일에 태어났습니다.""")
f.close()
print("저장이 완료되었습니다.")

'''
[ 실습 2 ]
파일명 : fileioLab2.py

제공된 sample.txt 파일을 읽고 sample_yyyy_mm_dd.txt 파일에 그대로 출력하는 프로그램을
구현한다. 이 파일은 append 모드로 오픈하여 여러 번 테스트하면 sample.txt 파일의 내용이 
sample_yyyy_mm_dd.txt 파일에 계속 추가되게 한다.

위의 내용을 파일에 저장하는 기능이 정상적으로 수행되면 화면에 “저장이 완료되었습니다.”
'''
sample = open("sample.txt", "rt", encoding="utf-8")
sample_data = sample.read()
sample.close()
f = open(f"sample_{now.year}.{now.month:02d}.{now.day:02d}.txt", "at", encoding="utf-8")
f.write(sample_data+f"\n\n확인날짜 : {now.year}년 {now.month}월 {now.day}일\n\n")
f.close()
print("수정내역 업데이트 되었습니다.")

'''
[ 실습 3 ]
파일명 : stLab1.py

프로그램 수행 중간에 년도와 월을 입력받아 해당년과 월의 달력을 출력한다. 
년도와 월은 숫자로 입력받아야 하며 숫자가 입력되지 않아서 발생하는 에러를 대비해야 
한다.  ValueError 처리를 통해서 숫자가 입력되지 않은 경우에는 메시지를 내보내고
다시 입력받는다. 숫자 입력을 잘 할때까지…… 
년도와 월이 제대로 입력되면 해당 년월의 달력을 출력한다.
'''
while True :
        x = int(input("달력을 출력하고 싶은 연도를 입력하시오 :"))
        y = int(input("원하는 월을 입력하시오 : "))
        try :
            year = int(x)
            month = int(y)
            print(calendar.month(x, y))
            break
        except (IndexError, ValueError) as e :
            print(e)

'''
[ 실습 4 ]
파일명 : fileioLab3.py

제공된 yesterday.txt 파일을 읽고 이 문서에 "Yesterday" 가 몇 개 들어 있는지 개수를 세어서 출력한다. (이 때 대소문자는 구분하지 않는다.)
FileNotFoundError 발생시 파일을 읽을 수 없어요 를 출력하고 종료한다.
에러가 발생하지 않으면 	Number of a Word 'Yesterday' X 를 출력하고 종료한다. 
(참고 : X는 9인걸루 예측됨)
에러 발생 여부와 관계없이 수행완료!! 를 출력하고 종료한다.
(try-except-else-finally 를 모두 사용해서 해결한다.)

'''
try :
    with open("yesterday.txt") as file :
        yesterday = file.read()
        count = yesterday.lower().count("yesterday")
except FileNotFoundError :
    print("파일을 읽을 수 없어요.")
else :
    print("Number of a word 'Yesterday'", count)
finally :
    print("수행완료!!")