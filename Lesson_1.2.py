user_input = input("Введите число: ")

if user_input.isdigit():
    number = int(user_input)
    if number % 2 == 0:
        print(f"Число {number} является четным")
    else:
        print(f"Число {number} не является четным")
else:
    print("Ошибка: введено не число")
