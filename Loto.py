import random

num = int(input("Введите количество бочонков: "))

lst = {1: '1 - Пётр I', 2: '2 - Опять двойка?', 3: '3 - 3-е тысячелетие вместе с «Русским Лото»', 4: '4 - Все четыре колеса',
         5: '5 - Отличник', 6: '6 - Точка внизу', 7: '7 - Кочережка', 8: '8 - Обручальные кольца', 9: '9 - Точка внизу',
         10: '10 - Череп', 11: '11 - Барабанные палочки', 12: '12 - Дюжина', 13: '13 - Чёртова дюжина', 14: '14 - Олимпиада в Сочи',
         15: '15 - Пятнадцатилетний капитан', 16: '16 - Кругом шестнадцать', 17: '17 - Где мои семнадцать лет', 18: '18 - В первый раз',
         19: '19', 20: '20 - Гусь на тарелке', 21: '21 - Очко', 22: '22 - Утята', 23: '23 - Два притопа, три прихлопа', 24: '24',
         25: '25 - Опять двадцать пять', 26: '26', 27: '27', 28: '28', 29: '29', 30: '30 - Ума нет', 31: '31', 32: '32',
         33: '33 - Кудри', 34: '34', 35: '35', 36: '36 - Нормальная температура', 37: '37', 38: '38 - 38 попугаев', 39: '39', 40: '40',
         41: '41', 42: '42', 43: '43 - Сталинград', 44: '44 - Стульчики', 45: '45 - День Победы', 46: '46', 47: '47 - Баба ягодка совсем',
         48: '48 - Пеле', 49: '49', 50: '50 - Полста', 51: '51 - Великолепная пятёрка и вратарь', 52: '52', 53: '53 - Холодное лето 53-го',
         54: '54', 55: '55 - Перчатки', 56: '56 - Оттепель', 57: '57', 58: '58', 59: '59', 60: '60', 61: '61 - Гагарин', 62: '62', 63: '63 - Валентина Терешкова',
         64: '64 - Шахматная доска', 65: '65', 66: 'Валенки', 67: '67', 68: '68', 69: '69 - Туда-сюда', 70: '70', 71: '71', 72: '72', 73: '73', 74: '74', 75: '75',
         76: '76', 77: '77 - Топорики', 78: '78', 79: '79 - Золото', 80: '80 - Олимпиада в Москве', 81: '81 - Бабка с клюшкой',
         82: '82 - Бабушка надвое сказала', 83: '83', 84: '84', 85: '85', 86: '86', 87: '87', 88: '88 - Матрёшки', 89: '89 - Дедушкин сосед',
         90: '90 - Дедушка', 91: '91', 92: '92', 93: '93', 94: '94', 95: '95', 96: '96', 97: '97', 98: '98', 99: '99'}

for i in range(num):
     a = random.randint(1, 99)
     print(lst[a])




