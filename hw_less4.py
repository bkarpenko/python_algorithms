#!/usr/bin/env python
# coding: utf-8

# In[9]:


import random


# #### 1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

# на примере поиска всех простых чисел до числа n

# In[1]:


get_ipython().run_cell_magic('time', '', '# способ 1 \nfrom math import sqrt\nn = int(input("введите число"))\nlst=[]\nfor i in range(2, n+1):\n    for j in lst:\n        if j > int((sqrt(i)) + 1):\n            lst.append(i)\n            break\n        if (i % j == 0):\n            break\n    else:\n        lst.append(i)\nprint (lst)')


# In[30]:


get_ipython().run_cell_magic('time', '', '# способ 2\nfrom math import sqrt\nn = int(input("введите число "))\nlst=[]\nfor i in range(2, n+1):\n    if (i > 10):\n        if (i%2==0) or (i%10==5):\n            continue\n    for j in lst:\n        if j > int((sqrt(i)) + 1):\n            lst.append(i)\n            break\n        if (i % j == 0):\n            break\n    else:\n        lst.append(i)\nprint (lst)')


# In[29]:


#второй алгоритм проверяет только числа, которые заканчиваются на 1, 3, 7 или 9, т.к. остальные делятся на 2 или 5
#в итоге программа работает почти в 2р быстрее 


# #### 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»
# Примечание ко всему домашнему заданию: Проанализировать скорость и сложность алгоритмов. Результаты анализа сохранить в виде комментариев в файле с кодом.

# In[4]:


def nth_prime_number(n):
    prime_list = [2]
    num = 3
    while len(prime_list) < n:

        for p in prime_list:
            if num % p == 0:
                break
        else:
            prime_list.append(num)
        num += 2
    return prime_list[-1]


# In[6]:


get_ipython().run_cell_magic('time', '', 'n = int(input("введите i-е число последовательности простых чисел "))\nnth_prime_number(n)')


# In[ ]:


# c решетом Эратосфена

