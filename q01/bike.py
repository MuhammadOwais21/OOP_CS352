from vehicle_interface import Vehicle

class Bike(Vehicle):
    def fueling(self):
        return f"{self.name} is being fueled with petrol."

    def driving(self):
        return f"{self.name} is now cruising through traffic."