# 공부한 곳 출처:파이썬 코딩 도장
import turtle as t
import copy
import pickle
import math
from abc import *
import random


# for 별찍기
def first():
    for i in range(5):
        for j in range(5):
            print('*', end='')
        print()
    print()
    for i in range(3):
        for j in range(7):
            print('*', end='')
        print()
    print()

    for i in range(5):
        for j in range(5):
            if j <= i:
                print('*', end='')
        print()
    print()

    for i in range(5):
        for j in range(5):
            if j == i:
                print('*', end='')
            else:
                print(' ', end='')
        print()


# Turtle 그래픽
def turtle():
    t.shape('turtle')
    t.speed('fastest')

    for i in range(300):
        t.fd(i)
        t.right(91)
    t.mainloop()


# List
def List():
    a = [10, 20, 30, 50, 9]
    a.append([500, 600])
    a.extend([500, 600])
    a.insert(2, 500)
    a.insert(len(a), 500)
    a[1:1] = [500, 600]
    a.pop(1)
    del a[1]
    a.reverse()
    a.sort()
    print(a)
    print(len(a))


# 2D List
def TwoD_List():
    a = [[10, 20], [30, 40], [50, 60]]
    print(a[0][0])
    print(a[0][1])
    print(a[2][1])
    for x, y in a:
        print(x, y)
    for i in a:
        for j in i:
            print(j, end=' ')
        print()
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        print()
    i = 0
    while i < len(a):
        x, y = a[i]
        print(x, y)
        i += 1
    a = []
    for i in range(3):
        line = []
        for j in range(2):
            line.append(0)
        a.append(line)
    a = [[0 for j in range(2)] for i in range(3)]
    print(a)
    a = [3, 1, 2, 7, 5]
    b = []
    for i in a:
        line = []
        for j in range(i):
            line.append(0)
        b.append(line)
    a = [[0] * i for i in [3, 1, 2, 7, 5]]
    print(a)


# string
def string():
    s = 'Hello, world'
    s = s.replace('world', 'Python')
    print(s)
    table = str.maketrans('aeiou', '12345')
    print('apple'.translate(table))
    print('apple pear grape pineapple orange'.split())
    print('.'.join(['apple', 'pear', 'grape', 'pineapple', 'orange']))
    print('python'.upper())
    print('PYTHON'.lower())
    print('     python      '.lstrip())
    print('     python      '.rstrip())
    print('     python      '.strip())
    print(', python.'.lstrip(',.'))
    print(', python.'.rstrip(',.'))
    print(', python.'.strip(',.'))
    print('python'.ljust(10))
    print('python'.rjust(10))
    print('python'.center(10))
    print('python'.rjust(10).upper())
    print('35'.zfill(4))
    print('apple pineapple'.find('pl'))
    print('apple pineapple'.rfind('pl'))
    print('apple pineapple'.index('pl'))
    print('apple pineapple'.rindex('pl'))
    print('apple pineapple'.count('pl'))
    print('I am %s.' % 'james')
    name = 'maria'
    print('I am %s.' % name)
    print('I am %d years old.' % 20)
    print('%.2f' % 2.3)
    print('%10s' % 'python')
    print('Today is %d %s.' % (3, 'April'))
    print('Hello, {0}'.format('world'))
    print('Hello, {0}'.format(100))
    print('Hello, {0} {2} {1}'.format('Python', 'Script', 3.6))
    print('Hello, {} {} {}'.format('Python', 'Script', 3.6))
    print('Hello, {language} {version} '.format(language='Python', version=3.6))
    language = 'python'
    version = 3.6
    print(f'Hello, {language} {version}')
    print('{{ {0} }}'.format('python'))
    print('{0:>10}'.format('python'))
    print('{0:0>10}'.format(15))
    print('{0:x>10}'.format(15))


