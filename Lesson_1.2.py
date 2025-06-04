def is_even(n):
    return n % 2 == 0

def get_positive_integer():
    while True:
        user_input = input("Введите целое положительное число: ")
        if not user_input.isdigit():
            print("Ошибка: введите целое положительное число.")
        elif int(user_input) <= 0:
            print("Ошибка: число должно быть больше нуля.")
        else:
            return int(user_input)

print("Проверка числа на чётность")
num = get_positive_integer()
if is_even(num):
    print(f"Число {num} является чётным")
else:
    print(f"Число {num} не является чётным")
