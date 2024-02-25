'''
7
4 3 6 1 2 5 2
'''
N = int(input())
arr = list(map(int, input().split()))

for i in range(N-1, -1, -1) :
    for j in range(0, i) :
        if arr[j] > arr[j+1] :
            arr[j], arr[j+1] = arr[j+1], arr[j]
print(arr)