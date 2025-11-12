medical_cause=input("did you have any medical cause(y or n)")
atendance=int(input("enter your attendance"))
if medical_cause=="y":
    print("yes you have premission")
else :
    if atendance>=75:
        print("have premission")
    else :
        print("dont have permission")