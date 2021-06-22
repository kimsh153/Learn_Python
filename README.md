# 파이썬
### 출력
#### 파이썬에선 출력을 할 때 print()로 문장을 출력합니다
* 파이썬은 문자와 문자열을 쓸때 (' '),(" ") 둘다 가능합니다
```python
print('hello world') # hello world
print(1, 2, 3) # 1 2 3
```
* 값을 콤마(,)로 구분하면 공백 처리가 돼서 나옵니다
```python
print('Hello', 'world!') # Hello world!
```
* sep은 값 사이의 공백이 아닌 다른문자를 쓸 때 사용합니다
```python
print(1, 2, 3, sep=', ') # 1, 2, 3
print(4, 5, 6, sep=',') # 4,5,6
print('Hello', 'python', sep='') #Hellopython
print(1000, 2000, sep='x') # 1000x2000
```
* 줄바꿈을 하고싶을때엔 줄바꿈 하고싶은 문자 뒤에 \n을 붙입니다
```python
print('1\n2\n3') # 1
                 # 2
                 # 3
```
* 줄바꿈을 없애고 싶을땐 end를 사용합니다
```python
print(1, end=' ')
print(2, end=' ')
print(3)
# 1 2 3
```
---
### 세미콜론(;)
#### 다른 언어와 달리 파이썬은 다음 줄로 넘어갈때 세미콜론을 쓸 필요가 없습니다
```python
 print('hello') <- 세미콜론을 붙히지 않음
 print('world') <- 세미콜론을 붙히지 않음
 ```
