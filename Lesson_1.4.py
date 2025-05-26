print("Выход из программы exit")
while True:
    user_input = input("Введите число: ")

    if user_input.lower() == "exit":
        print("Выход из программы...")
        break

    if user_input.lstrip('-').isdigit():
        number = user_input.lstrip('-')
        print(f"В этом числе {len(number)} цифры.")
    else:
        print("Ошибка: данные не являются числом.")
