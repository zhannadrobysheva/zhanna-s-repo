def math_trick():
    print("Привет! Какое бы число ты ни ввёл, я превращу его в 4 с помощью простых математических операций.")
    
    # Запрашиваем число у пользователя
    user_input = int(input("Введите любое число: "))
    
    # Умножаем введённое число на 2
    step1 = user_input * 2
    print(f"Ваше число {user_input} умноженное на 2 равно {step1}")
    
    # Прибавляем к результату 8
    step2 = step1 + 8
    print(f"К результату {step1} прибавляем 8, получаем {step2}")
    
    # Делим результат на 2
    step3 = step2 / 2
    print(f"Результат {step2} делим на 2, получаем {step3}")
    
    # Отнимаем введённое число
    final_result = step3 - user_input
    print(f"Отнимаем ваше число {user_input} от {step3}, получаем {final_result}")
    
    # Финальный результат
    print("Как я и обещала, результат всегда будет равен 4!")

# Запускаем программу
math_trick()