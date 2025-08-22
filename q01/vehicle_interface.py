
class Vehicle:
    def __init__(self, comp_name, model, name):
        self.comp_name = comp_name
        self.model = model
        self.name = name

    def fueling(self):
        print(f"{self.name} is being fueled.")

    def driving(self):
        print(f"{self.name} is now driving.")

    def show_info(self):
        print(f"{self.name} ({self.model}) by {self.comp_name}")
