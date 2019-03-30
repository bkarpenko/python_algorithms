#!/usr/bin/env python
# coding: utf-8

import random
from pprint import pprint

#1. В диапазоне натуральных чисел от 2 до 1000000 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

result = []
for i in range(2, 1000000 + 1):
    if i % 5 == 0 and i % 7 == 0 and i % 8 == 0 and i % 9 == 0:
        result.append(i)
print(len(result))
result[:10]

# 2. Во втором массиве сохранить индексы четных элементов первого массива. Например, если дан массив со значениями 8, 3, 15, 6, 4, 2, то во второй массив надо заполнить значениями 1, 4, 5, 6 (или 0, 3, 4, 5 - если индексация начинается с нуля), т.к. именно в этих позициях первого массива стоят четные числа.

l = [random.randint(1, 100) for i in range(10)]
print("исходный массив: ", l)

result = []

for i in range(len(l)):
    if l[i] % 2 == 0:
        result.append(i + 1)
print(result)

# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

l = [random.randint(1, 100) for i in range(10)]
print("исходный массив: ", l)

max = l[0]
min = l[1]
max_ind = 0
min_ind = 1

if max < min:
    max, min = min, max
    max_ind, min_ind = min_ind, max_ind   
    
for i in range(2, len(l)):
    if l[i] > max:
        max = l[i]
        max_ind = i
    elif l[i] < min:
        min = l[i]
        min_ind = i

l[max_ind], l[min_ind] = l[min_ind], l[max_ind]
print("итоговый массив: ", l)


#4. Определить, какое число в массиве встречается чаще всего.

def find_max(seq):
    max = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > max:
            max = seq[i]
    return max


l = [random.randint(1, 10) for i in range(20)]
print("исходный массив: ", *l)

d = {}
# populate dict with unique numbers as keys & freq as its values
for each in l:
    if each in d:
        d[each] = d[each] + 1
    else:
        d[each] = 1
print("dict:", d)

keys = list(d.keys())
values = list(d.values())

max = find_max(values)
result = []

for i in range(len(values)):
    if values[i] == max:
        result.append(keys[i])

print(*result)


# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.

l = [random.choice(range(-100, 101)) for i in range(10)]
print("исходный массив: ", *l)

min = l[0]
min_index = 0

for i in range(1, len(l)):
    if l[i] < min:
        min = l[i]
        min_index = i
        
print("максимальный отрицательный элемент: ", min)
print("позиция в массиве: ", min_index)


# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.
l = [random.choice(range(-100, 101)) for i in range(10)]
print("исходный массив: ", *l)

max = l[0]
min = l[1]
max_ind = 0
min_ind = 1

if len(list(set(l))) == 1:
    print("в массиве нет элементов для сравнения")
else:
    if max < min:
        max, min = min, max
        max_ind, min_ind = min_ind, max_ind  

    for i in range(2, len(l)):
        if l[i] > max:
            max = l[i]
            max_ind = i
        elif l[i] < min:
            min = l[i]
            min_ind = i

if min_ind > max_ind:
    min_ind, max_ind = max_ind, min_ind

print("min:", min, "\nmax:", max)
slice = l[min_ind + 1: max_ind]
if len(slice) == 0:
    print("между минимальным и максимальным элементом нет других элементов")
else:
    print("срез элементов между минимальным и максимальным элементами", *slice)
    s = sum(slice)
    print("сумма элементов между максимальным и минимальным элентами:", s)

# 7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.

l = [random.choice(range(-100, 101)) for i in range(10)]
print("исходный массив: ", *l)

min1 = l[0]
min2 = l[1]
min1_ind = 0
min2_ind = 1

if len(list(set(l))) == 1:
    print("в массиве нет элементов для сравнения")
else:
    if min1 > min2:
        min1, min2 = min2, min1
        min1_ind, min2_ind = min1_ind, min2_ind  

    for i in range(2, len(l)):
        if l[i] < min1:
            min2 = min1
            min2_ind = min1_ind
            min1 = l[i]
            min1_ind = i
        elif l[i] < min2:
            min2 = l[i]
            min2_ind = i
    print("min1:", min1, "\nmin2:", min2)


# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.

from pprint import pprint

def mtrx_generator(width, length):
    for row in range(width):
        r = [random.randint(1, 100) for clmn in range(length - 1)]
        r.append(sum(r))
        mtrx.append(r)

mtrx = []

user_input = list(map(int, input("введите через пробел кол. строк и столбцов для матрицы ").split()))
width, length = user_input

mtrx_generator(width, length)

pprint(mtrx)

# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

def mtrx_generator(width, length):
    for row in range(width):
        r = [random.randint(1, 100) for clmn in range(length)]
        mtrx.append(r)
        
def find_min(seq):
    min = seq[0]
    for i in range(1, len(seq)):
        if seq[i] < min:
            min = seq[i]
    return min     

def find_max(seq):
    max = seq[0]
    for i in range(1, len(seq)):
        if seq[i] > max:
            max = seq[i]
    return max  
        
mtrx = []

mtrx_generator(5, 4)
print("matrix")
pprint(mtrx)

# get columns
clmns = list(zip(*mtrx))
print("clmns", *clmns)

# create list of min elements from each clmn
l = [find_min(clmn) for clmn in clmns]
print("smallest elements from each clmn", *l)
print("max el from mins:", find_max(l))

