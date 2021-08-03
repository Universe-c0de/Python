from tkinter import *
from tkinter.font import Font
from tkinter import filedialog
import pickle

root = Tk()
root.title('To Do List!')
root.iconbitmap("F:/Python/To_Do/icons/ico.ico")
root.geometry("550x500+650+250")

# Шрифт
my_font = Font(
    family="Gabriola",
    size=25,
    weight="bold")

# Создаем рамку
my_frame = Frame(root)
my_frame.pack(pady=10)

# Создаем список
my_list = Listbox(my_frame,
                  font=my_font,
                  width=38,
                  height=5,
                  bg="SystemButtonFace",
                  bd=0,
                  fg="#464646",
                  highlightthickness=0,
                  selectbackground="#a6a6a6",
                  activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

stuff = ["Список дел", "Сходить в магазин", "Выпить витамины"]

for item in stuff:
    my_list.insert(END, item)

# Создаем колесо прокрутки
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=Y)

# Добавляем прокрутку
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# Создаем поле ввода
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Создаем кнопки и рамки
button_frame = Frame(root)
button_frame.pack(pady=20)

# Функции
def add_item():
    my_list.insert(END, my_entry.get())
    my_entry.delete(0, END)

def delete_item():
    my_list.delete(ANCHOR)

def cross_off_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#dedede")
    my_list.select_clear(0, END)

def uncross_item():
    my_list.itemconfig(
        my_list.curselection(),
        fg="#464646")
    my_list.select_clear(0, END)

def delete_crossed():
    count = 0
    while count < my_list.size():
        if my_list.itemcget(count, "fg") == "#dedede":
            my_list.delete(my_list.index(count))
        else:
            count += 1

def save_list():
    file_name = filedialog.asksaveasfilename(
        initialdir="F:/Python/To_Do/data",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
        )
    if file_name:
        if file_name.endswith(".dat"):
            pass
        else:
            file_name = f'{file_name}.dat'

        # Удаление пунктов перед сохранением
        count = 0
        while count < my_list.size():
            if my_list.itemcget(count, "fg") == "#dedede":
                my_list.delete(my_list.index(count))
            else:
                count += 1

        # выбор всех пунктов из списка
        stuff = my_list.get(0, END)

        # Открыть файл
        output_file = open(file_name, 'wb')

        pickle.dump(stuff, output_file)

def open_list():
    file_name = filedialog.askopenfilename(
        initialdir="F:/Python/To_Do/data",
        title="Save File",
        filetypes=(
            ("Dat Files", "*.dat"),
            ("All Files", "*.*"))
        )
    if file_name:
        my_list.delete(0, END)

        input_file = open(file_name, 'rb')

        stuff = pickle.load(input_file)

        for item in stuff:
            my_list.insert(END, item)

def delete_list():
    my_list.delete(0 ,END)

# Создаем меню
my_menu = Menu(root)
root.config(menu=my_menu)

# Добавляем элементы в меню
file_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Файл", menu=file_menu)

file_menu.add_command(label="Сохранить список", command=save_list)
file_menu.add_command(label="Открыть список", command=open_list)
file_menu.add_separator()
file_menu.add_command(label="Очистить список", command=delete_list)

add_button = Button(button_frame, text="Добавить", command=add_item)
delete_button = Button(button_frame, text="Удалить", command=delete_item)
cross_off_button = Button(button_frame, text="Вычеркнуть", command=cross_off_item)
uncross_button = Button(button_frame, text="Отменить", command=uncross_item)
delete_crossed_button = Button(button_frame, text="Удалить вычеркнутые", command=delete_crossed)

add_button.grid(row=0, column=0)
delete_button.grid(row=0, column=1, padx=20)
cross_off_button.grid(row=0, column=2)
uncross_button.grid(row=0, column=3, padx=20)
delete_crossed_button.grid(row=0, column=4)

root.mainloop()
