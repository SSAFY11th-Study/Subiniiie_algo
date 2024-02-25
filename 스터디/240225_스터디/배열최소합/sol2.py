import sys
sys.stdin = open('input.txt')

def f(i, s, N) :
    global min_v
    if i == N :
        if min_v > s :
            min_v = s
    elif s > min_v :
        return
    else :
        for j in range(i, N) :
            p[i], p[j] = p[j], p[i]
            f(i+1, s+arr[i][p[i]], N)
            p[i], p[j] = p[j], p[i]

    return min_v

T = int(input())

for tc in range(1, T+1) :
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    min_v = 100
    p = [i for i in range(N)]

    print(f'#{tc} {f(0, 0, N)}')