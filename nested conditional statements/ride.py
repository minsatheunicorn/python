print("select your ride 1.bike 2.car")
choice=int(input("enter your choice"))
if choice==1 :
    print("what type of bike? 1.scooter 2.motorbike")
    choice2=int(input("enter your four the bike"))
    if choice2==1 :
        print("you've selected a scooter")
    else :
        print("you've selected a motorbike")
elif choice==2 :
    print("what type of car? 1.small 2.big")
    choice3=int(input("enter your four the car"))
    if choice3==1 :
        print("you've selected a small car")
    else :
        print("you've selected a gig car")
