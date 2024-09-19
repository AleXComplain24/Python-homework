import tkinter
import os
from tkinter import filedialog

def file_select():
    filename = filedialog.askopenfilename(initialdir="/", title="Выберите файл",
                                        filetypes=(('Текстовый файл', '.txt'),
                                                   ('Все файлы', '*')))
    if filename:  # Проверка, выбран ли файл
        text['text'] = f'Файл: {filename}'
    else:
        text['text'] = 'Файл не выбран.'

def show_info():
    messagebox.showinfo("Информация", "Выберите файл, нажав кнопку 'Выбрать файл'.\n"
                                        "Вы можете выбрать текстовый файл или любой другой.")

def show_about():
    messagebox.showinfo("О программе", "Автор: Ваше имя\nВерсия: 1.0")


# Создание окна
window = tkinter.Tk()
window.title('Проводник')
window.geometry('350x150')  # Исправлены кавычки
window.configure(bg='black')
window.resizable(False, False)  # Исправлен синтаксис: False, False

# Создание меню
menu = tkinter.Menu(window)
window.config(menu=menu)

info_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="Info", menu=info_menu)
info_menu.add_command(label="Как работать", command=show_info)

about_menu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label="About", menu=about_menu)
about_menu.add_command(label="О программе", command=show_about)

# Добавление метки
text = tkinter.Label(window, text='Файл:', height=5, width=50,
                     background='silver', foreground='blue')  # Исправлено имя Label
text.grid(column=1, row=1)

# Добавление кнопки
button_select = tkinter.Button(window, width=20, height=3, text='Выбрать файл',
                               background='silver', foreground='blue',
                               command=file_select)
button_select.grid(column=1, row=2, pady=5)  # Здесь все скобки закрыты правильно

# Запуск главного цикла окна
window.mainloop()
