from random import randint

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
x = int(input("Максимальное значение рандомного числа: "))

a = [[randint(0, x) for a in range(n)] for b in range(m)]

for i in range(m):
    for j in range(n):
        print(a[i][j], end=' ')
    print("")
    