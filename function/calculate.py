def add(p,q):
    return p+q
def subtract(p,q):
    return p-q
def multiply(p,q):
    return p*q
def divide(p,q):
    return p/q
choise=input("plz enter ur chioce,add,subtract,multiply,divide/")
n1=int(input("enter the first number"))
n2=int(input("enter the second number"))
if choise=="add":
    print("addition",add(n1,n2))
elif choise=="subtract":
    print("defencce",subtract(n1,n2))
elif choise=="multiply":
    print("product",multiply(n1,n2))
elif choise=="divide":
    print("quotient",divide(n1,n2))