# Dictionary
def Dictionary():
    x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    x.setdefault('e')
    x.setdefault('f', 100)
    x.update(a=90)
    x.update(e=50)
    x.update(a=400, f=60)
    x.popitem()
    print(x.get('a'))
    print(x.items())
    print(x.keys())
    print(x.values())
    print(x)
    y = {1: 'one', 2: 'two'}
    y.update({1: 'ONE', 3: 'THREE'})
    y.update([[2, 'TWO'], [4, 'FOUR']])
    print(y)
    y.clear()
    keys = ['a', 'b', 'c', 'd']
    y = dict.fromkeys(keys, 100)
    print(y)
    x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    for i in x:
        print(i, end=' ')
    print()
    for key, value in x.items():
        print(key, value)
    for key in x.keys():
        print(key, end=' ')
    print()
    for value in x.values():
        print(value, end=' ')
    print()
    keys = ['a', 'b', 'c', 'd']
    x = {key: value for key, value in dict.fromkeys(keys).items()}
    print(x)
    print({key: 0 for key in dict.fromkeys(['a', 'b', 'c', 'd']).keys()})
    print({value: 0 for value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.values()})
    print({value: key for key, value in {'a': 10, 'b': 20, 'c': 30, 'd': 40}.items()})
    x = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
    x = {key: value for key, value in x.items() if value != 20}
    print(x)
    terrestrial_planet = {
        'Mercury': {
            'mean_radius': 2439.7,
            'mass': 3.3022E+23,
            'orbital_period': 87.969
        },
        'Venus': {
            'mean_radius': 6371.0,
            'mass': 5.97219E+24,
            'orbital_period': 365.25641,
        },
        'Mars': {
            'mean_radius': 33389.5,
            'mass': 6.4185E+23,
            'orbital_period': 686.9600,
        }
    }
    print(terrestrial_planet['Venus']['mean_radius'])
    x = {'a': 0, 'b': 0, 'c': 0, 'd': 0}
    y = x
    y['a'] = 99
    print(y is x)
    print(x['a'])
    print(y['a'])
    z = x.copy()
    print(x is z)
    print(x == z)
    z['b'] = 99
    print(x['b'])
    print(z['b'])
    x = {'a': {'python': '2.7'}, 'b': {'python': '3.6'}}
    y = x.copy()
    y['a']['python'] = '2.7.15'
    print(x, y, sep='\n')
    y = copy.deepcopy(x)
    y['a']['python'] = '2.7.15'
    print(x, y, sep='\n')


# set
def Learn_set():
    fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
    print(fruits)
    fruits = {'orange', 'orange', 'cherry'}
    print(fruits)
    fruits = {'strawberry', 'grape', 'orange', 'pineapple', 'cherry'}
    print('orange' in fruits)
    print('peach' in fruits)
    print('orange' not in fruits)
    print('peach' not in fruits)
    a = set('apple')
    print(a)
    b = set(range(5))
    print(b)
    c = set()
    print(c)
    c = {}
    print(type(c))
    c = set()
    print(type(c))
    print(set('안녕하세요'))
    a = frozenset(range(10))
    print(a)
    a = {1, 2, 3, 4}
    b = {3, 4, 5, 6}
    print(a | b)
    print(set.union(a, b))
    print(a & b)
    print(set.intersection(a, b))
    print(a - b)
    print(set.difference(a, b))
    print(a ^ b)
    print(set.symmetric_difference(a, b))
    a = {1, 2, 3, 4}
    a |= {5}
    print(a)
    a = {1, 2, 3, 4}
    a.update({5})
    print(a)
    a = {1, 2, 3, 4}
    a &= {0, 1, 2, 3, 4}
    print(a)
    a = {1, 2, 3, 4}
    a.intersection_update({0, 1, 2, 3, 4})
    print(a)
    a = {1, 2, 3, 4}
    a -= {3}
    print(a)
    a = {1, 2, 3, 4}
    a.difference_update({3})
    print(a)
    a = {1, 2, 3, 4}
    a ^= {3, 4, 5, 6}
    print(a)
    a = {1, 2, 3, 4}
    a.symmetric_difference_update({3, 4, 5, 6})
    print(a)
    a = {1, 2, 3, 4}
    print(a <= {1, 2, 3, 4})
    print(a.issubset({1, 2, 3, 4, 5}))
    a = {1, 2, 3, 4}
    print(a < {1, 2, 3, 4, 5})
    a = {1, 2, 3, 4}
    print(a >= {1, 2, 3, 4})
    print(a.issuperset({1, 2, 3, 4}))
    a = {1, 2, 3, 4}
    print(a > {1, 2, 3})
    a = {1, 2, 3, 4}
    print(a == {1, 2, 3, 4})
    print(a == {4, 2, 1, 3})
    a = {1, 2, 3, 4}
    print(a != {1, 2, 3})
    a = {1, 2, 3, 4}
    print(a.isdisjoint({5, 6, 7, 8}))
    print(a.isdisjoint({3, 4, 5, 6}))
    a = {1, 2, 3, 4}
    a.add(5)
    print(a)
    a.remove(3)
    print(a)
    a.discard(2)
    print(a)
    a.discard(3)
    print(a)
    a = {1, 2, 3, 4}
    a.pop()
    print(a)
    a.clear()
    print(a)
    a = {1, 2, 3, 4, 5}
    print(len(a))
    a = {1, 2, 3, 4, 5}
    for i in a:
        print(a)
    a = {1, 2, 3, 4}
    for i in a:
        print(a)
    a = {1, 2, 3, 4}
    b = a
    print(a is b)
    b.add(5)
    print(a)
    print(b)
    a = {1, 2, 3, 4}
    b = a.copy()
    print(a is b)
    print(a == b)
    a = {1, 2, 3, 4}
    b = a.copy()
    b.add(5)
    print(a)
    print(b)
    a = {1, 2, 3, 4}
    for i in a:
        print(i)
    for i in {1, 2, 3, 4}:
        print(i)
    a = (i for i in 'apple')
    print(a)
    a = {i for i in 'pineapple' if i not in 'apl'}
    print(a)


