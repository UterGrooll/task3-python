list1 = list(map(int, input("Введите первый список: ").split()))
list2 = list(map(int, input("Введите второй список: ").split()))

common_elements = set(list1) & set(list2)
print("Общие элементы:", ' '.join(map(str, common_elements)))