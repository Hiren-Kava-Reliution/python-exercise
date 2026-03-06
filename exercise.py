class location:
    def __init__(self, name, code):
        self.name = name
        self.code = code

class product:
    def __init__(self, name):
        self.name = name
        self.stock_at_locations = {}

class movement:
    all_movements = []

    def __init__(self, from_location, to_location, product, quantity):
        from_stock = product.stock_at_locations.get(from_location, 0)

        if from_stock < quantity:
            raise ValueError(
                f"Not enough stock of {product.name} at {from_location.name}"
            )

        product.stock_at_locations[from_location] = from_stock - quantity
        product.stock_at_locations[to_location] = (
            product.stock_at_locations.get(to_location, 0) + quantity
        )

        self.from_location = from_location
        self.to_location = to_location
        self.product = product
        self.quantity = quantity

        movement.all_movements.append(self)

    @staticmethod
    def movements_by_product(product):
        result = []
        for m in movement.all_movements:
            if m.product == product:
                result.append(m)
        return result


loc1 = location("Rajkot", 1)
loc2 = location("Ahmedabad", 2)
loc3 = location("Surat", 3)
loc4 = location("Vadodara", 4)

locations = [loc1, loc2, loc3, loc4]

p1 = product("Motherboard")
p2 = product("SSD")
p3 = product("RAM")
p4 = product("Processor")
p5 = product("Monitor")

products = [p1, p2, p3, p4, p5]

for p in products:
    p.stock_at_locations[loc1] = 100

try:
    movement(loc1, loc2, p1, 10)
    movement(loc1, loc3, p2, 20)
    movement(loc1, loc4, p3, 30)
    movement(loc2, loc3, p1, 5)
    movement(loc1, loc2, p4, 150)
except Exception as e:
    print("Error:", e)

print("\n-- Movements by product --")
for p in products:
    print(p.name)
    moves = movement.movements_by_product(p)
    for m in moves:
        print(
            f"  {m.quantity} moved from : {m.from_location.name} to {m.to_location.name}"
        )

print("\n-- Product stock at locations --")
for p in products:
    print(p.name)
    for loc, qty in p.stock_at_locations.items():
        if qty > 0:
            print(f"  {loc.name}: {qty}")

print("\n-- Products by location --")
for loc in locations:
    print(loc.name)
    for p in products:
        qty = p.stock_at_locations.get(loc, 0)
        if qty > 0:
            print(f"  {p.name}: {qty}")
