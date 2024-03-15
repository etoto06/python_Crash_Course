a , b  = input().split()

a_str = int(a)
b_str = int(b)

a_str = int(str(a_str)[::-1])   #문자열로 변환해야 ::-1 뒤집기가 써져서 문자열로 바꾸고 다시 정수 
b_str = int(str(b_str)[::-1])

if (a_str < b_str):
    print(b_str)
else:
    print(a_str)


