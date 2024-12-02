from tkinter import *
import customtkinter as ctk

root = Tk()
root.title("Крестики/Нолики")
root.geometry("450x600")
root.configure(background='#17141e')


# Функция, которая вызывается при нажатии на кнопку
def button_click(button_number):
    global current_player

    # Проверяем, была ли кнопка уже нажата
    if buttons_state[button_number - 1] is not None:
        return  # Если кнопка была нажата, ничего не делаем

    # Обновляем состояние кнопки
    buttons_state[button_number - 1] = current_player
    buttons[button_number - 1].configure(text=current_player, font=('Arial', 20))

    winner = check_winner()
    if winner:
        show_result(f"Победитель: {winner}")
    elif None not in buttons_state:
        show_result("      Ничья!      ")
    else:
        current_player = "O" if current_player == "X" else "X"
        current_player_label.configure(text=f"Ход: {current_player}")


def check_winner():
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                     (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if buttons_state[condition[0]] == buttons_state[condition[1]] == buttons_state[condition[2]] is not None:
            return buttons_state[condition[0]]
    return None


def show_result(message):
    result_label = ctk.CTkLabel(root, text=message, font=("Arial", 30), fg_color='#3d319e', text_color='white', corner_radius=10)
    result_label.place(x=115, y=100)

    restart_button = ctk.CTkButton(root, text="Начать заново", command=start_game, width=300, height=50, corner_radius=10)
    restart_button.place(x=80, y=435)


def start_game():
    global current_player, buttons_state, buttons

    # Глобальные переменные для хранения состояния игры
    buttons_state = [None] * 9  # Сброс состояния кнопок
    buttons = []  # Сброс списка кнопок
    current_player = "X"  # Начинаем с крестиков

    # Очистка существующих виджетов
    for widget in root.winfo_children():
        widget.destroy()

    global current_player_label
    current_player_label = ctk.CTkLabel(root, text=f"Ход: {current_player}", font=("Arial", 40), fg_color='#3d319e', text_color='white', corner_radius=10)
    current_player_label.place(x=150, y=20)

    button_width = 150
    button_height = 60
    spacing_x = (500 - (button_width * 3)) // 4  # Горизонтальные промежутки
    spacing_y = (600 - (button_height * 3)) // 4  # Вертикальные промежутки

    for i in range(3):
        for j in range(3):
            button_number = i * 3 + j + 1  # Номер кнопки
            button = ctk.CTkButton(root, text="", fg_color='#2c2933', hover_color='#434049',
                                   command=lambda num=button_number: button_click(num), width=100, height=100)
            # Вычисление координат для размещения кнопки
            x = j * (button_width + spacing_x) + spacing_x
            y = (i * (button_height + spacing_y) + spacing_y) + 60  # Учитываем высоту метки
            button.place(x=x, y=y)  # Размещаем кнопку
            buttons.append(button)  # Добавляем кнопку в список


button = ctk.CTkButton(root, text="Начать игру", command=start_game, font=("ARIAL", 16), fg_color='#2c2933', hover_color='#434049')
button.configure(width=300, height=50)
button.pack(anchor=CENTER, expand=1)

root.mainloop()