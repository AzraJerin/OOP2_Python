# Base class Vehicle
class Vehicle:
    def _init_(self, color):
        self.color = color  # Public attribute

    def vehicleInfo(self):
        return f"Vehicle color: {self.color}"


# Derived class Taxi
class Taxi(Vehicle):
    def _init_(self, color, model, capacity, variant):
        super()._init_(color)  # Initialize the base class
        self.__model = model      # Private attribute
        self.__capacity = capacity
        self.__variant = variant

    # Getters
    def getModel(self):
        return self.__model

    def getCapacity(self):
        return self.__capacity

    def getVariant(self):
        return self.__variant

    # Setters
    def setModel(self, model):
        self.__model = model

    def setCapacity(self, capacity):
        self.__capacity = capacity

    def setVariant(self, variant):
        self.__variant = variant

    # Overriding vehicleInfo method
    def vehicleInfo(self):
        return (f"Taxi Details: Color: {self.color}, Model: {self.__model}, "
                f"Capacity: {self._capacity}, Variant: {self._variant}")


# Creating two instances t1 and t2
t1 = Taxi("Yellow", "Sedan", 4, "Luxury")
t2 = Taxi("White", "SUV", 7, "Premium")

# Display details
print(t1.vehicleInfo())
print(t2.vehicleInfo())

# Update details for t1
t1.setModel("Hatchback")
t1.setCapacity(5)
print(t1.vehicleInfo())