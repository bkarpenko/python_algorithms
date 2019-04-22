#!/usr/bin/env python
# coding: utf-8


from collections import defaultdict, Counter, deque
import random
import re

""""
1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала 
(т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль 
(за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего 
и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
"""


n = int(input("введите количество компаний "))
d = defaultdict(list)
for i in range(n):
    compInput = input("введите название компании ")
    for j in range(1, 5):
        d[compInput].append(int(input(f"введите прибыль за {j} квартал ")))
print("data on companies", d)
# get average profit
profitAv = sum(map(sum, d.values())) / n
profHigh = []
profLaw = []
for company in d:
    if sum(d[company]) >= profitAv:
        profHigh.append(company)
    else:
        profLaw.append(company)
print("companies with profit higher than average:", *profHigh)
print("companies with profit lawer than average:", *profLaw) 


""""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел. 
При этом каждое число представляется как массив, элементы которого это цифры числа. 
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. 
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], 
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

def splitByChar(s):
    l = []
    for char in s.replace(" ", ""):
        l.append(char)
    return l

def normLen(list):
    maxLen = 0
    for each in list:
        if len(each) > maxLen:
            maxLen = len(each)
    for each in list:
        while len(each) < maxLen:
            each.append(0)

a = splitByChar(input("введите число в 16-сной системе "))
b = splitByChar(input("введите число в 16-сной системе "))
# create list of all numbers in hexadecimal system
l = [str(i) for i in range(10)] + ["A", "B", "C", "D", "E", "F"]

# normalize given numbers and reverse for easier calculation
a_norm = [l.index(each) for each in a][::-1]
b_norm = [l.index(each) for each in b][::-1]
# make each list of numbers equel length
normLen([a_norm, b_norm])
        
c = list(map(sum, list(zip(a_norm, b_norm))))
for i in range(len(c)): # 0; 1;
    if c[i] > 15:
        c[i] = c[i] - 16
        if i == len(c) - 1:
            c.append(1)
        else:
            c[i + 1] += 1
result = [l[each] for each in c][::-1]
print(result)