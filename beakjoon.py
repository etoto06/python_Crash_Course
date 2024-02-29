# A,B = int(input().split())
# A = int(7)
# B = int(3)

# print(int(A+B) )
# print(int(A-B) )
# print(int(A*B)) 
# print(int(A/B))
# print(int(A%B) )

# A = input()
# 1 s.len(input())

#리스트의 생성 조회 수정 삭제 
# a=[1,2,3,4,5] #슬라이싱
# a[3:]

# a=[1,2,3,4,5]
# a[::-1] a[-1] a[:2] a[:3]

# s='abcde'
# s[::-1] , s[-1] , s[:3] ,s[3:]

# str = input("단어입력")
# number = int(input("정수 입력"))

# for i in [1,2,3,4,5]:
#     print(i)

# print('============================================')

# for s in 'abcdef':
#     print(s)

# print('============================================')

# for i in range(1,6):
#     print(i)

print('============================================')
# #list, tuple, str, range 를 for문에
# d = {1:'a',
#      2:'b',
#      3:'c',
#      4:'d',
#      5:'e'}

# for i in d:
#     print(i)
print('============================================')

# for i in range(1,6):
#     if (i % 2 == 0 and i %2 ==1 ): #이렇게 조건을 and나 or도 된다 
#       print(i) 
#     elif (i %3==0):
#         print(i)
#     else:
#        print(i ,'odd')
    
print('============================================')


# A,B = input().split()
# A,B = int(A),int(B)

# if (A > B ):
#     print(">")
# elif(A < B):
#     print("<")
# elif(A == B):
#     print('==')

print('============================================')
# a = int(input())


# if (a > 89 ):
#     print('A')
# elif(a > 79):
#     print('B')
# elif(a >69):
#     print('C')
# elif(a >59):
#     print('D')
# else:
#     print('F')
print('============================================')
# n = int(input())

# gugudan =list(range(1,10))

# for A in gugudan:
#     print(f"{n} * {A} = {n*A}")
print('============================================')
# s = input()  # '1 2' 문자열형태로 저장 
# a,b = s.split() # '1' '2' 공백기준으로 분리,두개의 문자열로 분리
# a,b = int (a), int (b) # 1 2 

# a , b =  int('1'), int ('2') #위에 3줄을 한줄로(같은뜻) 
# print(a,b)

# 20 10 35 30 7 이 나왔을떄 이중에서 젤 작은거 찾는법 알기
print('============================================')
# k= int(input())

# add = list(range(1,k+1))
# p = 0

# for addadd in add:
#     p += addadd
# print(p)
print('============================================')

m = int(input())

list1 = input().split()[:m]
list1 = [int(x) for x in list1]

big = index(max(list1))+1
small=list1.index(min(list1))+1

print( big , small )




    


