from car import Car
class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.rented_cars = []

    def add_car(self, car):
        self.cars.append(car)

    def rent_car(self, car_id):
        for car in self.cars:
            if car.car_id == car_id and car.is_available:
                car.is_available = False
                self.rented_cars.append(car)
                return True
        return False

    def return_car(self, car_id):
        for car in self.rented_cars:
            if car.car_id == car_id:
                car.is_available = True
                self.rented_cars.remove(car)
                return True
        return False

    def list_available_cars(self):
        return [car for car in self.cars if car.is_available]

    def list_rented_cars(self):
        return self.rented_cars