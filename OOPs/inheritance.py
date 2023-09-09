class Vehicle():
    def __init__(self,seats,cc):
        self.seats = seats
        self.cc = cc
    def get_spec(self):
        print(f"The car has {self.seats} and comes with {self.cc} cc engine")

class Jaguar(Vehicle):
    def __init__(self):
        Vehicle.__init__(self,4,2500)


mycar = Jaguar()
mycar.get_spec()