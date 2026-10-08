class Vehicle:
    def __init__(self, companyName,model, enginHorse, price, color):
        self.companyName = companyName
        self.model = model
        self.enginHorse = enginHorse
        self.price = price
        self.color = color

    def printInfo(self):
        print("Company:", self.companyName)
        print("Engine Horsepower:", self.enginHorse)
        print("Price:", self.price)
        print("Color:", self.color)

    def compare(self, other):
        if self.price > other.price:
            print(self.companyName, "is more expensive")
        elif self.price < other.price:
            print(other.companyName, "is more expensive")
        else:
            print("Both vehicles have the same price")


        if self.enginHorse > other.enginHorse:
            print(self.companyName,"with",self.enginHorse, "horses is more powerfull")
        elif self.enginHorse < other.enginHorse:
            print(other.companyName,"with",other.enginHorse, "horses is more powerfull")
        else:
            print("Both vehicles have the same price")
        


car1 = Vehicle("BMW","series 3", 300, 50000, "Black")
car2 = Vehicle("Mercedes","c200", 250, 45000, "White")

car1.compare(car2)