h=float(input("enter your height in cm"))
w=float(input("enter your weight in kg"))
bmi=w/(h/100)**2
print("your bmi is",bmi)
if bmi <= 18.4:
    print("you are underweight")
elif bmi <=24.9:
    print("you are healthy")    
else:
    print("you are overweight")