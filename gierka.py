import random

x = random.randint(0,100)


while True:
    n = int(input("Podaj liczbe"))
    if x > n:
        print("Za malo")
    elif x < n:
        print("Za duzo")
    else:
        print("W sam raz")
        break
