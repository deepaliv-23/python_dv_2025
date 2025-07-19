class akshu:
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    def car(self):
        print(f"my brand name is {self.brand} my model {self.model}")
mycar = akshu("Thar","Mahindra")
print(mycar.brand)
print(mycar.model)
print(mycar.car())

        