# file
def file():
    file = open('hello.txt', 'w')
    file.write('Hello, world!')
    file.close()

    file = open('hello.txt', 'r')
    s = file.read()
    print(s)
    file.close()

    with open('hello.txt', 'r')as file:
        s = file.read()
        print(s)
    with open('hello.txt', 'w')as file:
        for i in range(3):
            file.write('Hello, world! {0}\n'.format(i))
    lines = ['안녕하세요.\n', '파이썬\n', '코딩 도장입니다.\n']
    with open('hello.txt', 'w') as file:
        file.writelines(lines)
    with open('hello.txt', 'r') as file:
        lines = file.readlines()
        print(lines)
    with open('hello.txt', 'r') as file:
        line = None
        while line != '':
            line = file.readline()
            print(line.strip('\n'))
    with open('hello.txt', 'r') as file:
        for line in file:
            print(line.strip('\n'))
    file = open('hello.txt', 'r')
    a, b, c = file
    print(a, b, c)

    name = 'james'
    age = 17
    address = '서울시 서초구 반포동'
    scores = {'korean': 90, 'english': 95, 'mathematics': 85, 'science': 82}
    with open('james.p', 'wb') as file:
        pickle.dump(name, file)
        pickle.dump(age, file)
        pickle.dump(address, file)
        pickle.dump(scores, file)

    with open('james.p', 'rb') as file:
        name = pickle.load(file)
        age = pickle.load(file)
        address = pickle.load(file)
        scores = pickle.load(file)
        print(name)
        print(age)
        print(address)
        print(scores)


