class Vehicle:
    brand = "TATA"
    def __init__(self,name,gears,cc):
        self.gears = gears
        self.cc = cc
        self.name = name
    
    @classmethod
    def change_brand(cls,brand):
        cls.brand = brand

    @property
    def print_details(self):
        print(f"The {self.brand} {self.name} comes with {self.gears} gears, {self.cc} engine")

altroz = Vehicle("Altroz",5,1500)
carens = Vehicle("Carens",6,1500)
carens.change_brand("KIA")

altroz.print_details
carens.print_details
print(Vehicle.brand)