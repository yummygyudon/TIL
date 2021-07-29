#14단원 1번문제
#사용자로부터 이름을 입력받아 name.txt 파일에 기록하라.
f = open("name.txt", "wt")
f.write("""안녕하십니까
벌써 프로그래밍을 배운지 1달째가 되었습니다.
앞으로 열심히 하겠습니다.""")
f.close()

#14단원 1번문제
#name.txt 파일을 읽어 화면으로 출력하라. 편의상 예외 처리 구문은 생략한다.
f = open("name.txt", "rt")
text = f.read()
print(text)
f.close()