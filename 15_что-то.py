# p = {2, 4, 6, 8, 10, 12, 14, 16, 18, 20}
# q = {3, 6, 9, 12, 15, 18, 21, 24, 27, 30}
# a = set()
#
# def f(x):
#     return ((x in p) <= (x in a)) or ((x not in a) <= (x not in q))
#
# for x in range(1,1000):
#     if f(x) == 0:
#         if f(x) == 0:
#             a.add(x)
#
# print(f'Множество: {a}')
# print(f'Сумма: {sum(a)}')
# print(f'Максимум: {max(a)}')
# print(f'Минимум: {min(a)}')
# p = {2, 4, 6, 8, 10, 12}
# q = {4, 8, 12, 116}
# a = set()
#
# def f(x):
#     return (x in p) <= (((x in q) and(x not in a)) <= (x not in p))
#
# for x in range(1,1000):
#     if f(x) == 0:
#         if f(x) == 0:
#             a.add(x)
#
# print(f'Множество: {a}')
# print(f'Сумма: {sum(a)}')
# print(f'Максимум: {max(a)}')
# print(f'Минимум: {min(a)}')
# p = {2, 4, 6, 8, 12, 14, 16, 18, 20}
# q = {5, 10, 15, 20, 25, 30, 35, 40, 45, 50}
# a = set(range(1, 1000))
#
# def f(x):
#     return ((x in a) <= (x in p)) or (not(x in q) <= (not(x in a)))
#
# for x in range(1, 1000):
#     if f(x) == 0:
#         a.remove(x)
#
# print(f'Множество: {a}')
# print(f'Сумма: {sum(a)}')
# print(f'Максимум: {max(a)}')
# print(f'Минимум: {min(a)}')