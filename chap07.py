# def test():
#     return (10,20)

# a,b = test()  #튜플값을 리턴
# print( f"a={a},b={b}")
# lst = ['a','b','c','d']
# for i , value in enumerate(lst): #enumrate() 함수가 튜플을 리턴한다 
#     print(f"i={i}, value ={value}")
('============================================')

# def get_formattes_name(first_name , last_name);
#     """실제 이름을 깔끔한 형식으로 반환"""
#     full_name = f"{first_name} {last_name}"
#     return full_name.title() # 풀네임이 첫이름과 마지

# while True:
#     print ("\nPlease tell me your name:")

#     f_name = input ("first name: ")
#     if f_name =='q':
#         break

#     l_name = input ("Last name: ")
#     if l_name =='q':
#         break

('============================================')
# # 함수에 list 컨트롤 
# #  ->함수내에서 수정가능

# def print_models(unprinted_designs,conpleted_models):
#     """빈리스트 일 때 까지 출력"""
# while unprinted_designs: #빈 리스트면 false 
#     current_design = unprinted_designs.pop() #un에서 가장 마지막요소 꺼내서 cu에 넣기,한개씩 삭제 
#     print(f"Printing model: {current_design}")
#     completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe 완료")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def modify_string(s):##string값을 전달받았다
#     ##immutable 변수는 튜플,숫자,스트링,불리언  
#     s = s+ "world" ##변수 s가 원래 변수가 가리키는 주소와 다름
#     print(s)

# st = "hello"
# modify_string(st)
# print(st) ## 출력결과가  hello =>변경안됨
('============================================')

# def print_models(unprinted_designs, completed_models):
#     """빈 리스트일 때까지 출력"""
#     while unprinted_designs:
#         current_design = unprinted_designs.pop()
#         print(f"Printing model: {current_design}")
#         completed_models.append(current_design)

# def show_completed_models(completed_models):
#     print("\nThe 완료")
#     for completed_model in completed_models:
#         print(completed_model)

# unprinted_designs = ['phone case', 'robot pendant', 'robot pendant', 'dodecahedron']
# completed_models = []

# print_models(unprinted_designs, completed_models)
# show_completed_models(completed_models)

# def modify_string(s):
#     s = s + "world"
#     return s

# st = "hello"
# st = modify_string(st)
# print(st)
('============================================')
#일련의 짧은 문자메세지 포함하는 리스트 만들기 
#이 리스트를 show_messages()함수에 전달해 각 메세지 출력 파이썬으로 쉽게

# def show_messages():
#     for message in messages:
#         print (message)

# messages =['안녕' '반갑습니다' '잘가' ]

# show_messages()

# send = messages.pop()

# send_messages = []

# send_messages.append(send)

print(send_messages)
('============================================')

def make_pizza(*toppings):
    """리스트출력"""
    print(toppings)
    for topping in toppings:
        print(f"-{topping}")

make_pizza('pepperoni')
make_pizza('mushroom', 'green peppers', 'extra cheese')
('============================================')
