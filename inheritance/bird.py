class bird:
    def swim(self):
        print("swim faster")
class penguin(bird):
    def run(self):
        print("run faster")
peggy=penguin()
peggy.swim()
peggy.run()