import tkinter as tk
from tkinter import messagebox, simpledialog
from car_rental_system import CarRentalSystem

class CarRentalGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Car Rental System")

        self.rental_system = CarRentalSystem()

        self.label = tk.Label(self.root, text="Car Rental System")
        self.label.pack()

        self.add_car_button = tk.Button(self.root, text="Add Car", command=self.add_car)
        self.add_car_button.pack()

        self.show_available_cars_button = tk.Button(self.root, text="Show Available Cars",
                                                    command=self.show_available_cars)
        self.show_available_cars_button.pack()

        self.show_rented_cars_button = tk.Button(self.root, text="Show Rented Cars", command=self.show_rented_cars)
        self.show_rented_cars_button.pack()

        self.rent_car_button = tk.Button(self.root, text="Rent a Car", command=self.rent_car)
        self.rent_car_button.pack()

        self.return_car_button = tk.Button(self.root, text="Return a Car", command=self.return_car)
        self.return_car_button.pack()

        self.quit_button = tk.Button(self.root, text="Quit", command=self.root.destroy)
        self.quit_button.pack()

        self.root.mainloop()

    def add_car(self):
        car_id = simpledialog.askstring("Add Car", "Enter Car ID:")
        model = simpledialog.askstring("Add Car", "Enter Car Model:")
        brand = simpledialog.askstring("Add Car", "Enter Car Brand:")
        year = simpledialog.askinteger("Add Car", "Enter Car Year:")

        if car_id and model and brand and year:
            from car import Car
            car = Car(car_id, model, brand, year)
            self.rental_system.add_car(car)
            messagebox.showinfo("Success", "Car added successfully!")

    def show_available_cars(self):
        available_cars = self.rental_system.list_available_cars()
        self.show_cars("Available Cars", available_cars)

    def show_rented_cars(self):
        rented_cars = self.rental_system.list_rented_cars()
        self.show_cars("Rented Cars", rented_cars)

    def rent_car(self):
        car_id = simpledialog.askstring("Rent a Car", "Enter Car ID:")
        if car_id:
            if self.rental_system.rent_car(car_id):
                messagebox.showinfo("Success", "Car rented successfully!")
            else:
                messagebox.showerror("Error", "Car not available or ID not found.")

    def return_car(self):
        car_id = simpledialog.askstring("Return a Car", "Enter Car ID:")
        if car_id:
            if self.rental_system.return_car(car_id):
                messagebox.showinfo("Success", "Car returned successfully!")
            else:
                messagebox.showerror("Error", "Car not rented or ID not found.")

    def show_cars(self, title, cars):
        cars_str = "\n".join([f"{car.car_id}: {car.brand} {car.model} ({car.year})" for car in cars])
        messagebox.showinfo(title, cars_str)


if __name__ == "__main__":
    CarRentalGUI()