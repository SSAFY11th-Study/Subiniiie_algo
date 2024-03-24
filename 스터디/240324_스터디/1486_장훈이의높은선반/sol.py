import sys
sys.stdin = open('input.txt')

def book_shelf(sum_height, i) :
    global height
    # 기저조건
    # 1. 키의 합이 선반 높이보다 큼
    if sum_height >= B :
        # 만든 총합이랑 height 비교
        # 만든 총합 제일 처음은 0
        # for i in range(N) :
        #   총합 + S[i]
        height = min(height, sum_height)
        return
    # 2. 모든 점원들을 합함
    if i == N :
        return
    # 재귀함수
    # 쌓았을 때
    book_shelf(sum_height + S[i], i + 1)
    # 안 쌓았을 때
    book_shelf(sum_height, i + 1)

T = int(input())
for tc in range(1, T+1) :
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    # 점원들의 키의 합
    height = 10000 * N + 1
    # 총합의 시작은 0
    # 0번째 사람부터 시작
    book_shelf(0, 0)
    print(f'#{tc} {abs(height-B)}')