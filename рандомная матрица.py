from random import randint

n = int(input("Введите значение n: "))
m = int(input("Введите значение m: "))
x = int(input("Максимальное значение рандомного числа: "))

matrix = [[randint(0, x) for i in range(n)] for j in range(m)]

for i in range(m):
    for j in range(n):
        print(matrix[i][j], end=' ')
    print("")
