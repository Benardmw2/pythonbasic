class Mpesa:
    def __init__(self, account_balance, phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number

    def send_money(self, amount, recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES Sent to {recipient}")
        else:
            print("Insufficient balance")


class Personal(Mpesa):
    def __init__(self, account_balance, phone_number, id_number):
        super().__init__(account_balance, phone_number)
        self.id_number = id_number

    def buy_airtime(self, amount):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES of airtime bought")
        else:
            print("Insufficient balance")


class Business(Mpesa):
    def __init__(self, account_balance, phone_number, business_name):
        super().__init__(account_balance, phone_number)
        self.business_name = business_name

    def receive(self, amount):
        self.account_balance += amount
        print(f"{amount} KES received successfully")


personal = Personal(555, 7895415, 18495623)
personal.send_money(400, 9851741)
personal.buy_airtime(20)
business = Business(2000, 78954126, "Bayview")
business.receive(500)
business.send_money(1500, 17563485)
