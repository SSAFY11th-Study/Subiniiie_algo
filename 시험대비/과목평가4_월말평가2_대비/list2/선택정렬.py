'''
10
4 3 1 2 7 6 9 0 8 5
'''
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1) :
    min_idx = i
    for j in range(i+1, N) :
        if arr[min_idx] > arr[j] :
            min_idx = j
    arr[min_idx], arr[i] = arr[i], arr[min_idx]
print(arr)