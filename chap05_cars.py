cars = [ 'audi' , 'bmw' , 'subaru' , 'toyota' ]

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

print('\n===========================================\n')
requested_toppings = ['mushrooms' , 'onions', 'pineapple']
'mushrooms' in requested_toppings

age = 3
if age < 4 :
    print('입장료 0$')
elif age < 18:      #else if => elif
    print('입장료 25$')
else:
    print('입장료 50$')
print('\n===========================================\n')

available_toppings = ['mushroom', 'olives' , 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese' ]

requested_toppings = ['mushrooms' , 'onions', 'pineapple']

for requested_toppings in requested_toppings: #for문 = 반복문에 있는 변수 requested_toppings에 하나씩 토핑을 넣기 
    if requested_toppings in available_toppings: # == 'green peppers':
        print(f"Adding {requested_toppings}")
    else:
        print(f"Sorry, we don't have {requested_toppings}.")

print("\nFinished making your pizza!")
