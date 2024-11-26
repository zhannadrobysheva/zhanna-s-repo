stroka = input("Введите набор слов через пробел: ")  # Вводим слова через пробел
print(stroka)
slova = stroka.split()  # Разбиваем строку на слова
print(slova)
result = []  # Создаем новый список для хранения результатов

# Проходим по всем словам
for index, slovo in enumerate(slova):
    if index % 2 == 1:  # Если индекс четный
        result.append(slovo[::-1])  # Добавляем перевернутое слово в список
    else:
        result.append(slovo)  # Добавляем обычное слово в список
print(result)  # Выводим результат


