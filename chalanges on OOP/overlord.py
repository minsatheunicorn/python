class A:
    def __init__(self,x):
        self.x=x
    def __lt__(self,other):
        if(self.x<other.x):
            return "ob1 is less than ob2"
        else:
            return "ob2 is less than ob1"
ob1=A(21)
ob2=A(18)
print("past values",ob1.x)
print(ob1<ob2)