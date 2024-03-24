import sys
sys.stdin = open('input.txt')

def book_shelf(sum_height, cnt) :
    global height
    if sum_height >= B :
        height = min(height, sum_height)
        return
    if cnt == N :
        return
    book_shelf(sum_height + S[cnt], cnt + 1)
    book_shelf(sum_height, cnt + 1)
T = int(input())
for tc in range(1, T+1) :
    N, B = map(int, input().split())
    S = list(map(int, input().split()))
    height = 10000 * N + 1
    book_shelf(0, 0)
    print(f'#{tc} {abs(height - B)}')