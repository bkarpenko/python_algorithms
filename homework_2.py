#!/usr/bin/env python
# coding: utf-8


import random


#1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа. Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль, если он ввел 0 в качестве делителя.


# define functions
def super_sum(n1, n2):
    print(n1 + n2)
    
def substract(n1, n2):
    print(n1 - n2)

def product(n1, n2):
    print(n1 * n2)
    
def devide(n1, n2):
    if n2 == 0:
        print("число нельзя поделить на 0")
    else:
        print(n1 / n2) 

# create dict of functions
dict_fns = {
    "+": super_sum,
    "-": substract,
    "*": product,
    "/": devide
}

commands = [
    "суммировать", 
    "вычесть", 
    "умножить", 
    "разделить"
]

# print menu for user
i = 0
for each in dict_fns:
    print(f"{each} : {commands[i]}")
    i += 1
print("0 : завершить программу\n")


#input
while True:
    user_input = input("введите через пробел 2 числа и знак операции, которую хотите выполнить.\nчтобы завершить программу, просто наберите 0\n").split()
    if len(user_input) == 1 and user_input[0] == "0":
        print("программа завершена")
        break
    
    elif len(user_input) == 3:
        try:
            #assign input to variables
            num1, num2 = list(map(float, user_input[ : 2]))
            operation = user_input[2]          
            if operation in ['+', "-", "*", "/"]:
                dict_fns[operation](num1, num2)
            else:
                print("выберите тип операции из предложенных")
        except:
            print("первые два значения должны быть числами")


    else:
        print("не правильный ввод")


#2. Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).

even_nums = []
uneven_nums = []

num = input("введите число\n")

for digit in num:
    if int(digit) % 2 == 0:
        even_nums.append(digit)
    else:
        uneven_nums.append(digit)
print(f"количество четных чисел: {len(even_nums)}, количество нечетных чисел: {len(uneven_nums)}")

#3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран. Например, если введено число 3486, то надо вывести число 6843.

num = input("введите число\n")

print(num[::-1])


#5. Вывести на экран коды и символы таблицы ASCII, начиная с символа под номером 32 и заканчивая 127-м включительно. Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

l2 = []

for i in range(loops):
    for each in l[i*10 : i*10 + 10]:
        l2.append(str(each) + "-" + chr(each))
    print(", ".join(l2))
    l2 = []


#6. В программе генерируется случайное целое число от 0 до 100. Пользователь должен его отгадать не более чем за 10 попыток. После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число, чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.

random_num = random.randint(0, 100)

result = "loose"

print("угадайте целое число 0 до 100\n")

for i in range(10):
    print(f"попытка номер {i + 1}\n")
    user_input = int(input())
    if user_input == random_num:
        result = "win"
        break
    else:
        if user_input > random_num:
            print("\nчисло меньше\n")
        else:
            print("\nчисло больше\n")

if result == "win": 
    print(f"поздравляю тебя, ты угадал! Это число {random_num}")
else:
    print(f"это число {random_num}. Не расстраивайся, повезет в следующий раз!")



#8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел. Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

user_input = input("введите последовательность чисел ")
user_digit = input("введите цифру, которую нужно найти ")

count = str(user_input.count(user_digit))

if len(count) > 1:
    if  "12" <= count[-2:] <= "14":
        word_ending = ""
    elif "2" <= count[-2:] <= "4":
        word_ending = "а"
    else:
        word_ending = ""
            
elif "2" <= count <= "4":
    word_ending = "а"
else:
    word_ending = ""

print(f'цифра {user_digit} встречается {count} раз{word_ending}')


#9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр. Вывести на экран это число и сумму его цифр.

user_input = list(map(int, input("введите через пробел несколько натуральных чисел ").split()))

max_num = user_input[0]

for i in range(1, len(user_input)):
    if super_sum(user_input[i]) > super_sum(max_num):
        max_num = user_input[i]

print(f"{max_num}, сумма чисел: {super_sum(max_num)}")


#7. Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.

#1+2+...+n = n(n+1)/2

while True:
    try:
        user_input = int(input("укажите диапозон для множества\n"))
        break
    except:
        print("введено не целое число\n")

l = list(range(1, user_input + 1))
n = len(l)

print("проверка множества 1+2+...+n = n(n+1)/2")

calc1 = sum(l)
calc2 = n * (n + 1) / 2

if calc1 == calc2:
    print("равенство выполняется")
else:
    print("равенство не выполняется")