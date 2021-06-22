text = str(input("Введите текст: "))

# Если пользователь забыл поставить точку:

for i in range(len(text)):
    if text[-1] == ".":
        print("Спасибо!")
        break
    elif text[i] != ".":
        text = str(input("Вы забыли точку! Введите с точкой: "))

# Длина строки:

print("Длина строки: ", len(text))

# Количество слов в строке:

length = len(text)
space = " "

n = 0
a = 0

while n < length:
    if text[n] == space:
        a += 1
    n = n + 1
print("Слов в строке: ", a + 1)

# Самое длинное слово:

text = text.split()
print("Самое длинное слово: ", max(text, key=len))

# Самое короткое слово:

print("Короткое слово: ", min(text, key=len))






































