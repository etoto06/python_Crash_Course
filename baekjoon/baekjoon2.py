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
# number = int(input())
# card = list(map(int , input().split()))

# number2 = int(input())
# card2 = list(map(int, input().split()))

# lst = input().split()
# print(lst)

# d1['6']=0


# for x in range(5):
#     for y in range(10):
#         print(x,y)

# if x < 5:
#     print('low')
# else :
#     print('high')


# d1 = {
#     'a': {
#         'aa':1,
#         'aa1':2
#     },
#     'b' : {
#         'bb':3,
#         'bbb':4
#     }
# }
# print(d1)


db2 = {}
db2['a'] = list()

db2['a'].append('3')



db3 = {}
db3['b'] = list()


def add(a,b):
    return a+b

add(1,2)


data={
    'a':1,
    'b':2
}
print(data)

print(add(**data))
print(data) 


print([x**2 for x in range(5) if x%2 ==0])


# def pow(n):
#     lst=[]
#     for x in range(n):
#         if x%2 ==0:
#             lst append(x**2)


num = 1
while num < 5:
    print("작다")
    num += 1 


from pickle import TRUE
n=0
b_N =True

while b_N:
    print(n)
    n +=1
    #if n==5
    # n_N = False
    if n==5:
        continue
    else:
        break

# //a의 값을 빼서 b에 넣기
# a = [1,2,3]
# b = []
# N = len(a)

# for i in a:
#     p = a.pop
#     b.append(p)

# print(a,b)



# a = [1,2,3]
# b = []
# n = 0
# while a.:
#     p = a.pop()
#     b.append(p)
    

# print(a , b)



# q = [1,2,3]
# w = []
# n = 0
# while True:
#     if not q:break
#     p = q.pop()
#     w.append(p)
    

# print(q , w)


a = [1,2,3,2,3]
a.remove(2)
print(a)


d1 ={}
d1['steve'] = list(map(int , input().split))
print(d1)


# --------------------------------

# for 
# if
# data 
# 1)변형, map("f",data)
# 2)조건, filter("f",data)
# 3)줄인다 res?뭐시기 


square = lambda x : x**2
square(2) 



list(map(square,data))

list(filter(even,data))