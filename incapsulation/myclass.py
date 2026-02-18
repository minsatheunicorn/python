class myclass:
    __privatevars=21
    def __privetemeth(self):
        print("i am in my class")
    def hello(self):
        print("private variable value",myclass.__privatevar)
obj=myclass()
obj.hello()
obj.__privetemeth()