# palindrome
def palindrome():
    word = input('단어를 입력하세요: ')
    is_palindrome = True
    for i in range(len(word) // 2):
        if word[i] != word[-1 - i]:
            is_palindrome = False
            break

    print(is_palindrome)
    print(word == word[::-1])
    word = 'level'
    print(list(word) == list(reversed(word)))
    print(list(word))
    print(list(reversed(word)))
    print(word == ''.join(reversed(word)))
    print(word)
    print(''.join(reversed(word)))
    text = 'Hello'
    for i in range(len(text) - 1):
        print(text[i], text[i + 1], sep='')
    text = 'this is python script'
    words = text.split()
    for i in range(len(words) - 1):
        print(words[i], words[i + 1])
    text = 'hello'
    two_gram = zip(text, text[1:])
    for i in two_gram:
        print(i[0], i[1], sep='')
    text = 'hello'
    print(list(zip(text, text[1:])))
    text = 'this is python script'
    words = text.split()
    print(list(zip(words, words[1:])))
    text = 'hello'
    print([text[i:] for i in range(3)])
    print(list(zip(['hello', 'ello', 'llo'])))
    print(list(zip(*['hello', 'ello', 'llo'])))
    print(list(zip(*[text[i:] for i in range(3)])))


# function
def function():
    def hello():
        print('Hello, world!')

    def pas():
        pass

    def add(a, b):
        """독스트링 이 함수는 a와 b를 더한 뒤 결과를 변환하는 함수입니다."""
        return a + b

    hello()
    x = add(10, 20)
    print(x)
    print(add.__doc__)

    def add(a, b):
        return a + b

    x = add(10, 20)
    print(x)
    print(add(10, 20))

    def one():
        return 1

    x = one()
    print(x)

    def not_ten(a):
        if a == 10:
            return
        print(a, '입니다', sep='')

    print(not_ten(5))
    print(not_ten(10))

    def add_sub(a, b):
        return a + b, a - b

    x, y = add_sub(10, 20)
    print(x)
    print(y)
    x = add_sub(10, 20)
    print(x)
    print(1, 2)

    def mul(a, b):
        c = a * b
        return c

    def add(a, b):
        c = a + b
        print(c)
        d = mul(a, b)
        print(d)

    x = 10
    y = 20
    add(x, y)
    print(10, 20, 30)

    # def print_numbers(a, b, c):
    #    print(a)
    #    print(b)
    #    print(c)

    # print_numbers(10, 20, 30)
    # x = [10, 20, 30]
    # print_numbers(*x)
    # print_numbers(*[10, 20, 30])

    def print_numbers(*args):
        for arg in args:
            print(arg)

    print_numbers(10)
    print_numbers(10, 20, 30, 40)
    x = [10]
    print_numbers(*x)
    y = [10, 20, 30, 40]
    print_numbers(*y)

    def personal_info(name, age, address):
        print('이름: ', name)
        print('나이: ', age)
        print('주소: ', address)

    # personal_info('홍길동', 30, '서울시 용산구 이촌동')
    # personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
    # personal_info(age=30, address='서울시 용산구 이촌동', name='홍길동')
    # print(10, 20, 30, sep=':', end='')  # sep, end 키워드 인수
    x = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
    personal_info(**x)
    personal_info(**{'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'})
    personal_info(*x)

    def personal_info(**kwargs):
        for kw, arg in kwargs.items():
            print(kw, ': ', arg, sep='')

    personal_info(name='홍길동')
    personal_info(name='홍길동', age=30, address='서울시 용산구 이촌동')
    x = {'name': '홍길동'}
    personal_info(**x)
    y = {'name': '홍길동', 'age': 30, 'address': '서울시 용산구 이촌동'}
    personal_info(**y)

    def personal_info(**kwargs):
        if 'name' in kwargs:  # in으로 딕셔너리 안에 특정 키가 있는지 확인
            print('이름: ', kwargs['name'])  # 이름이 들어감
        if 'age' in kwargs:
            print('나이: ', kwargs['age'])
        if 'address' in kwargs:
            print('주소: ', kwargs['address'])

    def personal_info(name, age, address='비공개'):
        print('이름: ', name)
        print('나이: ', age)
        print('주소: ', address)

    personal_info('홍길동', 30)
    personal_info('홍길동', 30, '서울시 용산구 이촌동')

    # def personal_info(name, address='비공개', age):
    #     print('이름: ',name)
    #     print('나이: ', age)
    #     print('주소: ', address) #이렇게 하면 실행 안됨 위치를 잘 맞춰야함


def return_function():
    def hello():  # 무한반복 위험
        print('Hello, world!')
        hello()

    hello()

    def hello(count):
        if count == 0:
            return

        print('Hello, world!', count)

        count -= 1
        hello(count)

    hello(5)

    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n - 1)

    print(factorial(5))


