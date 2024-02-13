class Fruits:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def dispaly(self):
        print(f"My favourite fruit is {self.name} and it is Ksh.{self.price}")


obj = Fruits("Apple", 70)
obj.dispaly()
obj1 = Fruits("Orange", 50)
obj1.dispaly()
obj2 = Fruits("Watermelon", 120)
obj2.dispaly()
obj3 = Fruits("Banana", 60)
obj3.dispaly()
obj4 = Fruits("Pear", 120)
obj4.dispaly()
