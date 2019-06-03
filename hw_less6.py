from memory_profiler import memory_usage
from math import sqrt

n = int(input("input number "))
lst=[]
for i in range(2, n+1):
    if (i > 10):
        if (i%2==0) or (i%10==5):
            continue
    for j in lst:
        if j > int((sqrt(i)) + 1):
            lst.append(i)
            break
        if (i % j == 0):
            break
    else:
        lst.append(i)
print (lst)
memory_usage()

# программа требует порядка 50 мб. Разрядность OC - 64-бит. Версия Питона - 3.7.1