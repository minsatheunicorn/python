units=int(input("plz enter the number of units you consumed"))
if units<50:
 amount=units*2.6
 tax=25
elif units<=100 :
 amounts=units*3.25
 tax=35
elif units<=200 :
 amount=units*5.2
 tax=45
else :
 amount=units*8.4
 tax=55
total=units+tax
print("elecricity bills",total)