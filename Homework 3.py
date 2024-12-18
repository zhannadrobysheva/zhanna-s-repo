user_input = input("Введите строку: ")
if not user_input:
    exit() # Выход, если строка пуста
result = ""
count = 1
for i in range(1, len(user_input)):
    if user_input[i] == user_input[i - 1]:
        count += 1
    else:
        result += user_input[i - 1] + str(count) if count > 1 else user_input[i - 1]
        count = 1
result += user_input[-1] + str(count) if count > 1 else user_input[-1]
print(result)
