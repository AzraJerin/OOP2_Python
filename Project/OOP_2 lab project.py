import numpy as np

# Encapsulation: Base Toy Class
class Toy:
    def __init__(self, name, price, quantity):
        self.name = name  # Public
        self._price = price  # Protected
        self.__quantity = quantity  # Private

    def get_quantity(self):  # Public method to access private attribute
        return self.__quantity

    def set_quantity(self, quantity):
        if quantity >= 0:
            self.__quantity = quantity
        else:
            raise ValueError("Quantity cannot be negative")

    def display_toy(self):
        return f"Name: {self.name}, Price: {self._price}, Quantity: {self.__quantity}"


# Single Inheritance
class ElectronicToy(Toy):
    def __init__(self, name, price, quantity, battery_type):
        super().__init__(name, price, quantity)
        self.battery_type = battery_type

    def display_toy(self):
        return f"{super().display_toy()}, Battery Type: {self.battery_type}"


# Multilevel Inheritance
class RemoteControlCar(ElectronicToy):
    def __init__(self, name, price, quantity, battery_type, range_in_meters):
        super().__init__(name, price, quantity, battery_type)
        self.range_in_meters = range_in_meters

    def display_toy(self):
        return f"{super().display_toy()}, Range: {self.range_in_meters} meters"


# Multiple Inheritance
class SoftToy:
    def __init__(self, material):
        self.material = material

    def display_material(self):
        return f"Material: {self.material}"


class HybridToy(RemoteControlCar, SoftToy):  # Hybrid inheritance
    def __init__(self, name, price, quantity, battery_type, range_in_meters, material):
        RemoteControlCar.__init__(self, name, price, quantity, battery_type, range_in_meters)
        SoftToy.__init__(self, material)


# Polymorphism: Method Overloading
class ToyManager:
    def calculate_total_cost(self, price, quantity):
        return price * quantity

    def calculate_total_cost(self, price, quantity, discount=0):  # Overloaded method
        return (price * quantity) * (1 - discount)


# Polymorphism: Method Overriding
class AdvancedToyManager(ToyManager):
    def calculate_total_cost(self, price, quantity, discount=0, tax=0):
        base_cost = super().calculate_total_cost(price, quantity, discount)
        return base_cost * (1 + tax)


# Custom Exception
class InvalidPriceException(Exception):
    def __init__(self, message="Price must be positive"):
        self.message = message
        super().__init__(self.message)


# Demonstrating NumPy Functions
def analyze_toy_data(prices):
    prices_array = np.array(prices)
    return {
        "Mean Price": np.mean(prices_array),
        "Median Price": np.median(prices_array),
        "Standard Deviation": np.std(prices_array),
        "Maximum Price": np.max(prices_array),
        "Minimum Price": np.min(prices_array),
    }


# Test the system
try:
    toy1 = Toy("Lego", 20, 100)
    print(toy1.display_toy())
    toy1.set_quantity(80)
    print(f"Updated Quantity: {toy1.get_quantity()}")

    rc_car = RemoteControlCar("RC Car", 50, 20, "AA", 100)
    print(rc_car.display_toy())

    hybrid_toy = HybridToy("Hybrid Toy", 100, 10, "AAA", 150, "Plush")
    print(hybrid_toy.display_toy())
    print(hybrid_toy.display_material())

    # Exception Handling
    try:
        invalid_toy = Toy("Invalid", -10, 5)  # Invalid price
    except InvalidPriceException as e:
        print(e)

    # NumPy
    prices = [20, 50, 100, 200, 300]
    analysis = analyze_toy_data(prices)
    print("Toy Data Analysis:", analysis)

    # Polymorphism in Action
    manager = AdvancedToyManager()
    total_cost = manager.calculate_total_cost(50, 3, discount=0.1, tax=0.05)
    print(f"Total Cost: {total_cost:.2f}")

except Exception as e:
    print(f"Error: {e}")