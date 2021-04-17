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
