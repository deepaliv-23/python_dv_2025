class car_1:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model
    def car(self):
        print(f"my brand name is {self.__brand} my model {self.model}")



        
mycar = car_1("Mahindra","thar")
# print(mycar.brand)
# print(mycar.model)
print(mycar.car())