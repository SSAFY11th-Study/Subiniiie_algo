import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    result = []
    for i in range(N) :
        for j in range(M) :
            temp = arr[i][j]
            for k in range(4) :
                for w in range(arr[i][j]) :
                    temp_x = i + (dx[k] * (w+1))
                    temp_y = j + (dy[k] * (w+1))

                    if 0 <= temp_x < N and 0 <= temp_y < M :
                        temp += arr[temp_x][temp_y]
            result.append(temp)
    #         print(temp)
    # print(result)
    print(f'#{tc} {max(result)}')

