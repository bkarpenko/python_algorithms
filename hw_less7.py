#!/usr/bin/env python
# coding: utf-8

# In[2]:


import random


# In[3]:


"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами 
на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. 
Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).
"""
def buble_sort(list):
    a = list[:]
    for i in range(len(a) - 1):
        for j in range(1, len(a) - i):
            if a[j] > a[j - 1]:
                a[j], a[j - 1] = a[j - 1], a[j]
    return a

a = [random.randint(-100, 99) for i in range(10)]

print("дано:  ", *a)
print("ответ: ", *buble_sort(a))


# In[10]:


"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами 
на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

"""

def merge(a1, a2):
    r = []
    i = 0
    j = 0
    for k in range(len(a1) + len(a2)):
        if i == len(a1):
            r += a2[j: ]
            break
        elif j == len(a2):
            r += a1[i: ]
            break
        else:
            if a1[i] < a2[j]:
                r.append(a1[i])
                i += 1
            else:
                r.append(a2[j])
                j += 1
    return r

def my_sort(l):
    if len(l) == 1:
        return l
    mid = len(l) // 2
    lefthalf = my_sort(l[ :mid])
    righthalf = my_sort(l[mid: ])

    return merge(lefthalf, righthalf)

a = [random.uniform(0, 50) for i in range(20)]

print(f"дано:\n{a}\n")
print(f"ответ:\n{my_sort(a)}")


# In[9]:


"""
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. 
Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: 
в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы. 
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то используйте метод сортировки, 
который не рассматривался на уроках

"""
from collections import Counter

def counting_sort(lst, maxv):
    count = Counter(lst)
    res = []
    for i in range(maxv + 1):
        res += [i] * count[i]
    return res

m = 1
n = 2 * (m + 1)
a = [random.randint(1, 100) for i in range(n)]

sorted_a = counting_sort(a, max(a))

if len(sorted_a) % 2 != 0:
    median = sorted_a[len(sorted_a) // 2]
else:
    median = (sorted_a[len(sorted_a) // 2 - 1] + sorted_a[len(sorted_a) // 2]) / 2

print(f"median is: {median}")

