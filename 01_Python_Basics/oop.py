'''class Mobile():
    def __init__(self,brand, battery, ram, camera, price):
        self.brand = brand
        self.battery = battery
        self.ram = ram
        self.camera = camera
        self.price = price
    def display (self):
        print("Brand:", self.brand)
        print("Battery:", self.battery)
        print("Ram:", self.ram)
        print("Camera:", self.camera)
        print("price:", self.price)
obj1 = Mobile("apple", "5000mah", "12gb", "50mp", "90000")
obj1.display()
print("===================")
obj2 = Mobile("oneplus", "6000mah", "8gb", "64mp", "55000")
obj2.display()
print("===================")
obj3 = Mobile("nokia", "3000mah", "4gb", "32mp", "25000")
obj3.display()'''

'''class Laptop:
    def __init__(self, brand, ssd, g_card, price):
        self.brand = brand
        self.ssd = ssd
        self.g_card = g_card
        self.price = price

    def display(self):
        print("Brand:", self.brand)
        print("ssd:", self.ssd)
        print("g_card:", self.g_card)
        print("price:", self.price)    
obj = Laptop("MSI", "512gb", "8gb", 73000)
obj.display()'''

class Bank:
    def __init__(self, credit, withdrawl, loan, invest):
        self.credit = credit
        self.withdrawl = withdrawl
        self.loan = loan
        self.invest = invest
    def display(self):
        print("Credit:", self.credit)
        print("Withdrawl:", self.withdrawl)
        print("Loan:", self.loan)
        print("Invest:", self.invest)
obj = Bank(50000, 24000, 100000, 26000)
obj.display()