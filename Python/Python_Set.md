# 세트 (Set)

- 세트 생성
  - 비어있는 셋(Set)은 잘 만들지 않음.
    - Dictionary에서 `{}`로 빈 Dict 만들 수 있기 때문에 *Set에서는 {} 사용 불가*
    - set() 로 빈 세트

```python
a = set()
b = set([1, 2, 3, 3,4])	#리스트로 세트 만들기
c = {1, 4, 5, 6, 1, 4}
d = set([1, 2, 'Pen', 'Cap', 'Plate'])
e = set((10,))	# set((<요소> ,)) = {<요소>,}	튜플로 세트 만들기
f = {100,}		# 하나의 요소로만 생성할 땐 쉼표(,) 

print('a - ', type(a), a)
a -  <class 'set'> set()

print('b - ', type(b), b)
b -  <class 'set'> {1, 2, 3, 4}

print('c - ', type(c), c)
c -  <class 'set'> {1, 4, 5, 6}

print('d - ', type(d), d)
d -  <class 'set'> {1, 2, 'Cap', 'Pen', 'Plate'}

print('e - ', type(e), e)
e -  <class 'set'> {10}

print('f - ', type(f), f)
f -  <class 'set'> {100}

```



- interable 가능하기때문에 데이터 추출 가능
  - 순서 상관없이 **무작위로 추출**되는 데이터 구조
  - 같은 값 **중복**은 **불가**

```python
for data in d :
    print(data)
    
1
2
Cap
Pen
Plate
```



- 데이터 구조 변환

  - 튜플

  ```python
  
  ```

  

  - 리스트

  ```python
  ```

  

- 튜플과 다르게 수정 가능 (가변)