# 문자열

- 문자열은 메모리상 개별 문자들이 일렬로 늘어선 형태
  - 개별 문자를 읽을 때 : `[ ]`(대괄호)와 문자의 위치인 **'첨자'**를 적음
  - 앞으로 셀 때 = 0~ / 뒤에서 셀 때 =  -1 ~ -n (음수 값은 점점 작아짐)



- `[ ]`괄호에 첨자 하나만 적으면 해당 위치 문자를 읽지만 Range함수 같이 시작, 끝, 증가값 지정 가능


```python
for i, name in enumerate(['body', 'foo', 'bar']):
 print(i, name)

0 body		#앞에 첨자
1 foo
2 bar
```

*# enumerate : 첨자 같이 출력*




### 슬라이스

```python
[begin : end : step]
```

```python
s = "python"
print(s[2:5])
tho
print(s[3:])	#생략 가능(양 끝값이 기준)
hon
print(s[:4])
pyth
print(s[2:-2])	#2번째 t 부터 -2인 o 직전(h) 까지
th
```



```python
#파일 이름 형식 활용
file = "20171224-104830.jpg"
print("촬영날짜 : " + file[4:6] + "월 " + file[6:8] + "일")
print("촬영시간 : " + file[9:11] + "시 " + file[11:13] + "일")
print("확장자 : " + file[-3:])

촬영날짜 : 12월 24일
촬영시간 : 10시 48분
확장자 : jpg
```



```python
#Step 역순
day = "월화수목금토일"
print(day[::2])
월수금일
print(day[::-1])
일토금목수화월
print(day[::-2])
일금수월
```



## 문자열 메서드

### 검색



### 조사



### 변경



### 분할



### 대체



