class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
 
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles


class Battery:

    def __init__(self, battery_size=40):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"이 차의 배터리 용량은 {self.battery_size}")

    def get_descriptive_name(self):
        print(super.get_descriptive_name())
        print(f"차량 배터리 크기는 {self.battery_size}")

    def get_range(self):
        if self.battery_size == 40:
            range = 150
        elif self.battery_size == 65:
            range = 225

class ElectricCar(Car):
    """전기차"""

    def __init__(self, make, model, year,large_battery):
        """전기 자동차에 고유한 속성을 초기화합니다"""
        super().__init__(make, model, year)
        self.battery = large_battery()

    def describe_battery(self):
        return(f"이 차 배터리 용량은 {self.battery.battery_size}")

    get_descriptive_name(self):


my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())
print(f"배터리 크기는 {my_leaf.def}")
my_leaf.battery.describe_battery()
my_car = Car('Bentz', 'E200' , 2023)
my_car.get_descriptive_name
print(f"차 제원은 {my_car.get_descriptive_name()}")
my_leaf.battery.describe_battery() # 하위 구성 객체 사용

large_battery = Battery(80)
large_battery_car = ElectricCar('nissan', 'leaf' , )
large_battery.battery.describe_battery()

#클래스 관련성
# 1.상속관계
# 2.has-a reletion
#   use relation
