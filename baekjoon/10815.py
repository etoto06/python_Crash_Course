x = int(input())
numcard = list(map(int, input().split()))

m = int(input())
mNUM = list(map(int, input().split()))

result = []
for num in mNUM:
    if num in numcard:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
        result.append(1)
    else:
        result.append(0)

# 결과 출력
print(' '.join(map(str, result)))



