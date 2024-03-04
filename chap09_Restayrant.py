class Restaurant:
    def __init__(self, rname , rtype):
        self.restaurant_name=rname
        self.cuisine_type=rtype

    def describe_restaurant(self):
        print(f"레스토랑 이름: {self.restaurant_name} {self.cuisine_type}")
    def open_restaurant(self):
        print(f"레스토랑이 문들 열었습니다: {self.restaurant_name}")

new_rest = Restaurant("새로운 레스토랑" , "한식")
# print(f"레스토랑 이름과 타입 {} {}")  
new_rest.describe_restaurant()

