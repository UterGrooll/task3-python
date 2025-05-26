# Ввод данных от пользователя
first_name = input("Введите имя: ")
last_name = input("Введите фамилию: ")
age = input("Ваш Возраст: ")

# Реализация через .format()
output_format = "Ваше имя: {}, Фамилия: {}, Возраст: {} лет".format(first_name, last_name, age)
print("\nРеализация через format:")
print(output_format)

# Реализация через f-string
output_fstring = f"Ваше имя: {first_name}, Фамилия: {last_name}, Возраст: {age} лет"
print("\nРеализация через f-string:")
print(output_fstring)
