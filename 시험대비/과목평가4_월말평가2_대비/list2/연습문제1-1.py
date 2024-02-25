'''
5
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
5 4 3 2 1
1 2 3 4 5
'''
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

result = 0
for i in range(N) :
    for j in range(N) :
        temp = 0
        for k in range(4) :
            temp_x = i + dx[k]
            temp_y = j + dy[k]
            if 0 <= temp_x < N and 0 <= temp_y < N :
                temp += arr[temp_x][temp_y]
        result += temp

print(result)