# lambda
def learn_lambda():
    def plus_ten(n):
        return n + 10

    print(plus_ten(1))
    plus_te = lambda z: z + 10
    plus_te(1)
    print((lambda z: z + 10)(1))
    # print((lambda x: y = 10; x + y)(1)) 람다 표현식 안에서는 변수를 만들 수 없다
    y = 10
    print((lambda z: z + y)(1))

    def plus_ten(n):
        return n + 10

    print(list(map(plus_ten, [1, 2, 3])))
    print(list(map(lambda z: z + 10, [1, 2, 3])))
    print((lambda: 1)())
    x = 10
    print((lambda: x)())
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(lambda x: str(x) if x % 3 == 0 else x, a)))  # 람다 표현식에선 if를 쓰면 else를 반드시 써야한다
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(lambda x: str(x) if x == 1 else float(x) if x == 2 else x + 10, a)))

    def f(x):
        if x == 1:
            return str(x)
        elif x == 2:
            return float(x)
        else:
            return x + 10

    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(list(map(f, a)))
    a = [1, 2, 3, 4, 5]
    b = [2, 4, 6, 8, 10]
    print(list(map(lambda x, y: x * y, a, b)))

    def f(x):
        return 5 < x < 10

    a = [8, 3, 2, 10, 15, 7, 1, 9, 0, 11]
    print(list(filter(f, a)))  # [i for i in a if i > 5 and i < 10]
    print(list(filter(lambda x: 5 < x < 10, a)))

    def f(x, y):
        return x + y

    a = [1, 2, 3, 4, 5]
    from functools import reduce

    print(reduce(f, a))

    a = [1, 2, 3, 4, 5]
    from functools import reduce
    print(reduce(lambda x, y: x + y, a))
    # x = a[0]
    # for i in range(len(a) - 1):
    #     x = x + a[i + 1]
    #
    # print(x)


