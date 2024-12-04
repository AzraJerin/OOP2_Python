class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display_detail(self):
        print("Product name:", self.name)
        print("Price:", self.price)


class ElectronicProduct(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name, price)
        self.warranty = warranty

    def display_detail(self):
        super().display_detail()
        print("Warranty:", self.warranty)


class Shape:
    def __init__(self, name):
        self.name = name

    def getname(self):
        return self.name

    def display(self):
        print("Shape name:", self.name)

    def display_info(self):
        self.display()


class Rectangle(Shape):
    def __init__(self, name, length, width):
        super().__init__(name)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)