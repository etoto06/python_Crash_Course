class Dog:
    """개 표현 클래스"""

    def __init__ (self,name,age):
        #self는 생성된 객체 자기자신
        """name과 age속성 초기화"""
        self.name = name
        self.age = age
        self.__price = 100
        
    def sit(self):
        """앉기"""
        print(f"{self.name} is 앉기")

my_dog = Dog('willie',6)
 # 생성자 호출 >인스턴스 생성>__init__()함수가 자동 호출
my_dog.sit() #모든 클래스의 메소드는 self를 포함(여기선 my_dog)

print(f"개 이름은 {my_dog.name} + {my_dog.__price}")
your_dog = Dog('Lucy',3)
your_dog.sit()
print(f"너의 개는 {your_dog.name}")