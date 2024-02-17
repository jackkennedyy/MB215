# Define the Car class with all requirements
class Car:
    def __init__(self, make, model, year):
        self.make = make
        self._model = model
        self.year = year

    def display_info(self):
        "A public method to display the car's information."
        print(f"Make: {self.make}, Model: {self._model}, Year: {self.year}")

    def _update_model(self, new_model):
        "A private method to update the car's model. Demonstrates encapsulation."
        self._model = new_model

    def __str__(self):
        "String representation of the Car object."
        return f"{self.year} {self.make} {self._model}"

# Function to compare two cars based on their year
def compare_car_years(car1, car2):
    if car1.year < car2.year:
        return f"{car1} is older than {car2}"
    elif car1.year > car2.year:
        return f"{car1} is newer than {car2}"
    else:
        return f"{car1} and {car2} are from the same year"

# Example usage
if __name__ == "__main__":
    car1 = Car("Toyota", "Corolla", 2021)
    car2 = Car("Honda", "Civic", 2024)
    
    # Display information for both cars
    car1.display_info()
    car2.display_info()
    
    # Update model of car1 and display again
    car1._update_model("Corolla Altas")
    print("\nAfter model update:")
    car1.display_info()

    # Compare the two cars
    print("\nComparing two cars:")
    print(compare_car_years(car1, car2))
