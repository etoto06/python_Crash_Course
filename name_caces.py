name = 'kdh'
message = f'안녕하세요 {name}'

print(message.title())
print(name.title())

print(name.upper())
print(name.lower())
print(name.capitalize())

message1 = '명언입니다, "명언입니다명언입니다" '

print(message1.title())

bicycles = ['trek' , 'cannondale' , ' redline' , 'specialized']
print(bicycles[-3]) #마이너스는 뒤에서 n번째 이다

del bicycles[0]
print(bicycles)

popped_bicycles = bicycles.pop()

print(bicycles)

print(popped_bicycles)

#사용 예시
last_owned = bicycles.pop()
print(f"the last bicycle I owned was a {last_owned.title()}")
