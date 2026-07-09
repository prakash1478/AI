class Ecommerce:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def display(self):
        return f"Product: {self.name}, Price: ${self.price}"


class Electronics(Ecommerce):
    def __init__(self, name, price, brand):
        super().__init__(name, price)
        self.brand = brand

    def display(self):
        return f"Product: {self.name}, Price: ${self.price}, Brand: {self.brand}"


class Clothing(Ecommerce):
    def __init__(self, name, price, size):
        super().__init__(name, price)
        self.size = size

    def display(self):
        return f"Product: {self.name}, Price: ${self.price}, Size: {self.size}"


# Creating objects
item1 = Electronics("Laptop", 1000, "Dell")
item2 = Clothing("T-shirt", 20, "M")

# Display details
print(item1.display())
print(item2.display())

# Checking object types

print(isinstance(item1, Electronics))  # True
print(isinstance(item2, Electronics))  # False
print(isinstance(item2, Clothing))     # True~