# Class
def Class():
    class Person:
        def __init__(self):
            self.hello = '안녕하세요'

        def greeting(self):
            print(self.hello)

    james = Person()
    james.greeting()

    class Person:
        def __init__(self, name, age, address):
            self.hello = '안녕하세요'
            self.name = name
            self.age = age
            self.address = address

        def greeting(self):
            print('{0} 저는 {1}입니다.'.format(self.hello, self.name))

    maria = Person('마리아', 20, '서울시 서초구 반포동')
    maria.greeting()

    print('이름: ', maria.name)
    print('나이: ', maria.age)
    print('주소: ', maria.address)

    class Person:
        def __init__(self, name, age, address, wallet):
            self.name = name
            self.age = age
            self.address = address
            self.__wallet = wallet

        def pay(self, amount):
            if amount > self.__wallet:
                print('돈이 모자라네...')
                return
            self.__wallet -= amount
            print('이제 {0}원 남았네요.'.format(self.__wallet))

    maria = Person('마리아', 20, '서울시 서초구 반포동', 10000)
    maria.pay(3000)

    class Person:
        bag = []

        def put_bag(self, stuff):
            self.bag.append(stuff)

    james = Person()
    james.put_bag('책')

    maria = Person()
    maria.put_bag('열쇠')

    print(james.bag)
    print(maria.bag)

    class Person:
        def __init__(self):
            self.bag = []

        def put_bag(self, stuff):
            self.bag.append(stuff)

    james = Person()
    james.put_bag('책')

    maria = Person()
    maria.put_bag('열쇠')

    print(james.bag)
    print(maria.bag)

    # class Knight:
    #     __item_limit = 10
    #
    #     def print_item_limit(self):
    #         print(Knight.__item_limit)
    #
    #
    # x = Knight()
    # x.print_item_limit()
    #
    # print(Knight._item_limit)

    class Person:
        """사람 클래스입니다."""

        def greeting(self):
            """인사 메서드입니다."""
            print('Hello')

    print(Person.__doc__)
    print(Person.greeting.__doc__)

    maria = Person()
    print(maria.greeting.__doc__)

    class Calc:
        @staticmethod
        def add(a, b):
            print(a + b)

        @staticmethod
        def mul(a, b):
            print(a * b)

    Calc.add(10, 20)
    Calc.mul(10, 20)

    class Person:
        count = 0

        def __init__(self):
            Person.count += 1

        @classmethod
        def print_count(cls):
            print('{0}명 생성되었습니다.'.format(cls.count))

    james = Person()
    maria = Person()

    Person.print_count()

    class Person:
        def greeting(self):
            print('안녕하세요')

    class Student(Person):
        def study(self):
            print('공부하기')

    james = Student()
    james.greeting()
    james.study()

    class Person:
        def greeting(self):
            print('안녕하세요.')

    class Student(Person):
        def study(self):
            print('공부하기')

    james = Student()
    james.greeting()
    james.study()

    class Person:
        def greeting(self):
            print('안녕하세요.')

    class PersonList:
        def __init__(self):
            self.person_list = []

        def append_person(self, person):
            self.person_list.append(person)

    class Person:
        def __init__(self):
            print('Perosn __init__')
            self.hello = '안녕하세요'

    class Student(Person):
        def __init__(self):
            print('Student __init__')
            super().__init__()  # super(Student, self).__init__()
            self.school = '파이썬 코딩 도장'

    james = Student()
    print(james.school)
    print(james.hello)

    class Person:
        def __init__(self):
            print('Person __init__')
            self.hello = '안녕하세요'

    class Student(Person):
        pass

    james = Student()
    print(james.hello)

    class Person:
        def greeting(self):
            print('안녕하세요')

    class Student(Person):
        def greeting(self):
            print('안녕하세요 저는 파이썬 코딩 도장 학생입니다')

    james = Student()
    james.greeting()

    class Person:
        def greeting(self):
            print('안녕하세요')

    class university:
        def manage_credit(self):
            print('학점 관리')

    class Undergraduate(Person, university):
        def study(self):
            print('공부하기')

    james = Undergraduate()
    james.greeting()
    james.manage_credit()
    james.study()

    class A:
        def greeting(self):
            print('안녕하세요 A입니다')

    class B(A):
        def greeting(self):
            print('안녕하세요 B입니다')

    class C(A):
        def greeting(self):
            print('안녕하세요 C입니다')

    class D(B, C):
        pass

    x = D()
    x.greeting()
    print(D.mro())

    class StudentBase(metaclass=ABCMeta):
        @abstractmethod
        def study(self):
            pass

        @abstractmethod
        def go_to_school(self):
            pass

    class Student(StudentBase):
        def study(self):
            print('공부하기')

        def go_to_school(self):
            print('학교가기')

    james = Student()
    james.study()
    james.go_to_school()

    class Point2D:
        def __init__(self, x, y):
            self.x = x
            self.y = y

    p1 = Point2D(x=30, y=20)
    p2 = Point2D(x=60, y=50)

    a = p2.x - p1.x
    b = p2.y - p1.y
    print('p1: {} {}'.format(p1.x, p1.y))
    print('p2: {} {}'.format(p2.x, p2.y))

    c = math.sqrt((a * a) + (b * b))
    print(c)


def Try():
    try:
        x = int(input('나눌 숫자를 입력하세요: '))
        y = 10 / x
        print(y)
    except:
        print('에외가 발생했습니다')

    y = [10, 20, 30]

    try:
        index, x = map(int, input('인덱스와 나눌 숫자를 입력하세요(두 개): ').split())
        print(y[index] / x)
    except ZeroDivisionError as e:
        print('숫자를 0으로 나눌 수 없습니다.', e)
    except IndexError as e:
        print('잘못된 인덱스입니다.', e)
    try:
        x = int(input('나눌 숫자를 입력하세요: '))
        y = 10 / x
    except ZeroDivisionError:
        print('숫자를 0으로 나눌 수 없습니다')
    else:
        print(y)
    try:
        x = int(input('나눌 숫자를 입력하세요: '))
        y = 10 / x
    except ZeroDivisionError:
        print('숫자를 0으로 나눌 수 없습니다')
    else:
        print(y)
    finally:
        print('코드 실행이 끝났습니다')


