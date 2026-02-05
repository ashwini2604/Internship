#multilevel inheritance
class Product:
    def __init__(self, product_name, price):
        self.product_name = product_name
        self.price = price

    def display_product(self):
        print("Product:",self.product_name)
        print("Price:",self.price)

class ElectronicProduct(Product):
    def __init__(self, product_name, price, brand, warranty):
        super().__init__(product_name, price)
        self.brand = brand
        self.warranty = warranty

    def display_electronic_product(self):
        self.display_product()
        print("Brand:",self.brand)
        print("Warranty:",self.warranty)

class MobilePhone(ElectronicProduct):
    def __init__(self, product_name, price, brand, warranty, ram, storage):
        super().__init__(product_name, price, brand, warranty)
        self.ram = ram
        self.storage = storage

    def display_mobile_details(self):
        self.display_electronic_product()
        print("RAM:",self.ram)
        print("Storage:",self.storage)

my_mobile = MobilePhone("Galaxy S24", 899, "Samsung", "2 Years", 12, 256)
my_mobile.display_mobile_details()