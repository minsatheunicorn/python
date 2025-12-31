import random
playing=True
number=random.randint(0,10)
print("i will guess a number from 0 to 9,and you will guess the correct number")
print("the game ends when you guess it correctly")
while playing:
    guess=int(input("give me your best guess"))
    if number==guess:
        print("you win the game the correct number was",number)
        break
    else:
        print("your guess is not correct plz try again")