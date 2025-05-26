user_input = input("Введите ваш возраст: ")

if user_input.isdigit():
    age = int(user_input)
    if age < 0:
        print("Ошибка: возраст не может быть отрицательным!")
    elif age >= 18:
        print("Вы совершеннолетний.")
    else:
        print("Вы несовершеннолетний.")
else:
    print("Ошибка: введено не число!")