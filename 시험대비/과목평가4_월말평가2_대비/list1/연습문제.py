N = int(input())
box = list(map(int, input().split()))

result = []
for i in range(N) :
    cnt = 0
    for j in range(i+1, N) :
        if box[i] > box[j] :
            cnt += 1
    result.append(cnt)
print(max(result))

