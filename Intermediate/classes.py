class Car:
    amount_cars = 0

    def __init__(self, manufacturer, model, hp):
        self.manufacturer = manufacturer
        self.model = model
        self.hp = hp
        Car.amount_cars += 1

    def print_info(self):
        print(f"Manufacturer: {self.manufacturer}, Model: {self.model}, hp: {self.hp}")
    
    def print_car_amount(self):
        print(f"Total number of cars: {Car.amount_cars}")

    def __del__(self):
        print(f"Car {self.manufacturer} {self.model} has been destroyed")
        Car.amount_cars -= 1
    
myCar = Car("Tesla", "Model X", 525)
myCar.print_info()
mySecondCar = Car("Ford", "Mustang", 350)

myCar.print_car_amount()