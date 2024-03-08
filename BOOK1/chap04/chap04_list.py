# 파이썬의 자료구조 
# list , set , tuple , dict
# list = []   , set = {}   기호이다 
for value in range(6): 
    print(value)

print('\n============================================\n')

numbers = list(range(1,10,2)) # 여기서 2가 step
print(numbers)

print('\n=========================================106p\n')

squares = [] 
for value in range(1,11) :   #파이썬은 콜론이 블럭의 시작,기억하기
    #square = value **2       
    #squares.append(square)     아래처럼 바로쓰면 더 간결

    squares.append(value **2 )

print(squares)

print('\n==========================================107p\n')

squares = [value**2 for value 
in range(1,11)]  #106p 의 긴 코드를 이 한줄로 간결하게 가능 
print(squares)
print(squares[0:3])
print(squares)


print('\n==========================================\n')

my_list = [1,2,3,4,5,6]
print(my_list[::-1])
print(my_list[::-2])
print(my_list[::-3])

print('\n==========================================\n')

a = [1,2]
b = [3,4]
c = a + b 
print(c)

#d = a - b < 에러

c1=[x for x in a if x not in b]
c2=list(set(a)-set(b))
print(c1)
print(c2)  #두가지방법

print('\n==========================================\n')

#a = [[1,2,3],[4,5,6]]
#b = a #shallow copy 
# b = a[0:3] ###deep copy 
#a[0] = 100
#print(b) 
#print(a) 

print('\n==========================================\n')

a = [[1, 2, 3], [4, 5, 6]]
b = a  # shallow copy

a[0] = [100, 200, 300]  # 원본 객체 변경

print(a)  # [[100, 200, 300], [4, 5, 6]]
print(b)  # [[100, 200, 300], [4, 5, 6]]

print('\n==========================================\n')
import copy

a = [[1, 2, 3], [4, 5, 6]]
b = copy.deepcopy(a)  # deep copy

a[0] = [100, 200, 300]  # 원본 객체 변경

print(a)  # [[100, 200, 300], [4, 5, 6]]
print(b)  # [[1, 2, 3], [4, 5, 6]]

print('\n==========================================\n')

players = ['charles' , 'martina' , 'michael' ,'floreance','eli']

print("mt team")
for player in players[:3]:
    print(player.title())
print('\n==========================================\n')
my_foods = ['pizza' , 'falafel' , 'carrot cake']
#friend_foods = my_foods  [:] #deep copy
friend_foods = my_foods  #shallow copy

my_foods.append('cannoli')

print(my_foods)
print(friend_foods)

print('\n=======================================114p\n')

dimensions=(10,20,30,40,50)  # 대괄호가 아니라 일반괄호를 쓰면 튜블로 선언 
#dimensions[0]=30
print(dimensions)

for dimensions in dimensions:
    print(dimensions)

dimensions = (200,50)
print(dimensions)  #튜블은 언제든지 재선언해서 사용 가능하다 

print('\n===========================================\n')




