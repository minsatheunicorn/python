class vehicle:
    def __init__(self,name,max_speed,colour):
        self.name=name
        self.max_speed=max_speed
        self.colour=colour
class bus(vehicle):
    pass
object=bus("school bus",180,"beige")
print("vehicle name",object.name)
print("vehicle colour",object.colour)
print("speed of the veh",object.max_speed)