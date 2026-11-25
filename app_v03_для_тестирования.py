# Приложение «Приём заявок», версия 0.3.0 (для тестирования обновления)
# Изменение CR-1: счётчик закрытых заявок и номер версии в окне.

from tkinter import *
from tkinter import ttk
from datetime import datetime

LIMIT = 10          # по требованиям: максимум 10 заявок
count = 0           # сколько заявок принято
STATUSES = ["Новая", "В работе", "Готово"]
status_index = 0
closed = 0          # сколько заявок закрыто (статус «Готово»)
VERSION = "0.3.0"

def accept():
    global count
    count = count + 1
    label_count["text"] = count
# ЗАДАЧА #14: дата принятия заявки (раскомментируйте строку ниже)
    label_date["text"] = "Принято: " + datetime.now().strftime("%d.%m.%Y %H:%M")
    if count > LIMIT:
        label_count["text"] = "Лимит: " + str(count)
        btn_accept["state"] = "disabled"

def reset():
    global count, closed
    count = 0
    label_count["text"] = count
    btn_accept["state"] = "normal"
    label_date["text"] = "Принято: —"

# ЗАДАЧА #12: статус заявки (раскомментируйте функцию целиком)
def change_status():
    global status_index, closed
    status_index = (status_index + 1) % len(STATUSES)
    label_status["text"] = "Статус: " + STATUSES[status_index]
    if STATUSES[status_index] == "Готово":
        closed = closed + 1
        label_closed["text"] = "Закрыто заявок: " + str(closed)

window = Tk()
window.title("Приём заявок " + VERSION)
window.geometry("300x460")

logo = PhotoImage(file="logo.png")
picture = Label(image=logo)
picture.pack()

label_title = Label(text="Количество заявок:")
label_title.pack()

label_count = Label(text="0", fg="black")
label_count.pack()

# ЗАДАЧА #14: дата принятия заявки (раскомментируйте 2 строки ниже)
label_date = Label(text="Принято: —")
label_date.pack()

# ЗАДАЧА #12: статус заявки (раскомментируйте 4 строки ниже)
label_status = Label(text="Статус: Новая")
label_status.pack()
label_closed = Label(text="Закрыто заявок: 0")
label_closed.pack()
btn_status = ttk.Button(text="Сменить статус", command=change_status)
btn_status.pack(pady=5)

btn_accept = ttk.Button()
btn_accept.pack(pady=5)
btn_accept["text"] = "Принять заявку"
btn_accept["command"] = accept

btn_reset = ttk.Button()
btn_reset.pack(pady=5)
btn_reset["text"] = "Сбросить"
btn_reset["command"] = reset

# ЗАДАЧА #13: крупные кнопки (раскомментируйте 2 строки ниже)
btn_accept["width"] = 20
btn_reset["width"] = 20

label_version = Label(text="Версия " + VERSION, fg="gray")
label_version.pack(side="bottom")

window.mainloop()
