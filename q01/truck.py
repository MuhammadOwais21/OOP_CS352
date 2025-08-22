from vehicle_interface import Vehicle

class Truck(Vehicle):
    def fueling(self):
        return f"{self.name} is being fueled with diesel."

    def driving(self):
        return f"{self.name} is hauling goods across the highway."