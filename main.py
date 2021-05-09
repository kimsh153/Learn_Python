import turtle as t
import copy
import pickle


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
def set():
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
