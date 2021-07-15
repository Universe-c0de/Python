import sqlite3

try:
    conn = sqlite3.connect('db1.sqlite')
    cursor = conn.cursor()
    print("Opened database successfully")
except sqlite3.Error as err:
    print('Error : ' + err.args[0])
finally:
    conn.close()
    print("Closed database successfully")

# Создаем таблицу

conn = sqlite3.connect('db1.sqlite')
cursor = conn.cursor()

cursor.execute(''' CREATE TABLE AUTHORIZATION
                   (ID INT PRIMARY KEY     NOT NULL,
	                LOGIN	 TEXT   NOT NULL,
	                PASSWORD	TEXT  NOT NULL);''')
conn.commit()


# Авторизация


for i in range(0, 1):
    id = i
    login = input("Введите логин: ")
    password = input("Введите пароль: ")
    cursor.execute('''INSERT INTO AUTHORIZATION(ID, LOGIN, PASSWORD) VALUES (?, ?, ?)''', (id, login, password))
    conn.commit()

conn.commit()
cursor.close()
conn.close()