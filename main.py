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
            print('*',end='')
    print()
print()

for i in range(5):
    for j in range(5):
        if j == i:
            print('*',end='')
        else:
            print(' ',end='')
    print()