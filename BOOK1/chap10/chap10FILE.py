with open('name.txt', encoding='utf-8') as file:
    for line in  file:
        print(line)


import csv

with open('grade.csv') as file:
    reader = csv.reader(file)

    for line in reader:
        print(line)
    print(next(reader))

n= range(10)
print(n)
print(next(iter(n)))
print(next(iter(n)))
print(next(iter(n)))




for i in range(5):
    print(i)

# def add(a,b):
#     return a+b

# print('a', end='') #이렇게하면 print에도 엔터를 자동으로 안쳐줌

# print(line.rsplit()) # r , l 은 각각 오른쪽 왼쪽을 자름 

