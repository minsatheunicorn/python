from abc import ABC
class abcclass(ABC):
    def print(self,x):
        print("value of x",x)
    def task(self):
        print("hi")
class test(abcclass):
    def task(self):
        print("we are learning abstraction")
obj=test()
obj.task()
obj.print(100)