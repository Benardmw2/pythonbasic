class Cars:

    def __init__(self, make, model, year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def onyesha(self):
        print(f"This car is the {self.make}, {self.model} model manufactured in {self.year} in a {self.color} color.")
        # this is a comment


myobj = Cars("Toyota", "Supra", 2010, "blue")
myobj.onyesha()
myobj2 = Cars("BMW", "Mk series", 2020, "black")
myobj2.onyesha()
