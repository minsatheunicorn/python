amount=int(input("plz enter the amount"))
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)//50)//10
print("number of 100 rupes notes",note1)
print("nuber of 50 rupes notes",note2)
print("number of 10 rupes notes",note3)