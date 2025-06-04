name = input("Как вас зовут? ")
surname = input("А фамилия? ")
years_old = input("Сколько вам лет? ")

formatted_str = "Ваше имя: {0}, Фамилия: {1}, Возраст: {2} лет.".format(name, surname, years_old)
print("\n[Метод .format()]")
print(formatted_str)

f_str = f"Ваше имя: {name}, Фамилия: {surname}, Возраст: {years_old} лет."
print("\n[f-string]")
print(f_str)
