# 반복문으로 하고 싶엇으나 하지 못했다...


import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, B = map(int, input().split())
    S = list(map(int, input().split()))

    S.sort(reverse=True)

    result = 0
    for i in range(len(S)) :
        result += S[i]
        if result == B :
            print(f'#{tc} 0')
            break
        elif result > B :
            for j in range(len(S) - 1, i - 1, -1) :
                if result - S[i] + S[j] >= B :
                    print(f'#{tc} {abs(result - S[i] + S[j] - B)}')
                    break
            break


