n = int(input("Введите n: "))

def seq(n):
     if n == 1:
         return 1
     else:
         a = n - seq(seq(n - 1))
         return a

print(seq(n))


