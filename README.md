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
print(hello) # Python isn't difficult
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
---
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
#### range를 사용하여 튜플 만들기
```python
a = tuple(range(10))
print(a) # (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
b = tuple(range(5, 12))
print(b) # (5, 6, 7, 8, 9, 10, 11)
c = turple(range(-4, 10, 2))
print(c) # (-4, -2, 0, 2, 4, 6, 8)
```
---
### 리스트가 있는데 튜플을 왜 쓰나? 
* 튜플은 요소 변경 불가능 / 리스트는 요소 변경 가능
---
### 시퀀스 자료형
#### 리스트, 튜플, range, 문자열처럼 값이 연속적으로 이어진 자료형을 시퀀스 자료형이라고 한다
#### 시퀀스 객체중에 있는 값을 확인하는법
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(30 in a) # True
print(100 in a) # False
print(100 not in a) # True
print(30 not in a) # False
print(43 in (38, 76, 43, 62, 19) # True
print(1 in range(10)) # True
print('P' in 'Hello, Python') # True
```
#### 시퀀스 객체 연결은 + 로 할 수 있습니다
```python
a = [0, 10, 20, 30]
b = [9, 8, 7, 6]
print(a + b) # [0, 10, 20, 30, 80, 9, 8, 7, 6]
```
* range끼리는 리스트 또는 튜플을 사용해서 연결할 수 있습니다
```python
print(list(range(0, 10)) + list(range(10, 20))) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]
print(tuple(range(0, 10)) + tuple(range(10, 20))) # (0, 1, 2, 3, 4, 5, 6, ㅇ7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19)
```
* 문자열 끼리 + 로 연결할 수 있습니다
```python
print('Hello, ' + 'world!') # Hello, world!
```
#### 시퀀스 객체를 * 로 반복할 수 있습니다
```python
print([0, 10, 20] * 3) # [0, 10, 20, 0, 10, 20, 0, 10, 20]
print(list(range(0, 5, 2)) * 3) # [0, 2, 4, 0, 2, 4, 0, 2, 4]
print(tuple(range(0, 5, 2)) * 3) # (0, 2, 4, 0, 2, 4, 0, 2, 4)
```
* 문자열 끼리 * 로 반복할 수 있습니다
```python
print('Hello, ' * 3) # Hello, Hello, Hello, 
```
---
### 시퀀스 객체의 요소 구하기
#### 시퀀스 객체의 요소의 개수를 구할땐 len을 이용합니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(len(a)) # 10
b = (38, 23, 35, 92, 87)
print(len(b)) # 5
```
#### range의 숫자가 생성되는 갯수도 len으로 구할 수 있습니다
```python
print(len(range(0, 10, 2))) # 5
```
#### len을 이용하여 문자열의 갯수도 구할 수 있습니다
```python
hello = 'Hello, world!'
print(len(hello)) # 13
```
#### 시퀀스객체에 []을 붙여 객체안의 요소를 확인할 수 있습니다
```python
a = [38, 21, 53, 62, 19]
print(a[0]) # 38
print(a[2]) # 53
```
* 인덱스는 요소의 순서입니다
* []안에 인덱스를 넣어서 확인 가능합니다
#### range로 만든 객체도 인덱스로 확인할 수 있습니다
```python
r = range(0, 10, 2)
print(r[2]) # 4
```
#### 문자열도 인덱스로 문자를 확인할 수 있습니다
```python
hello = 'Hello, world!'
print(hello[7]) # w
```
#### 인덱스를 음수로 하여 반대로 접근할 수 있습니다
```python
a = [38, 21, 53, 62, 19]
print(a[-1]) # 19
print(a[-5]) # 38
r = range(0, 10, 2)
print(r[-3]) # 4
hello = 'hello, world!'
print(hello[-4]) # r
```
#### 인덱스에 접근해서 요소안에 값을 바꿀 수 있습니다
```python
a = [0, 0, 0, 0, 0]
a[0] = 81
a[1] = 15
a[2] = 77
a[3] = 52
a[4] = 36
print(a) # [81, 15, 77, 52, 36]
print(a[0]) # 81
```
#### del로 요소를 삭제할 수 있습니다
```python
a = [81, 15, 77, 52, 36]
del a[2]
print(a) [81, 15, 52, 36] 
```
#### 슬라이스는 시퀀스객체의 일정부분을 복사하는 것 입니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:4]) # [0, 10, 20, 30] 0이상 4미만까지 잘라서 새 리스트를 만듭니다
print(a[0:10]) # 0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 0이상 4미만까지 잘라서 새 리스트를 만듭니다
b = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
print(b[4:7]) # (40, 50, 60)
print(b[4:]) # (40, 50, 60, 70, 80, 90)
print(b[:7:2]) # (0, 20, 40, 60)  
```
* 리스트의 중간 부분만 가져오는방법
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[4:7]) # [40, 50, 60]
print(a[4:-1]) # [40, 50, 60, 70, 80] 4이상 -2까지 잘라서 새 리스트를 만듭니다
```
#### 인덱스의 증가폭 사용하기
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
# 2부터 인덱스를 3씩 더하면서 8미만까지 출력하는 코드
print(a[2:8:3]) # [20, 50]
# 2부터 인덱스를 3씩 더하면서 9미만까지 출력하는 코드
print(a[2:9:3]) # [20, 50, 80]
```
#### 슬라이스를 사용할때 인덱스를 생략할 수 있습니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[:7]) # [0, 10, 20, 30, 40, 50, 60]
print(a[7:] # [70, 80, 90]
print(a[:]) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[::]) # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]  
print(a[:7:2] # [0, 20, 40, 60]
print(a[7::2] # [70, 90]
print(a[::2]) # [0, 20, 40, 60, 80]
```
* 증가폭을 음수로 두면 역순으로 출력합니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[::-1]) # [90, 80, 70, 60, 50, 40, 30, 20, 10, 0]
```
#### len을 이용하여 리스트 전체를 불러오기
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(a[0:len(a)] # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90] 
print(a[:len(a)] # [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
```
#### 슬라이스로 범위를 지정하여 요소를 할당할 수 있습니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c']
print(a) # [0, 10, 'a', 'b', 'c', 50, 60, 70, 80, 90]
b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
b[2:5] = ['a']
print(b) # [0, 10, 'a', 50, 60, 70, 80, 90]
c = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
a[2:5] = ['a', 'b', 'c', 'd', 'e']
print(c) # [0, 10, 'a', 'b', 'c', 'd', 'e', 50, 60, 70, 80, 90]
d[2:8:2] = ['a', 'b', 'c']
print(d) # [0, 10, 'a', 30, 'b', 50, 'c', 70, 80, 90]
```
#### 슬라이스를 삭제하려면 (del)를 사용합니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]
print(a) # [0, 10, 50, 60, 70, 80, 90]
b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del b[2:8:2]
print(b) # [0, 10 20, 30, 50, 70, 80, 90]
```
---
### 딕셔너리
#### 딕셔너리는 키와 값으로 구분이 됩니다
* 딕셔너리를 만들때는 키:값으로 씁니다
```python
animals = {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
print(animals) # {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
```
#### 딕셔너리의 키가 중복이되면 뒤에있는 키가 저장이 됩니다
```python
animals = {'dog': 4, 'dog': 5, 'cat':3, 'giraffe':5, 'mouse': 1.0}
print(animals) # {'dog': 5, 'cat':3, 'giraffe':5, 'mouse': 1.0}
```
#### 딕셔너리의 키는 정수,실수,불,문자열이 사용가능하고 값은 모든 자료형이 사용 가능합니다
```python
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x) # {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
```
#### 빈 딕셔너리를 만들 수 있습니다
```python
a = {}
print(a) # {}
b = dict()
print(b) # {}
```
#### dict는 키=값형식으로 딕셔너리를 만듭니다 값을 넣을땐 (' '), (" ")는 빼고 만듭니다
```python
animals = dict(dog=4, cat=3, giraffe=5, mouse=1.0)
print(animals) # {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
```
#### zip은 키와 값을 순서에 맞게 묶습니다
```python
animals = dict(zip(['dog', 'cat', 'giraffe', 'mouse'], [4, 3, 5, 1.0]))
print(animals) # {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
```
* 리스트안에 튜플 나열하기
```python
animals = dict([('dog', 4), ('cat', 3), ('giraffe', 5), ('mouse', 1.0)])
print(animals) # {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
```
#### 딕셔너리에 값을 할당하려면 (딕셔너리[키] = 값)형식으로 할당합니다
```python
animals = {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
animals['dog'] = 7
animals['cat'] = 11
print(animals) # {'dog': 7, 'cat':11, 'giraffe': 5, 'mouse': 1.0}
animals['rabbit'] = 4
print(animals) # {'dog': 7, 'cat':11, 'giraffe': 5, 'mouse': 1.0, 'rabbit': 4}
```
#### 딕셔너리에 키가 있는지 확인하는법은 (print('키' in 딕셔너리)) 입니다
```python
animals = {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
print('dog' in animals) # True
print('bear' in animals) # False
print('bear' not in animals) # True
print('dog' not in animals) # False
```
#### 딕셔너리의 키의 개수를 보려면 (len)을 사용합니다
```python
animals = {'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0}
print(len(animals)) # 4
print(len({'dog': 4, 'cat':3, 'giraffe':5, 'mouse': 1.0})) # 4
```
---
### if 조건문
#### if는 조건을 쓰고 조건이 참이면 if안에있는 코드를 실행합니다
* 파이썬은 자동으로 들여쓰기를 안 해주기 때문에 들여쓰기를 꼭 해줘야 합니다
```python
x = 10
if x == 10:
    print('x는 10입니다') # x는 10입니다
y = 5
if y == 10:
    print('y는 10입니다') # 조건이 참이 아니므로 실행되지 않음
```
> x == 10 <- 조건식 
> 
> : <- 콜론 
> 
> print('x는 10입니다') <- 조건식이 참일때 실행하는 코드
#### 조건문 생략은 pass를 이용합니다
```python
x = 10
if x == 10:
    pass
```
#### 중첩 if문 쓰기
```python
x = 20
if x >= 10:
    print('x는 10이상입니다') # x는 10이상입니다
    
    if x == 15:
        print('x는 15입니다') # 실행x
    
    if x == 20:
        print('x는 20입니다') # x는 20입니다
```
#### 입력값을 if조건문에 쓰기
```python
x = int(input()) # 입력 : 10
if x == 10:
    print('x는 10입니다') # x는 10입니다
    
if x == 20:
    print('x는 20입니다') # 실행x
```
---
### else
#### else는 if조건문이 참이 아니면 실행하는 조건문입니다
```python
x = 5
if x == 10:
    print('x는 10입니다') # 실행x
else:
    print('x는 10이 아닙니다') # x는 10이 아닙니다
```
* if조건문이 참이 아니여서 else문이 실행이 됐습니다
#### if조건문의 None은 False로 간주합니다 그리고 '0'이외의 모든 수는 참입니다
```python
if None:
    print('참') # 실행x
else:
    print('거짓') # 거짓
    
if 0:
    print('참') # 실행x
else:
    print('거짓') # 거짓
    
if 1:
    print('참') # 참
else:
    print('거짓') # 실행x
```
#### if조건문의 빈 문자열은 거짓입니다
```python
if 'wow':
    print('참') # 참
else:
    print('거짓') # 실행x
    
if '':
    print('참') # 실행x
else:
    print('거짓') # 거짓
```
#### if조건문에도 사용가능한 논리 연산자
```python
x = 10
y = 20

if x == 10 and y == 20:
    print('참') # 참
else:
    print('거짓') # 실행x
a = 10
b = 10
if a == 10 or b == 20:
    print('참') # 참
else:
    print('거짓') # 실행x
```
---
### elif
#### elif조건문은 else if의 뜻이며 if문이 참이 아닐때 아래에 있는 elif조건문을 확인합니다
```python
x = 20
if x == 10:
    print('x는 10입니다') # 실행x
elif x == 20:
    print('x는 20입니다') # x는 20입니다
    
y = 10
if y == 10:
    print('y는 10입니다') # y는 10입니다
elif y == 20:
    print('y는 20입니다') # 실행x
```
* if문이 참이라면 아래있는 elif문은 컴파일하지 않고 넘어갑니다 그리고 elif문이 참이라면 그 아래있는 elif문을 넘어갑니다
---
### for 
#### for는 반복문으로 반복되는 실행을 해줍니다 
```python
for i in range(5):
    print('hello') # hello
                   # hello
                   # hello
                   # hello
                   # hello
                   
for i in range(5):
    print('hello', i) # hello 0
                      # hello 1
                      # hello 2
                      # hello 3
                      # hello 4
```
#### for문에 range(시작값, 끝값)을 정할 수 있습니다
```python
for i in range(5, 10):
    print('hello', i) # hello 5
                      # hello 6
                      # hello 7
                      # hello 8
                      # hello 9
```
#### for문에 range(시작값, 끝값, 증가값)을 정할 수 있습니다
```python
for i in range(0, 10, 2):
    print('hello', i) # hello 0
                      # hello 2
                      # hello 4
                      # hello 6
                      # hello 8
```
#### reversed는 range의 숫자의 순서를 반대로 뒤집을 수 있습니다
```python
for i in reversed(range(5)):
    print('hello', i) # hello 4
                      # hello 3
                      # hello 2
                      # hello 1
                      # hello 0
```
#### range를 응용해서 입력한 값 만큼 반복하는 for문 만들기
```python
cnt = int(input('반복할 횟수를 입력하세요: '))

for i in range(cnt):
    print('hello', cnt)
```
#### for문에 range대신 리스트를 넣으면 리스트의 요소를 꺼내면서 반복합니다
```python
a = [10, 20, 30, 40, 50]
for i in a:
    print(i)
```
#### 튜플도 마찬가지로 튜플의 요소를 꺼내면서 반복합니다
```python
animals = ('cat', 'dog', 'mouse')
for animal in animals:
    print(animal)
```
#### 문자열도 시퀀스 객체이므로 for문으로 한글자씩 빼낼 수 있습니다
```python
for letter in 'Python':
    print(letter, end=' ')
```
---
### while
#### while도 for와 비슷한 반복문입니다
```python
i = 0
while i < 100:
    print('hello')
    i += 1
```
> i = 0 <- 초기식
>
> i < 100 <- 조건식
>
> print('hello') <- 반복할 코드
>
> i += 1 <- 변화식
#### random모듈을 이용하여 while반복문의 반복 횟수를 정하지 않고 반복하기
```python
import random
random.randint(1, 6)

i = 0
while i != 3:
    i = random.randint(1, 6)
    print(i)
```
> random.randint(1, 6) <- 1과 6사이의 난수를 생성
> 
> while i != 3 <- i가 3이 아닐때까지 반복하기

