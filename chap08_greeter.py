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