# Iterator
def Iter():
    print(dir([1, 2, 3]))
    print([1, 2, 3].__iter__())
    it = [1, 2, 3].__iter__()
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())
    print('Hello, world'.__iter__())
    print({'a': 1, 'b': 2}.__iter__())
    print({1, 2, 3}.__iter__())
    it = range(3).__iter__()
    print(it.__next__())
    print(it.__next__())
    print(it.__next__())

    class Counter:
        def __init__(self, stop):
            self.current = 0
            self.stop = stop

        def __iter__(self):
            return self

        def __next__(self):
            if self.current < self.stop:
                r = self.current
                self.current += 1
                return r
            else:
                raise StopIteration

    for i in Counter(3):
        print(i, end=' ')
    print()
    a, b, c = Counter(3)
    print(a, b, c)
    a, b, c, d, e = Counter(5)
    print(a, b, c, d, e)

    class Counter:
        def __init__(self, stop):
            self.stop = stop

        def __getitem__(self, index):
            if index < self.stop:
                return index
            else:
                raise IndexError

    for i in Counter(3):
        print(i, end=' ')

    it = iter(range(3))
    print(next(it))
    print(next(it))
    print(next(it))
    it = iter(lambda: random.randint(0, 5), 2)
    # next(it)
    # next(it)
    # next(it)
    for i in iter(lambda: random.randint(0, 5), 2):
        print(i, end=' ')

    while True:
        i = random.randint(0, 5)
        if i == 2:
            break
        print(i, end=' ')

    it = iter(range(3))
    print(next(it, 10))
    print(next(it, 10))
    print(next(it, 10))
    print(next(it, 10))
    print(next(it, 10))


# Generator
def Generator():
    def number_generator():
        yield 0
        yield 1
        yield 2

    for i in number_generator():
        print(i)
    g = number_generator()
    print(g)
    print(g.__next__())
    print(g.__next__())
    print(g.__next__())

    def number_generator():
        yield 0
        yield 1
        yield 2

    g = number_generator()

    a = next(g)
    print(a)

    b = next(g)
    print(b)

    c = next(g)
    print(c)

    def number_generator(stop):
        n = 0
        while n < stop:
            yield n
            n += 1

    for i in number_generator(3):
        print(i)

    g = number_generator(3)
    print(next(g))
    print(next(g))
    print(next(g))

    def upper_generator(x):
        for i in x:
            yield i.upper()

    fruits = ['apple', 'pear', 'grape', 'pineapple', 'orange']
    for i in upper_generator(fruits):
        print(i)

    def number_generator():
        x = [1, 2, 3]
        for i in x:
            yield i

    for i in number_generator():
        print(i)

    def number_generator():
        x = [1, 2, 3]
        yield from x

    for i in number_generator():
        print(i)

    g = number_generator()

    # print(next(g))
    # print(next(g))
    # print(next(g))

    def number_generator(stop):
        n = 0
        while n < stop:
            yield n
            n += 1

    def three_generator():
        yield from number_generator(3)

    for i in three_generator():
        print(i)


# 코루틴
def coroutine():
    def add(a, b):
        c = a + b
        print(c)
        print('add 함수')

    def calc():
        add(1, 2)
        print('calc 함수')

    calc()

    def number_coroutine():
        while True:
            x = (yield)
            print(x)

    co = number_coroutine()
    next(co)

    co.send(1)
    co.send(2)
    co.send(3)

    def sum_coroutine():
        total = 0
        while True:
            x = (yield total)
            total += x

    co = sum_coroutine()
    print(next(co))

    print(co.send(1))
    print(co.send(2))
    print(co.send(3))

    def number_coroutine():
        while True:
            x = (yield)
            print(x, end=' ')

    co = number_coroutine()
    next(co)

    for i in range(20):
        co.send(i)

    co.close()

    def number_coroutine():
        try:
            while True:
                x = (yield)
                print(x, end=' ')
        except GeneratorExit:
            print()
            print('코루틴 종료')

    co = number_coroutine()
    next(co)

    for i in range(20):
        co.send(i)

    co.close()

    def sum_coroutine():
        try:
            total = 0
            while True:
                x = (yield)
                total += x
        except RuntimeError as e:
            print(e)
            yield total

    co = sum_coroutine()
    next(co)

    for i in range(20):
        co.send(i)

    print(co.throw(RuntimeError, '예외로 코루틴 끝내기'))

    def accumulate():
        total = 0
        while True:
            x = (yield)
            if x is None:
                return total
            total += x

    def sum_coroutine():
        while True:
            total = yield from accumulate()
            print(total)

    co = sum_coroutine()
    next(co)

    for i in range(1, 11):
        co.send(i)
    co.send(None)

    for i in range(1, 101):
        co.send(i)
    co.send(None)

    def accumulate():
        total = 0
        while True:
            x = (yield)
            if x is None:
                # raise StopIteration(total)  # (파이썬 3.6 이하)
                return total  # (파이썬 3.6 이상)
            total += x

    def sum_coroutine():
        while True:
            total = yield from accumulate()
            print(total)

    co = sum_coroutine()
    next(co)

    for i in range(1, 11):
        co.send(i)
    co.send(None)

    for i in range(1, 101):
        co.send(i)
    co.send(None)


