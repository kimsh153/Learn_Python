import turtle as t


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
