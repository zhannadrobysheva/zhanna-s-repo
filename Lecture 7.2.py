cunning = input("Фамилии людей, которые получили надбавку за хитрость: ").split()
greed = input("Фамилии людей, которые получили надбавку за жадность: ").split()
# Преобразование списков в множества 
cunning_set = set(cunning)
greed_set = set(greed)
# Фамилии, получившие только одну надбавку
only_cunning = cunning_set - greed_set
only_greed = greed_set - cunning_set
# Количество людей, которые получили только одну из двух надбавок
people = len(only_cunning) + len(only_greed)
print("Количество людей, которые получили только одну надбавку: ", people)