# 데코레이터
def decorator():
    def hello():
        print('hello 함수 시작')
        print('hello')
        print('hello 함수 끝')

    def world():
        print('world 함수 시작')
        print('world')
        print('world 함수 끝')

    hello()
    world()

    def trace(func):
        def wrapper():
            print(func.__name__, '함수 시작')
            func()
            print(func.__name__, '함수 끝')

        return wrapper

    @trace
    def hello():
        print('hello')

    @trace
    def world():
        print('world')

    hello()
    world()

    def trace(func):
        def wrapper(a, b):
            r = func(a, b)
            print(' {0}(a={1}, b={2}) -> {3}'.format(func.__name__, a, b, r))
            return r

        return wrapper

    @trace
    def add(a, b):
        return a + b

    print(add(10, 20))

    def trace(func):
        def wrapper(*args, **kwargs):
            r = func(*args, **kwargs)
            print('{0}(args={1}, kwargs={2}) -> {3}'.format(func.__name__, args, kwargs, r))

            return r

        return wrapper

    @trace
    def get_max(*args):
        return max(args)

    @trace
    def get_min(**kwargs):
        return min(kwargs.values())

    print(get_max(10, 20))
    print(get_min(x=10, y=20, z=30))

    def is_multiple(x):
        def real_decorator(func):
            def wrapper(a, b):

                r = func(a, b)

                if r % x == 0:
                    print('{0}의 반환값은 {1}의 배수입니다.'.format(func.__name__, x))
                else:
                    print('{0}의 반환값은 {1}의 배수가 아닙니다'.format(func.__name__, x))
                return r

            return wrapper

        return real_decorator

    @is_multiple(3)
    def add(a, b):
        return a + b

    print(add(10, 20))
    print(add(2, 5))

    class Trace:
        def __init__(self, func):
            self.func = func

        def __call__(self):
            print(self.func.__name__, '함수 시작')
            self.func()
            print(self.func.__name__, '함수 끝')

    @Trace
    def hello():
        print('hello')

    hello()

    # @Trace 데코레이터를 안 쓸떄
    # trace_hello = Trace(hello)
    # trace_hello()

    class Trace:
        def __init__(self, func):
            self.func = func

        def __call__(self, *args, **kwargs):
            r = self.func(*args, **kwargs)
            print('{0}(args={1}, kwargs={2}) -> {3}'.format(self.func.__name__, args, kwargs, r))

            return r

    @Trace
    def add(a, b):
        return a + b

    print(add(10, 20))
    print(add(a=10, b=20))

    class IsMultiple:
        def __init__(self, x):
            self.x = x

        def __call__(self, func):
            def wrapper(a, b):
                r = func(a, b)
                if r % self.x == 0:
                    print('{0}의 반환값은 {1}의 배수입니다'.format(func.__name__, self.x))
                else:
                    print('{0}의 반환값은 {1}의 배수가 아닙니다'.format(func.__name__, self.x))
                return r

            return wrapper

    @IsMultiple(3)
    def add(a, b):
        return a + b

    print(add(10, 20))
    print(add(2, 5))


