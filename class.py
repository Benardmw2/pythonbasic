class Gari:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def desc(self):
        return f"{self.make} {self.model} {self.year}"

    def read(self):
        return f"This car has {self.odometer_reading} milage"

    def upt(self, milage):
        if milage >= self.odometer_reading:
            self.odometer_reading = milage
        else:
            print("You can't roll back an odometer")

    def incr(self, miles):
        self.odometer_reading += miles


mycar = Gari("toyota", "supra", 2012)
print(mycar.desc())
print(mycar.read())
mycar.upt(100)
print(mycar.read())
mycar.incr(50)
print(mycar.read())
