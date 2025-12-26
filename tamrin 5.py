class Vehicle:
    def __init__(self ,brand ,year ):
        self.brand = brand
        self.year = year

    def display_info(self):
        print(f"year: {self.year}")
        print(f"brand: {self.brand}")

class Car (Vehicle) :
    def __init__(self ,brand ,year ,num_doors):
        super().__init__(brand ,year)
        self.num_doors = num_doors

    def display_info(self):
        super().display_info()
        print(f"num_doors : {self.num_doors}")    

class Motorcycle (Vehicle) :
    def __init__(self ,brand ,year ,has_sidecar):
        super().__init__(brand ,year)
        self.has_sidecar = has_sidecar

    def display_info(self):
        super().display_info()
        print(f"has_sidecar : {self.has_sidecar}") 

v1 = Vehicle("Dodge", 2023)
print("Vehicle Info:")
v1.display_info()

c1 = Car("Dodge Challenger", 2023, 2)
print("Car Info:")
c1.display_info()

m1 = Motorcycle("Dodge", 2023, False)
print("Motorcycle Info:")
m1.display_info()