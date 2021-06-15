# Задание № 3:

x = float(input("Введите вес шоколадных конфет: "))
a = float(input("Введите цену шоколадных конфет: "))
y = float(input("Введите вес ирисок: "))
b = float(input("Введите цену ирисок: "))
chocoSum = a / x
toffeeSum = b / y
diff = chocoSum / toffeeSum
print("Цена шоколадных конфет за 1кг: ", chocoSum)
print("Цена ирисок за 1 кг: ", toffeeSum)
if chocoSum > toffeeSum:
    print("Шоколадные конфеты дороже ирисок в: ", diff)
else:
    print("Данные не соответствуют условиям задачи!")

