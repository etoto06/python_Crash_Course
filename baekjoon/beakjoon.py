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

('============================================')

# for s in 'abcdef':
#     print(s)

('============================================')

# for i in range(1,6):
#     print(i)

('============================================')
# #list, tuple, str, range 를 for문에
# d = {1:'a',
#      2:'b',
#      3:'c',
#      4:'d',
#      5:'e'}

# for i in d:
#     print(i)
('============================================')

# for i in range(1,6):
#     if (i % 2 == 0 and i %2 ==1 ): #이렇게 조건을 and나 or도 된다 
#       print(i) 
#     elif (i %3==0):
#         print(i)
#     else:
#        print(i ,'odd')
    
('============================================')


# A,B = input().split()
# A,B = int(A),int(B)

# if (A > B ):
#     print(">")
# elif(A < B):
#     print("<")
# elif(A == B):
#     print('==')

('============================================')
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
('============================================')
# n = int(input())

# gugudan =list(range(1,10))

# for A in gugudan:
#     print(f"{n} * {A} = {n*A}")
('============================================')
# s = input()  # '1 2' 문자열형태로 저장 
# a,b = s.split() # '1' '2' 공백기준으로 분리,두개의 문자열로 분리
# a,b = int (a), int (b) # 1 2 

# a , b =  int('1'), int ('2') #위에 3줄을 한줄로(같은뜻) 
# print(a,b)

# 20 10 35 30 7 이 나왔을떄 이중에서 젤 작은거 찾는법 알기
('============================================')
# k= int(input())

# add = list(range(1,k+1))
# p = 0

# for addadd in add:
#     p += addadd
# print(p)
('============================================')

# m = int(input())

# list1 = input().split()[:m]
# list1 = [int(x) for x in list1]

# max = list1[0]
# min = list1[0]

# for num in list1:
#     if num >max:
#         max = num
#     if num <min:
#         min =num

# print(min,max)
('============================================')
# n이 주어졌을 때, 1부터 n까지 합을 구하는 프로그램을 작성하시오.
# 입력
# 첫째 줄에 n (1 ≤ n ≤ 10,000)이 주어진다. 3입력 6출력

# n=int(input())
# add = list(range(0,n+1)) 
# m=0
# added = 0
# for added in add:
#     m += added
# print(m)
('============================================')
# 총 N개의 정수가 주어졌을 때
# 정수 v가 몇 개인지 구하는 프로그램

# number = int(input())

# num1 = input(list(range(0,range)))

# num2 = input()
('============================================')

# a ,b ={} , []
# print (type(a),type(b))

# a = ['a',"b"]

# a['b']del

db = {
    1:['정원' , 'a+'],
    "english":"b",
    "science":"b"
    }
print(db)


for row in db.items():
    print(row)

for k,v in db.items():
    print(k,v,type(row)) # 튜플이 온다 

e = [3,2,1] 
print(e)

e.sort()   #위험한 sort , e값을 바꾼다 
print(e)

sorted(e)
print(e)

db = {
    1:['정원' , 'a+'],
    2 :'b',
    "science":"b"
    }

first = lambda x : x[0]
second = lambda x : x[1]

print(sorted(db.items(),key=second))



if 3 db in 

# 2557
# 1000
# 10869

# 1330
# 9498
# 2739
# 8393 ----------------------이까지o

# 10807
# 10871 
# 10818 o

# 3052
# 2675
# 1152
