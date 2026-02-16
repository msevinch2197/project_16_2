import random

secret_number = random.randint(1, 100)
urinishlar = 0

print("Men 1 dan 100 gacha son o‘yladim. Topishga harakat qiling!")

while True:
    guess = int(input("Taxminingizni kiriting: "))
    urinishlar += 1

    if guess > secret_number:
        print("Katta")
    elif guess < secret_number:
        print("Kichik")
    else:
        print(f"To‘g‘ri! Siz {urinishlar} ta urinishda topdingiz!")
        break
