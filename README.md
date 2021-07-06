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
#### 슬라이스를 삭제하려면 del를 사용합니다
```python
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del a[2:5]
print(a) # [0, 10, 50, 60, 70, 80, 90]
b = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
del b[2:8:2]
print(b) # [0, 10 20, 30, 50, 70, 80, 90]
```
### 딕셔너리
#### 딕셔너리는 키와 값으로 구분이 됩니다
* 딕셔너리를 만들때는 키:값으로 씁니다
```python
lux = {'health': 490, 'mana':334, 'melee':550, 'armor': 18.72}
print(lux) # {'health': 490, 'mana':334, 'melee':550, 'armor': 18.72}
```
#### 딕셔너리의 키가 중복이되면 뒤에있는 키가 저장이 됩니다
```python
lux = {'health': 490, 'health':800, 'mana':334, 'melee':550, 'armor': 18.72}
print(lux) # {'health': 800, 'mana':334, 'melee':550, 'armor': 18.72}
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
#### dict는 키=값형식으로 딕셔너리를 만듭니다 값을 넣을땐 ' '," "는 빼고 만듭니다
```python
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1) # {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
#### zip은 키와 값을 순서에 맞게 묶습니다
```python
lux2=dict(zip(['health', 'mana', 'melee', 'armor'], [490, 334, 550, 18.72]))
print(lux2) # {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
* 리스트안에 튜플 나열하기
```python
lux3=dict([('health', 490), ('mana', 334), ('melee', 550), ('armor', 18.72)])
print(lux3) # {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
```
##### 정리 출처 : 코딩도장
