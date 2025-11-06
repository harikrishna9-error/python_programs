class car:
    def __init__(self,make,model,year,color):
        self.make=make
        self.model=model
        self.year=year
        self.color=color
        self.speed=0

car1=car("Toyata","camry",2022,"Red")
car2=car("Ford","Mustang",2023,"Black")
print(car1.make)
print(car2.speed)
