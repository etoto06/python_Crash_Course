class Car:
   
    def __init__(self, make, model, year):
        """차량 속성 초기화"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"이 차는  {self.odometer_reading}")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# my_used_car = Car('subaru', 'outback', 2019)
# print(my_used_car.get_descriptive_name())

# my_used_car.update_odometer(23_500)
# my_used_car.read_odometer()

# my_used_car.increment_odometer(100)
# my_used_car.read_odometer()
# class Car:
#     """자동차를 표현하는 클래스"""

#     def ___init__(self,make,model,year):
#         self.make = make
#         self.model = model
#         self.year = year

#     def get descriptive_name(self):
#     """뜻이 분명하고 깔끔한 이름 반환"""
#     long_name = f"{self.year} {self.make} {self.model}"
#     return long_name.title()

#     def read odometer(self):
#     """자동차의 주행거리를 출력합니다"""
#         self.odometer_reading += miles

#     class ElectricCar(Car):
#         """전기차"""
#         def __init__(self ,make,model,year,battery):
#             super().__init__(make,model,year)
#             self.battery_size = battery

#             def describe_battery(self):
#                 print(f"This car has a {self.battery_size}-kWh battery")

#     my_leaf = ElectricCar('nissan','leaf',2024)
#     print(my_leaf.get_descriptive_name())
#     print(f"배터리 크기는 {my_leaf.describe_battery()}")