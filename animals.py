giraffe = float(input("Введите вес жирафа: "))
elephant = float(input("Введите вес слона: "))
crocodile = float(input("Введите вес крокодила: "))

gaz = float(input("Введите грузоподъемность ГАЗа: "))
zil = float(input("Введите грузоподъемность ЗИЛа: "))

a = (giraffe + elephant + crocodile) <= gaz
b = (giraffe + elephant + crocodile) <= zil
c = (giraffe + elephant <= gaz) and (crocodile <= zil)
d = (giraffe <= gaz) and (elephant + crocodile <= zil)
e = (elephant <= gaz) and (crocodile + giraffe <= zil)
f = (crocodile <= gaz) and (giraffe + elephant <= zil)
g = (elephant + crocodile <= gaz) and (giraffe <= zil)
h = (crocodile + giraffe <= gaz) and (elephant <= zil)

all = a or b or c or d or e or f or g or h

print("Жираф, слон, крокодил на ГАЗе: " + str(a))
print("Жираф, слон, крокодил на ЗИЛе: " + str(b))
print("Жираф, слон на ГАЗе, крокодил на ЗИЛе: " + str(c))
print("Жираф на ГАЗе, слон, крокодил на ЗИЛе: " + str(d))
print("Слон на ГАЗе, крокодил, жираф на ЗИЛе: " + str(e))
print("Крокодил на ГАЗе, жирафб слон на ЗИЛе: " + str(f))
print("Слон, крокодил на ГАЗе, жираф на ЗИЛе: " + str(g))
print("Крокодил, жираф на ГАЗе, слон на ЗИЛе: " + str(h))

print("Один из вариантов верен: " + str(all))

