import random
while True:
    user_action=input("enter a choice,rock,scissors,paper-")
    possible_action=["rock","paper","scissors"]
    computer_action=random.choice(possible_action)
    print("you choose ",user_action , "compueter choose",computer_action)
    if user_action==computer_action:
        print("both pairs selected",user_action,"its a tie")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("u WIN")
        else:
            print("u LOOSE")
    elif user_action=="paper":
        if computer_action=="rock":
            print("u WIN")
        else:
            print("u LOOSE")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("u WIN")
        else:
            print("u LOOSE")