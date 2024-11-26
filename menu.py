from tkinter import *
import tkinter as tk
 
root = Tk()
root.title("Крестики/Нолики")
root.geometry("450x600") 
root["bg"] = "gray22"



# Глобальные переменные для хранения состояния игры
current_player = "X"  # Начинаем с крестиков
buttons_state = [None] * 9  # Состояние кнопок (None означает, что кнопка не нажата)
buttons = []  # Список для хранения всех кнопок

# Функция, которая вызывается при нажатии на кнопку
def button_click(button_number):
    global current_player

    # Проверяем, была ли кнопка уже нажата
    if buttons_state[button_number - 1] is not None:
        return  # Если кнопка была нажата, ничего не делаем

    # Обновляем состояние кнопки
    buttons_state[button_number - 1] = current_player

    # Обновляем текст кнопки
    buttons[button_number - 1].config(text=current_player)

    # Меняем игрока
    current_player = "O" if current_player == "X" else "X"

    # Обновляем метку с текущим ходом
    current_player_label.config(text=f"Ход: {current_player}")

# Функция для очистки окна и создания 9 новых кнопок
def start_game():
    # Очистка существующих виджетов 
    for widget in root.winfo_children():
        widget.destroy()

    # Метка для отображения очереди хода
    global current_player_label
    current_player_label = tk.Label(root, text=f"Ход: {current_player}", font=("Arial", 16))
    current_player_label.place(x=150, y=20)  # Размещаем метку вверху

    # Создаем 9 кнопок в сетке 3x3
    global buttons  # Эта переменная будет использоваться для хранения кнопок
    buttons = []  # Сбрасываем список кнопок
    button_width = 150
    button_height = 60
    spacing_x = (500 - (button_width * 3)) // 4  # Горизонтальные промежутки
    spacing_y = (600 - (button_height * 3)) // 4  # Вертикальные промежутки

    for i in range(3):
        for j in range(3):
            button_number = i * 3 + j + 1  # Номер кнопки
            button = tk.Button(root, text="", command=lambda num=button_number: button_click(num),
                               width=8, height=3)  # Устанавливаем размеры кнопок
            # Вычисление координат для размещения кнопки
            x = j * (button_width + spacing_x) + spacing_x
            y = (i * (button_height + spacing_y) + spacing_y) + 60  # Учитываем высоту метки
            button.place(x=x, y=y)  # Размещаем кнопку
            buttons.append(button)  # Добавляем кнопку в список














button = tk.Button(root, text="Начать игру", command=start_game, bg= 'blue')
button.config(width=50, height=30, )
button.pack(anchor=CENTER, expand=1)
 
root.mainloop()