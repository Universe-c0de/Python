

# Задание №2. В списке A=(a1, а2, ..., аn) все элементы, равные нулю, поставить сразу после
# максимального элемента данного списка. Заполняем список с помощью randint().


import random

number = int(input("Введите количество элементов в списке: "))

A = []

for i in range(number):
    a = random.randint(0, 6)
    A.append(a)
    maxi = max(A)
    mini = min(A)
    if mini == 0:
        A.insert(i, maxi)

print(A)
print(maxi)
print(mini)

