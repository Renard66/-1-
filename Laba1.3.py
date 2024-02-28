import random
import time

#Случайная матрица
def Random_massiv(m, n):
    matr = []
    for _ in range(n):
        diapazon = [random.randint(0,60) for _ in range(m)]
        matr.append(diapazon)
    return matr

#Сортировка выбором
def sort_vibor(rez):
    for i in range(len(rez)):
        min = i
        for j in range(i+1, len(rez)):
            if rez[j] < rez[min]:
                min = j
        rez[min], rez[i] = rez[i], rez[min]
    return rez

# Сортировка вставкой
def sort_vstavka(rez):
    for i in range(1, len(rez)):
        hislo = rez[i]
        j = i - 1
        while j >= 0 and hislo < rez[j]:
            rez[j+1] = rez[j]
            j -= 1
        rez[j+1] = hislo
    return rez

#Сортировка пузырьком
def sort_bubble(rez):
    a = len(rez)
    for i in range(a-1):
        for j in range (0, a-i-1):
            if rez[j] > rez[j+1]:
                rez[j], rez[j+1] = rez[j+1], rez[j]
    return rez

#Сортировка Шелла
def sort_shell(rez):
    n = len(rez) // 2
    while n > 0:
        for i in range(n, len(rez)):
            temp = rez[i]
            j = i
            while j >= n and rez[j - n] > temp:
                rez[j] = rez[j - n]
                j -= n
            rez[j] = temp
        n //= 2
    return rez

#Сортировка быстрая
def sort_bistraya(rez):
    if len(rez) > 1:
        pivot = rez.pop()
        gr_lst, eq_lst, sm_lst = [], [pivot], []
        for item in rez:
            if item == pivot:
                eq_lst.append(item)
            elif item > pivot:
                gr_lst.append(item)
            else:
                sm_lst.append(item)
        return (sort_bistraya(sm_lst) + eq_lst + sort_bistraya(gr_lst))
    else:
        return rez

#Пирамидальна сортировка(турнирная, сортировка кучей)
def sort_piramida(rez):
    def heapify(rez, n, i):
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and rez[i] < rez[l]:
            largest = l
        if r < n and rez[largest] < rez[r]:
            largest = r
        if largest != i:
            rez[i], rez[largest] = rez[largest], rez[i]
            heapify(rez, n, largest)

    def build_max_heap(rez):
        n = len(rez)
        for i in range(n//2 - 1, -1, -1):
            heapify(rez, n, i)

    def tournament(rez):
        n = len(rez)
        build_max_heap(rez)
        for i in range(n-1, 0, -1):
            rez[0], rez[i] = rez[i], rez[0]
            heapify(rez, i, 0)

    tournament(rez)
    return rez

# Замер времени работы алгоритма сортировки
def time_sort(sort_func, rez): #measure_time_sort
    start_time = time.time()
    sorted_rez = sort_func(rez)
    end_time = time.time()
    return sorted_rez, end_time - start_time

# Замер времени работы стандартной функции сортировки
def time_sorted(rez): #measure_time_sorted
    start_time = time.time()
    sorted_rez = sorted(rez)
    end_time = time.time()
    return sorted_rez, end_time - start_time

# Генерация случайной матрицы размером 100*100
matr = Random_massiv(100, 100)
print("Исходная матрица:")
for diapazon in matr:
    print(diapazon)

# Перевод матрицы в одномерный список
rez = [a for diapazon in matr for a in diapazon]

# Сортировка выбором
sorted_rez, duration = time_sort(sort_vibor, rez)
print("\nРезультат сортировки выбором:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка вставкой
sorted_rez, duration = time_sort(sort_vstavka, rez)
print("\nРезультат сортировки вставкой:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка пузырьком
sorted_rez, duration = time_sort(sort_bubble, rez)
print("\nРезультат сортировки пузырьком:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка Шелла
sorted_rez, duration = time_sort(sort_shell, rez)
print("\nРезультат сортировки Шелла:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

# Быстрая сортировка
sorted_rez, duration = time_sort(sort_bistraya, rez)
print("\nРезультат быстрой сортировки:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

#Пирамидальна сортировка(турнирная, сортировка кучей)
sorted_rez, duration = time_sort(sort_piramida, rez)
print("\nРезультат турнирной сортировки:")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)

# Сортировка с использованием стандартной функции sorted()
sorted_rez, duration = time_sorted(rez)
print("\nРезультат сортировки с использованием стандартной функции sorted():")
print(sorted_rez)
print("Время работы алгоритма: %.6f сек" % duration)












