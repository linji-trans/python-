import random
bet = int(input("Lay your stakes: "))
money = 1000
while bet > 1000:
    print("Error!!You do not have enough money!!!")
    bet = int(input("Lay your stakes: "))
while bet <= 0:
    print("Error! Lay your stakes again!")
    bet = int(input("Lay your stakes: "))

if 0 < bet <= 1000:
    a = random.randrange(1, 7, 1)
    b = random.randrange(1, 7, 1)
    sum1 = a + b
    if sum1 == 7 or sum1 == 11:
        money = 1000 + bet
        print(a, b, "First chance, Player won!", "You have", money, "dollars now!")
    elif sum1 == 2 or sum1 == 3 or sum1 == 12:
        money = 1000 - bet
        print(a, b, "First chance, Player lost!", "You have", money, "dollars now!")
    else:
        money = 1000
        print(a, b, "You still have", money, "dollars!")

while money > 0:
    answer = input("Do you want to continue: ")
    if answer == "no" or answer == "No":
        print("Game over! You have", money, "dollars!")
        break
    else:
        print("Okay, let's continue!")
        bet = int(input("Lay your stakes: "))
        while bet > money:
            print("Error!!You do not have enough money!!!")
            bet = int(input("Lay your stakes: "))
        while bet <= 0:
            print("Error! Lay your stakes again!")
            bet = int(input("Lay your stakes: "))

        if 0 < bet <= money:
            a = random.randrange(1, 7, 1)
            b = random.randrange(1, 7, 1)
            sum = a+b
            if sum == 7:
                money = money - bet
                print(a, b, "Player lost!", "You have", money, "dollars now.")
            elif sum == sum1:
                money = money + bet
                print(a, b, "Player won!", "You have", money, "dollars now.")
            else:
                print(a, b, "You still have", money, "dollars!")

if money == 0:
    print("Sorry, you do not have enough money to play now.")

    

















