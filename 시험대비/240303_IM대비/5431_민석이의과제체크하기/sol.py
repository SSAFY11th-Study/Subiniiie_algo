import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, K = map(int, input().split())
    jaechul = list(map(int, input().split()))

    result = []
    for num in range(1, N+1) :
        if num not in jaechul :
            result.append(num)

    result.sort()
    print(f'#{tc}', *result)
