# 2-ое задание: Написать генератор случайных матриц(многомерных), который принимает опциональные параметры
# m, n, min_limit, max_limit, где m и n указывают размер матрицы, а min_lim и max_lim - минимальное и максимальное
# значение для генерируемого числа.

import random

def Random_massiv(m, n, min_limit, max_limit):
    matr = []
    for i in range(m):
        a = []
        for j in range(n):
            diapazon = random.randint(min_limit, max_limit)
            a.append(diapazon)
        matr.append(a)
    return matr

m = random.randint(1,10)
n = random.randint(1,10)
min_limit = int(input("Введите самое маленькое число в матрице: "))
max_limit = int(input("Введите самое большое число в матрице: "))

mas = Random_massiv(m, n, min_limit, max_limit)
print("Наша матрица:")
for a in mas:
    print(a)





