nums = input("Введите числа через пробел: ").split()

power = int(input("Введите степень: "))
result = []
for item in nums:
    if item.lstrip('-').isdigit():
        result.append(str(int(item) ** power))
    else:
        result.append(item * power)

print("Вывод:", " ".join(result))
