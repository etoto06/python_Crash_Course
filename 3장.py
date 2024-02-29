motocycles = [ 'honda' , 'ducati' , 'yamaha' , 'suzuku' , 'ducati']
print(motocycles)

too_expensive = 'ducati'
motocycles.remove(too_expensive)
motocycles.remove(too_expensive)
print(motocycles)
print(f"\nA { too_expensive.title()} is too expensive for me.")


print('============================================'.title())

cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(cars)
cars.sort()  #리스트 자체를 수정, 알파벳순으로
# cars.sort(reverse=True) #이렇게하면 알파벳 역순으로  
print(cars)



print('============================================'.title())

#임시로 정렬하는 sorted() 함수 , 원하는 순서로 표시하지만 실제 순서는 안바뀜 
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(sorted(cars))
print(cars)

print('============================================'.title())
#리스트의 길이 확인하기 len
cars = ['bmw' , 'audi' , 'toyota' , 'subaru']
print(len(cars))
print(cars(-1))


