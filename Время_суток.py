clock = int(input("Введите время суток: "))

if 6 <= clock < 12:
    print("Сейчас утро!")
elif 12 <= clock < 18:
    print("Сейчас день!")
elif 18 <= clock < 24:
    print("Сейчас вечер")
elif 0 <= clock < 6:
    print("Сейчас ночь!")
else:
    print("Не верно введенные данные!")