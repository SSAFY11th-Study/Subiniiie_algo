# 부분 집합 합 구하기

N = int(input())
arr = list(map(int, input().split()))

result = 0
for i in range(1, N+1) :
    for j in range(N) :
        if j + i < N :
            temp = arr[j:j+i]
            if sum(temp) == 0 :
                result += 1
if result >= 1 :
    print('pass')
else :
    print('fail')

