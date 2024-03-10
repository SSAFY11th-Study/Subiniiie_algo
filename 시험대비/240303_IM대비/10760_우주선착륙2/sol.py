import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dx = [0, 1, 1, 1, 0, -1, -1, -1]
    dy = [1, 1, 0, -1, -1, -1, 0, 1]

    result_cnt = 0
    for i in range(N) :
        for j in range(M) :
            cnt = 0
            for k in range(8) :
                temp_x = i + dx[k]
                temp_y = j + dy[k]
                if 0 <= temp_x < N and 0 <= temp_y < M :
                    if arr[i][j] > arr[temp_x][temp_y] :
                        cnt += 1
            if cnt >= 4 :
                result_cnt += 1
    print(f'#{tc} {result_cnt}')