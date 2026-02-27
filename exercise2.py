class Category:
    def __init__(self, code, name, parent=None):
        self.code = code
        self.name = name
        self.parent = parent
        self.products = []
        self.disp = self.display()

    def display(self):
        if self.parent is None:
            return self.name
        else:
            return f"{self.parent.display()} > {self.name}"
    
    def __str__(self):
        return f"Code : {self.code}, Name : {self.name}, Total Product : {len(self.products)}"

class Product:
    def __init__(self, code, name, category, price):
        self.code = code
        self.name = name
        self.category = category
        self.price = price
        category.products.append(self)

    def __str__(self):
        return f"Product Code : {self.code}, Product Name : {self.name}, Product Category : {self.category}, Product Price : {self.price}"

vehicle = Category(1, "Vehicle")
car = Category(11, "Car", parent=vehicle)
bike = Category(12, "Bike", parent=vehicle)
petrol = Category(111, "Petrol", parent=car)
electric = Category(121, "Electric", parent=bike)

#Vehicles Product
products = [
    Product(101, "Truck", vehicle, 25000),
    Product(102, "Bus", vehicle, 31000),
    Product(103, "Helicopter", vehicle, 50000),
    Product(1101, "Tesla Model X", car, 13000),
    Product(1101, "Porsche", car, 18000),
    Product(1102, "BMW M7", car, 56000),
    Product(1201, "Royal Enfied", bike, 10000),
    Product(1202, "XPulse", bike, 15000),
    Product(1203, "Mazda", bike, 15360),
    Product(11101, "Inline", petrol, 41000),
    Product(11102, "V-Type", petrol, 51000),
    Product(11103, "Flat", petrol, 21000),
    Product(12101, "PMSM", electric, 12000),
    Product(12102, "Induction", electric, 11000),
    Product(12103, "EESM", electric, 10000)
    ]

all_categories = [vehicle, car, bike, petrol, electric]

for i in all_categories:
    print(i)
    for j in i.products:
        print(j)

sort = sorted(all_categories, key=lambda x : x.name)

for i in sort:
    print(f"Category : {i.name}")
    for j in i.products:
        print(f"{j.name}, {j.price}")