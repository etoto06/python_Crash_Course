#for문 
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
for car in cars: #자바에서 확장형 for문 
    print(car)
    print(f"my car is a {car}") #들여쓰기 한 것이 다 for문  
print("리스트 출력 완료 ")    

print('============================================')

for car2 in cars:
    print('my car\n')
    for c2 in cars:
        print()  #102페이지 해보기 
print("for문 종료")

print('============================================')
magicians = ['alice' , 'david' , 'carolina']
for magicians in magicians:
    print()
           