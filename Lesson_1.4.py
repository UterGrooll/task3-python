print("Программа 'Длина числа'. Введите число, чтобы узнать, сколько в нём цифр.")
print("Для выхода введите 'exit'.")

while True:
    user_input = input("Введите число: ").strip()

    if user_input.lower() == "exit":
        print("Выход из программы...")
        break

    if user_input.replace('-', '', 1).isdigit():
        if user_input.count('-') > 1:
            print("Ошибка: число не может содержать более одного знака '-'!")
            continue
        digits = len(user_input.lstrip('-'))
        print(f"В этом числе {digits} цифры(а).")
    else:
        print("Ошибка: данные не являются корректным целым числом.")
