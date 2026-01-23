class Car:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

    def drive(self):
        print(self.brand, "is driving at", self.speed)


c1 = Car("Tesla", 120)
c2 = Car("BMW", 150)

c1.drive()
c2.drive()
