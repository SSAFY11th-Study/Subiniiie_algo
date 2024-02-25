N = int(input())
arr = list(map(int, input().split()))
temp = [0 for _ in range(N)]
counting = [0 for _ in range(N+1)]

for i in range(N) :
    counting[arr[i]] += 1

for j in range(1, len(counting)) :
    counting[j] += counting[j-1]

for k in range(len(arr)-1, -1, -1) :
    counting[arr[k]] -= 1
    temp[counting[arr[k]]] = arr[k]

print(temp)