* while 반복문은 반복 횟수가 정해져 있지 않을 때 유용합니다
---
### break, continue
#### break를 사용하여 반복문을 끝내기
```python
i = 0
while True:
    print(i)
    i += 1
    if i == 10:
        break
```
> if i == 10: <- 만약 i가 10이라면
>
> break <- 반복문 끝내기

#### continue를 사용하여 다음 코드 건너뛰기
```python
for i in range(100):
    if i % 3 == 0:
        continue
    print(i)
```
> if i % 3 == 0: <- 만약 i가 3으로 나눈 나머지가 0이라면
>
> continue <- 다음 코드 건너뛰기
---
### 별 출력
#### 이중for문을 이용하여 계단식 별 출력하기
```python
for i in range(5):
    for j in range(i + 1):
        print('*', end='')
    print()
```
---
### 리스트, 튜플 응용
#### 리스트에 요소 하나 추가하기
```python
a = [10, 20, 30]
a.append(500)
print(a) # [10, 20, 30, 500]
print(len(a)) # 4
```
#### 리스트안에 리스트 추가하기
```python
a = [10, 20, 30]
a.append([500, 600])
print(a) # [10, 20, 30, [500, 600]]
print(len(a)) # 4
```
> a.append([500, 600]) <- 요소 하나를 리스트에 끝에 추가 하는 것이기 때문에 len의 길이가 4이다
#### 리스트를 확장하기
```python
a = [10, 20, 30]
a.extend([500, 600])
print(a) # [10, 20, 30, 500, 600]
print(len(a)) # 5
```
#### 리스트의 특정 인덱스에 요소 추가하기
```python
a = [10, 20, 30]
a.insert(2, 500)
print(a) # [10, 20, 500, 30]
print(len(a)) # 4
```
> a.insert(2, 500) <- a.insert(몇번째 인덱스, 값
#### 리스트의 특정 인덱스의 요소 삭제하기
```python
a = [10, 20, 30]
a.pop()
print(a) # [10, 20]

b = [10, 20, 30]
b.pop(1)
print(b) # [10, 30]
```
#### 리스트의 특정 값을 찾아서 삭제하기
```python
a = [10, 20, 30]
a.remove(20)
print(a) # [10, 30]

b = [10, 20, 30, 20]
b.remove(20)
print(b) # [10, 30, 20]
```
* remove는 가장 처음에 있는 값 삭제합니다
#### 리스트에서 특정 값의 인덱스 구하기
```python
a = [10, 20, 30, 15, 20, 40]
print(a.index(20)) # 1
```
* index는 가장 처음에 있는 값의 인덱스를 구합니다
#### 리스트에서 특정 값의 개수 구하기
```python
a = [10, 20, 30, 15, 20, 40]
print(a.count(20)) # 2
```
#### 리스트의 순서를 뒤집기
```python
a = [10, 20, 30, 15, 20, 40]
a.reverse()
print(a) # [40, 20, 15, 30, 20, 10]
```
#### 리스트의 요소 정렬하기
```python
a = [10, 20, 30, 15, 20, 40]
a.sort()
print(a) # [10, 15, 20, 20, 30, 40]
```
#### 리스트의 모든 요소 삭제하기
```python
a = [10, 20, 30]
a.clear()
print(a) # []
```
#### del로 모든 요소 삭제하기
```python
a = [10, 20, 30]
del a[:]
print(a) # []
```
#### 리스트를 슬라이스로 조작하기
```python
a = [10, 20, 30]
a[len(a):] = [500]
print(a) # [10, 20, 30, 500]
```
#### 리스트 표현식 사용하기
```python
a = [i for i in range(10)]
print(a) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
b = list(i for i in range(10))
print(b) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```
> a = [i for i in range(10)] <- range(10) <- 숫자 10개를 생성, i for i <- 숫자를 하나씩 꺼냄, i <- i 리스트 생성
```python
c = [i + 5 for i in range(10)] # 0부터 9까지 숫자를 생성하면서 값에 5를 더하여 리스트 생성
print(c) # [5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
d = [i * 2 for i in range(10)] # 0부터 9까지 숫자를 생성하면서 값에 2를 곱하여 리스트 생성
print(d) # [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
```
#### 리스트 표현식에서 if조건문 사용하기
```python
a = [i for i in range(10) if i % 2 == 0] # 0~9 숫자 사이에서 2의 배수인 숫자로 리스트 생성
print(a) # [0, 2, 4, 6, 8]
```
#### 리스트의 가장 작은 수, 가장 큰 수, 합계 구하기
```python
a = [38, 21, 53, 62, 19]
print(min(a)) # 19
print(max(a)) # 62
print(sum(a)) # 193
```
#### 튜플에서 특정 값의 인덱스 구하기
```python
a = (38, 21, 53, 62, 19, 53)
print(a.index(53)) # 2
```
#### 튜플에서 특정 값의 개수 구하기
```python
a = (10, 20, 30, 15, 20, 40)
print(a.count(20)) # 2
```
#### for 반복문으로 튜플 요소 출력하기
```python
a = (38, 21, 53, 62, 19)
for i in a:
    print(i, end=' ') # 38 21 53 62 19
```
#### 튜플 표현식 사용하기
```python
a = tuple(i for i in range(10) if i % 2 == 0)
print(a) # (0, 2, 4, 6, 8)
```
#### 튜플에서 가장 작은 수, 가장 큰 수, 합계 구하기
```python
a = (38, 21, 53, 62, 19)
print(min(a)) # 19
print(max(a)) # 62
print(sum(a)) # 193
```
---
### 2차원 리스트
#### 2차원 리스트 만들기
```python
a = [[10, 20], [30, 40], [50, 60]]
print(a) # [[10, 20], [30, 40], [50, 60]]
```
#### 2차원 리스트의 인덱스 접근하기
```python
a = [[10, 20], [30, 40], [50, 60]]
print(a[0][0]) # 10
print(a[1][1]) # 40
a[0][1] = 1000
print(a) # [[10, 1000], [30, 40], [50, 60]]
```
* 톱니형 리스트
> 가로 세로의 크기가 불규칙한 2차원리스트를 만들 수 
```python
a = [[10, 20],
     [500, 600, 700],
     [9],
     [30, 40],
     [8],
     [800, 900, 1000]]
```
#### 2차원 리스트의 요소를 하나하나 꺼내기
```python
a = [[10, 20], [30, 40], [50, 60]]
for x, y in a:
    print(x, y) # 10 20
                # 30 40
                # 50 60
```
> [10, 20] 중에 10 > x, 20 > y로 넘어간 것 입니다
```python
a = [[10, 20], [30, 40], [50, 60]]

for i in a:
    for j in i:
        print(j, end=' ')
    print()
```
> 출력
> 
> 10 20
>
> 30 40
>
> 50 60

> for i in a <- [10, 20] 리스트를 꺼냄
>
> for j in i <- [10], [20] 리스트를 꺼냄
* for문과 range를 사용하여 2차원 리스트의 요소 꺼내기
```python
a = [[10, 20], [30, 40], [50, 60]]

for i in range(len(a)):           # 세로 크기
    for j in range(len(a[i])):    # 가로 크기
        print(a[i][j], end=' ')
    print()
```
#### while을 이용하여 2차원 리스트의 요소 꺼내기
```python
a = [[10, 20], [30, 40], [50, 60]]

i = 0
while i < len(a):
    x, y = a[i]
    print(x, y)
    i += 1
```
#### for반복문으로 1차원 리스트 만들기
```python
a = []
for i in range(10):
    a.append(0) # append로 요소 추가
print(a) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
#### for반복문으로 2차원 리스트 만들기
```python
a = []

for i in range(3):
    line = []
    for j in range(2):
        line.append(0)
    a.append(line)
print(a) # [[0, 0], [0, 0], [0, 0]]
```
> line = [] <- 안쪽 리스트로 사용할 빈 리스트 만들기
>
> line.append(0) <- 안쪽 리스트에 0 추가
>
> a.append(line) <- 전체 리스트에 안쪽 리스트를 추가
#### 리스트 표현식으로 2차원 리스트 만들기
```python
a = [[0 for j in range(2)] for i in range(3)]
print(a) # [[0, 0], [0, 0], [0, 0]] 
```
#### 2차원 톱니형 리스트 만들기
```python
a = [3, 1, 3, 2, 5] # 가로 크기를 지정한 리스트
b = []

for i in a:
    line = []
    for j in range(i):
        line.append(0)
    b.append(line)
    
print(b) # [[0, 0, 0], [0], [0, 0, 0], [0, 0], [0, 0, 0, 0, 0]]
```
> for i in a: <- 리스트의 크기만큼 반복
>
> for j in range(i): <- a리스트의 숫자만큼 반복
#### 2차원 리스트의 값 할당, 복사하기
```python
a = [[10, 20], [30, 40]]
b = a
b[0][0] = 500
print(a) # [[500, 20], [30, 40]]
print(b) # [[500, 20], [30, 40]]
```
#### 2차원 리스트의 값 할당, 복사를 copy로 하기
```python
a = [[10, 20], [30, 40]]
b = a.copy()
b[0][0] = 500
print(a) # [[500, 20], [30, 40]]
print(b) # [[500, 20], [30, 40]]
```
#### 리스트a를 b가 복사해고 b의 요소를 변경해도 a에 영향을 미치지 않게 하기
```python
a = [[10, 20], [30, 40]]
import copy
b = copy.deepcopy(a)
b[0][0] = 500
print(a) # [[10, 20], [30, 40]]
print(b) # [[500, 20], [30, 40]]
```
---
### 문자열 응용하기
#### 문자열 바꾸기
```python
s = 'Hello, world!'
s = s.replace('world!', 'Python')
print(s) # 'Hello, Python'
```
#### 문자 바꾸기
```python
table = str.maketrans('aeiou', '12345')
print('apple'.translate(table)) # '1ppl2'
```
#### 문자열 분리하기
```python
print('apple pear grape pineapple orange'.split()) # ['apple', 'pear', 'grape', 'pineapple', 'orange']
```
```python
print('apple, pear, grape, pineapple, orange'.split(', ')) # ['apple', 'pear', 'grape', 'pineapple', 'orange']
```
* split()는 공백은 기준으로 문자열을 분리하여 리스트를 만듭니다
#### 구분자 문자열과 문자열 리스트 연결하기
```python
print(' '.join(['apple', 'pear', 'grape', 'pineapple', 'orange'])) 
# 'apple pear grape pineapple orange'
```
* join은 구분자 문자열과 문자열 리스트의 요소를 연결하여 문자열로 만듭니다
```python
print('-'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
# 'apple-pear-grape-pineapple-orange'
```
#### 문자열의 소문자를 대문자로 바꾸기
```python
print('python'.upper())
# 'PYTHON'
```
* upper()는 문자열의 문자를 모두 대문자로 바꿉니다. 만약 문자열 안에 대문자가 있다면 그대로 유지됩니다. 
#### 문자열의 대문자를 소문자로 바꾸기
```python
print('PYTHON'.lower())
# 'python'
```
* lower()는 문자열의 문자를 모두 소문자로 바꿉니다. 만약 문자열 안에 소문자가 있다면 그대로 유지됩니다.
#### 문자열의 왼쪽 공백 삭제하기
```python
print('    Python    '.lstrip())
# 'Python    '
```
#### 문자열의 오른쪽 공백 삭제하기
```python
print('    Python    '.rstrip())
# '    Python'
```
#### 양쪽 공백 삭제하기
```python
print('    Python    '.strip())
# 'Python'
```
#### 왼쪽의 특정 문자 삭제하기
```python
', python.'.lstrip(', .')
# ' python.'
```
#### 오른쪽의 특정 문자 삭제하기
```python
', python.'.rstrip(',.')
# ', python'
```
#### 양쪽의 특정 문자 삭제하기
```python
', python.'.strip(',.')
# ' python'
```
#### 문자열을 왼쪽으로 정렬하기
```python
'python'.ljust(10)
# 'python    '
```
* ljust(길이)는 문자열을 지정된 길이로 만든 뒤 남은 공간은 공백으로 채웁니다.
#### 참고 : 코딩도장(https://dojang.io/course/view.php?id=7)
