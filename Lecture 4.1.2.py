a = int(input())
if a % 4 == 0:
    if a % 100 != 0:
        print("да")
    else:
        if a % 400 == 0:
            print("да")
        else:
            print("нет")
else:
    print("нет")