* 여러 문장을 이어서 쓸땐 세미콜론을 쓰기도 합니다
```python
 print('hello'); print('world')
 ```
 ---
 ### 주석(#)
 #### 주석이 있는 문장은 실행이 되지 않습니다
 ```python
 # print('hello') 사용하지 않는 문장
 ```
 ---
 ### 들여쓰기
 #### 파이썬은 들여쓰기가 문법이여서 들여서 써야합니다
 #### ex)
 ```python
 if i == 10:
 print('i는 10입니다') <- 코드 오류가 뜸

 if i == 10:
     print('i는 10입니다')
 ```
 * 많은 문장을 들여쓰기를 할땐 같은 공백으로 해야합니다
 ```python
 if i == 10:
     print('i는')
     print('10입니다')
 ```
 ---
 ### 자료형
 #### 파이썬의 수치형
 | int | float | complex |
 |:---:|:------:|:--------:
 | **정수** | **실수** | **복소수** |
 #### 정수(int)
 ```python
 print(int(3)) # 3
 print(int(3.3)) # 3
 print(int(5 - 2)) # 3
 ```
 #### 실수(float)
 ```python
 print(float(3)) # 3.0
 print(float(3.3)) # 3.3
 print(float(5 - 2)) # 3.0
 ```
 * 객체의 자료형을 알려면 type(숫자)를 사용하면 됩니다
 ```python
 print(type(10)) # int형
 print(type(1.0)) # float형
 print(type(1+1j) # complex형
 ```
 ---
 ### 연산
 #### 사칙연산, 몫 나눗셈, 나머지 나눗셈, 거듭제곱
 #### > 사칙연산(+,-,*,/)
 ```python
 print(1 + 1) # 2
 print(5 - 2) # 3
 print(2 * 2) # 4
 print(10 / 2) # 5
 ```
 #### > 몫 나눗셈(//)
 ```python
 print(5 // 2) # 2
 print(4 // 2) # 2
 ```
 #### > 나머지 나눗셈(%)
 ```python
 print(5 % 2) # 1
 print(6 % 2) # 0
 ```
 #### > 거듭제곱(**)
 ```python
 print(2 ** 10) # 1024
 print(3 ** 5) # 243
```
---
### 변수
#### 변수란 값의 저장공간 입니다 
> 변수를 상자라고 생각하시면 편합니다
```python
x = 10
print(x) # 10
```
#### x변수에 10을 할당하고 x를 출력했습니다
* 변수를 쓸때에는 변수이름 = 값 형식으로 써야합니다
```python
10 = x <- 코드 오류가 뜸
```
#### 변수에는 숫자뿐만 아니라 문자열도 넣을 수 있습니다
```python
y = 'Hello, world!'
```
#### 변수 여러개의 값을넣어 출력
```python
a, b, c = 10, 20, 30
print(a, b, c) # 10 20 30
```
#### 변수를 여러개의 값을 모두 같은 값으로 넣어 출력
```python
a = b = c = 10
print(a, b, c) # 10 10 10
```
#### 두개 변수의 값을 서로 바꿔서 출력
```python
a, b = 10, 20
a, b = b, a
print(a, b) # 20 10
```
#### 변수로 계산을 해서 출력
```python
a = 10
b = 20
c = a + b
print(c) # 30
```
#### 변수의 값을 추가해서 출력
```python
x = 10
# x의 계산결과가 남지 않는 방법
print(x + 20) # 30
print(x) # 10
# x의 계산결과가 남는 방법 두가지
x = x + 20  
print(x) # 30
x += 20
print(x) # 50
```
* 부호 붙이기
```python
x = -10
print(+x) # -10
print(-x) # 10
```
---
### 입력
#### 입력값을 받을때에는 input()을 사용합니다
```python
input() 
x = input()
print(x)
x = input('문자열을 입력하세요: ')
# 문자열을 입력하세요: hello, world!
print(x) # hello, world!
```
#### 입력값을 2개의 변수에 저장하려면 input().split()를 사용합니다
```python
a,b = input('문자열 두개를 입력하세요').split() # 공백을 기준으로 분리
# 문자열 두개를 입력하세요: hello python
print(a) # hello
print(b) # python
```
---
### 불과 비교 연산자
#### 불은 참 또는 거짓을 나타냅니다
```python
print(True) # True
print(False) # False
```
#### 비교 연산자의 결과는 참 또는 거짓이 나옵니다
```python
print(3 > 1) # True
print(3 < 1) # False
print(3 <= 3) # True
print(3 >= 4) # False
```
#### 다양한 비교 연산자
```python
print(3 == 3) # True
```
> * 느낌표는 not 반대의 결과를 출력합니다
```python
print(3 != 1) # True
print(3 != 3) # False
print('python' == 'python') # True
print('Python' == 'python') # False
```
#### is, is not은 객체가 같은지를 비교합니다
```python
print(3 == 3.0) # 값이 같아서 True 
print(3 is 3.0) # 객체가 달라서 False
print(1 is not 1.0) # not에 객체가 달라서 True
```
* 객체의 차이 아는법(id(값))
```python
print(id(1)) # 12345678 <- 파이썬을 실행할때마다 달라짐
print(id(1.0)) # 4315123647 <- 파이썬을 실행할때마다 달라짐
```
---
### 논리연산자
#### 논리 연산자는 and, or, not 이 있습니다
#### and 연산자는 두 값이 모두 참이여야 참입니다
```python
print(True and True) # True
print(True and False) # False
print(False and True) # False
print(False and False) # False
```
#### or 연산자는 두 값중 하나만 참이여도 참입니다
```python
print(True and True) # True
print(True and False) # True
print(False and True) # True
print(False and False) # False
```
#### not 연산자는 참이면 거짓 거짓이면 참입니다
```python
print(not True) # False
print(not False) # True
```
---
### 문자열
#### 변수에 문자열 저장해서 출력하기
```python
hello = 'Hello, world!'
print(hello) # Hello, world!
hi = '안녕하세요'
print(hi) # 안녕하세요
```
* 문자열을 나타날 때 ( ''' )로 묶거나 ( """ )로 묶을 수도 있습니다
```python
hello = '''Hello, world!'''
print(hello) # Hello, world!
python = """Hello, python"""
print(python) # Hello, python
```
#### 문자열을 어려줄로 쓸 때 ( ''' )랑 ( """ )를 사용합니다
```python 
hello = '''Hello, world!
안녕하세요
python입니다'''
print(hello) # Hello, world!
             # 안녕하세요
             # python입니다
```
> 또는 ( \n )을 이용해서 줄 바꿈을 할 수 있습니다
```python
print('Hello\nPython') # Hello
                       # Python
```
#### 문자열 안에 ( ' )와 ( " )포함시키기
```python
hello = "Python isn't difficult"
print(hello) # Python isn't difficult
python = 'He said "Python is easy"'
print(python) # He said "Python is easy"
```
> 또는 ( \\ )를 사용해서 ( ' , " )를 붙힐 수 있습니다
```python
hello = 'Python isn\'t difficult'
print(hello) # Python isn't difficult'
```
---
### 리스트
#### 리스트엔 여러가지 자료형을 저장할 수 있습니다
```python
a = [10, 20, 30, 40, 50]
print(a) # [10, 20, 30, 40, 50]
person = ['james', 17, 175.3, True]
print(person) # ['james', 17, 175.3, True]
```
* 빈 리스트를 만들 때는 []또는 list를 사용할 수 있습니다
```python
a = []
print(a) # []
b = list()
print(b) # []
```
#### range를 사용하여 리스트 만들기
* range는 연속된 숫자를 생성합니다
```python
print(range(10)) # range(0, 10)
a = list(range(10))
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(range(5, 12))
print(b) # [5, 6, 7, 8, 9, 10, 11]
```
* range(시작, 끝, 증가량)
```python
c = list(range(-4, 10, 2))
print(c) # [-4, -2, 0, 2, 4, 6, 8]
d = list(range(10, 0, -1))
print(d) # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
```
### 튜플
#### 튜플은 여러가지 자료형을 저장할 수 있습니다
```python
a = (38, 21, 53, 62, 19)
print(a) # (38, 21, 53, 62, 19)
b = 38, 21, 53, 62, 19
print(b) # (38, 21, 53, 62, 19)
person = ('james', 17, 175.3, True)
print(person) # ('james', 17, 175.3, True)
```
### 리스트가 있는데 튜플을 왜 쓰나? 
* 튜플은 요소가 절대 변경 되지 않고 유지되어야 할 때 사용합니다
#### range를 사용하여 튜플 만들기
```python
a = tuple(range(!0))
print(a) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b = tuple(range(5, 12))
print(b) # (5, 6, 7, 8, 9, 10, 11)
c = turple(range(-4, 10, 2))
print(c) (-4, -2, 0, 2, 4, 6, 8)
```



##### 정리 출처 : 코딩도장
