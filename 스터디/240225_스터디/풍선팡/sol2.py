import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]

    max_num = 0
    for i in range(N) :
        for j in range(M) :
            flower = arr[i][j]
            for w in range(4) :
                for k in range(1, arr[i][j]+1) :
                    temp_x = i + (dx[w] * k)
                    temp_y = j + (dy[w] * k)
                    if 0 <= temp_x < N and 0 <= temp_y < M :
                        flower += arr[temp_x][temp_y]

            # i, j는 고정
            if max_num < flower :
                max_num = flower
    print(f'#{tc} {max_num}')