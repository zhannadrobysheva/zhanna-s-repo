sentence = input("Введите предложение: ")
words = sentence.split()
for i in range(len(words) - 1, -1, -3):
  if i >= 0:
    print(words[i])