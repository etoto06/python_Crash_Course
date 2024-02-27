def greet_user(username):
    """단순한 인사말을 표시합니다""" #함수를 설명해주는거 주석같은것 
    print(f"hello! , {username}") #username은 스트링은 immutable 변수
    username = 'kim'

input_name = 'jesse'
greet_user(input_name)#함수 호출
input_name = 'kim' #값이 변경된게 아니라 다시 변수를 설정한것 
#주소를 출력해보면 다르게 나온다 
#immutable / mutable 개념을 알고있기 
print(input_name)
#help(greet_user) # 함수 실행은 안하고 """ """를 알려준다 (함수의 주석)
print(greet_user.__doc__) # 이걸 써도 똑같다

print('\n=========================================196p\n')


def describe_pet( pet_name , animal_type='dog' ): #값이 안나오면 dog를 쓴다 ,그리고 이처럼 기본값을 가지는 매개변수는 반드시 마지막에 와야한다 
    """반려동물 정보를 표시합니다"""
    print(f"\n I have a {animal_type}")
    print(f"my {animal_type}'s name is {pet_name.title()}")

describe_pet('harry') # 차례대로 
describe_pet(pet_name='harry')
describe_pet(pet_name='harry',animal_type='hamster') 
#순서대로 하기싫으면 키워드값 주면 된다 
print('\n=========================================203p\n')

def get_formatted_name(first_name, last_name , middle_name =''):
    """실제이름 반환"""
    if middle_name: #빈스트링(비어있으면)이면 FALSE로 간주
        full_name = f"{first_name}{middle_name}{last_name}"
    else: 
        full_name = f"{first_name} {last_name}"#자바처럼 타입 지정안해도 알아서함
    return full_name.title() 

musician = get_formatted_name('jimi' , 'handrix')
print(musician)
musician = get_formatted_name('jimi' , 'handrix','lee')
print(musician)

