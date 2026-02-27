class category:
    def __init__(self, name, code):
        self.name = name
        self.code = code
        self.no_of_products = 0

    def __str__(self):
        return f"Category : {self.name} \n Code : {self.code} \n No. Of Products : {self.no_of_products}"

    def disctr(ctrlis):
        for prr in ctrlis:
            print(prr)


class product:
    def __init__(self, name, code, category, price):
        self.name = name
        self.code = code
        self.category = category
        self.price = price
        category.no_of_products += 1

    def __str__(self):
        return f"Name : {self.name} \n Code : {self.code} \n Category : {self.category.name} \n Price : {self.price}"

    def disproducts(products):
        print("-- All Products List --")
        for pr2 in products:
            print(f"Name : {pr2.name}, Price : {pr2.price}")

    def srtli(procucts):
        print("-- Sorted List --")
        products.sort(key=lambda x: x.price)
        for pr3 in products:
            print(f"Name : {pr3.name}, Price : {pr3.price}")

    def revli(products):
        print("-- Reverse List --")
        products.sort(key=lambda x : x.price, reverse=True)
        for pr4 in products:
            print(f"Name : {pr4.name}, Price : {pr4.price}")

    def search(prli, cde):
        for p in prli:
            if p.code == cde:
                return p
        return None


cars = category("Cars", 11)
electronics = category("Electronics", 22)
foods = category("Foods", 33)

products = [
    product("Ford Mustang", 111, cars, 45),
    product("BMW M6", 112, cars, 80),
    product("Tesla Model X", 113, cars, 25),
    product("Lamborghini Urus", 114, cars, 55),
    product("Nikon Z01", 221, electronics, 11),
    product("BenQ Projector", 222, electronics, 12),
    product("Gaming Laptop", 223, electronics, 32),
    product("Pizza", 331, foods, 5),
    product("Burger", 332, foods, 6),
    product("Frenchfries", 333, foods, 7),
]

for pr1 in [cars, electronics, foods]:
    print(pr1)
#print("-- All Products List --")
#for pr2 in products:
#    print(f"Name : {pr2.name}, Price : {pr2.price}")

#print("-- Sorted All Products List --")
#products.sort(key=lambda x: x.price)

#for pr3 in products:
#    print(f"Name : {pr3.name}, Price : {pr3.price}")

#print("-- Reverse Sorted All Products List --")
#products.sort(key=lambda x: x.price, reverse=True)

#for pr4 in products:
#    print(f"Name : {pr4.name}, Price : {pr4.price}")


#def search(prli, cde):
#    for p in prli:
#        if p.code == cde:
#            return p
#    return None

product.disproducts(products)

#srch = search(products, 1)
#if srch:
#    print(f"Product Found : {srch.name}")
#else:
#    print(f"Product Not Found")
product.srtli(products)

product.revli(products)

srch = product.search(products, 111)
if srch:
    print(f"Product Found : {srch.name}")
else:
    print("Product Not Found")