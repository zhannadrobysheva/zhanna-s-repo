name = input("Введите строку: ")
f = 0
i = 0
for letter in name:
    if letter == "ф":
        f += 1
    if letter == "я":
        i += 1
print("Количество букв 'ф':", f)
print("Количество букв 'я':", i)