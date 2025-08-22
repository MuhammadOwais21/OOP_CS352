from car import Car
from bike import Bike
from truck import Truck
import copy

def main():
    car1 = Car("Toyota", "2020", "Corolla")
    bike1 = Bike("Honda", "2022", "CD 70")
    truck1 = Truck("Ford", "2018", "CargoMaster")

    # Printing objects
    print(car1)
    print(bike1)
    print(truck1)

    # Calling methods
    print(car1.fueling())
    print(truck1.driving())

    # Copy vs Clone
    copy_car = copy.copy(car1)
    clone_car = copy.deepcopy(car1)

    print("Copy Car:", copy_car)
    print("Clone Car:", clone_car)

    # Array of vehicles
    vehicle_array = [car1, bike1, truck1]
    for vehicle in vehicle_array:
        print(vehicle.driving())

if __name__ == "__main__":
    main()