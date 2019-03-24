import random, string, re


#1 Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

n = input("введите 3-х значное число\n")
s = sum(map(int, n))
p = 1
for each in n:
    p *= int(each)
print("сумма чисел =", s, "\nпроизведение чисел =", p)


#4 Написать программу, которая генерирует в указанных пользователем границах: 

#a случайное целое число
n1, n2 = list(map(int, input("введите через пробел нижнюю и верхнюю границы числового диапозона. Используйте целые числа\n").split()))
if n1 > n2:
    n1, n2 = n2, n1
print(random.randint(n1, n2))

#b случайное вещественное число
l = list(map(float, input("введите через пробел нижнюю и верхнюю границы числового диапозона. Используйте вещественные числа\n").split()))
print(random.uniform(l[0], l[1]))

#с случайный символ
a, b = input("введите через пробел границы символьного диапозона. Используйте две любых буквы английского алфавита\n").split()
if a < b:
    a, b = b, a

abc = string.ascii_letters
abc_slice = abc[abc.index(a) : abc.index(b) + 1]

print(random.choice(abc_slice))


# 5 Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв
letters = input("введите 2 любые буквы английского алфавита\n")

letters_clean = re.sub("[^A-Za-z]", "", letters)

letter1, letter2 = letters_clean[0], letters_clean[1]

# define alphabet    
abc = string.ascii_letters

print('позиция первого символа: {0}, позиция второго символа: {1}'.format(abc.index(letter1), abc.index(letter2)))

if letter1 < letter2:
    letter1, letter2 = letter2, letter1

letters_between = abc[abc.index(letter1) + 1 : abc.index(letter2)]
    
print("колличество букв между указанными буквами:", len(letters_between))



#6 Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

number = int(input("введите номер буквы английского алфавита в диапозоне от 1 до 26 включительно"))
abc = string.ascii_letters
print("вы ввели букву", abc[number - 1])




# 9 Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого)

a, b, c = list(map(int, input("введите 3 разных числа через пробел\n").split()))

if b < a < c or c < a < b:
    print(a, "является средним из 3-х чисел")
    
elif a < b < c or c < b < a:
    print(b, "является средним из 3-х чисел") 
    
elif a < c < b or c < c < a:
    print(c, "является средним из 3-х чисел") 



# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

year = int(input("введите год"))
if year % 400 == 0:
    print("Високосный")
else:
    if year % 4 == 0 and year % 100 > 0:
        print("Високосный")
    else:
        print("Обычный")
