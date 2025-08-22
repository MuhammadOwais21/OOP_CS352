from vehicle_interface import Vehicle

class Car(Vehicle):
    def fueling(self):
        return f"{self.name} is being fueled with petrol."

    def driving(self):
        return f"{self.name} is now driving smoothly on the road."