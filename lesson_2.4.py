text = input("Введите строку: ").lower().split()
unique_words = set(text)

for word in unique_words:
    print(f"{word}: {text.count(word)}")
