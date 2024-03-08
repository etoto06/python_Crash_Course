m = int(input())

list1 = input().split()[:m]
list1 = [int(x) for x in list1]

max = list1[0]
min = list1[0]

for num in list1:
    if num >max:
        max = num
    if num <min:
        min =num


print(min,max)


