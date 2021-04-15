#for문 별찍기
# for i in range(5):
#     for j in range(5):
#         print('*', end='')
#     print()
# print()
# for i in range(3):
#     for j in range(7):
#         print('*', end='')
#     print()
# print()
#
# for i in range(5):
#     for j in range(5):
#         if j <= i:
#             print('*',end='')
#     print()
# print()
#
# for i in range(5):
#     for j in range(5):
#         if j == i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()
import turtle as t
t.shape('turtle')
t.speed('fastest')

for i in range(300):
    t.fd(i)
    t.right(91)
t.mainloop()