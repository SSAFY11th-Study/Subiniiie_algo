# 더 짧은 코드

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, numbers = map(str, input().split())

    N = int(N)
    alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F':15}
    result = ''
    for i in range(N) :
        temp = ''
        if numbers[i] in '0123456789' :
            number = int(numbers[i])
        else :
            for key in alpha.keys() :
                if numbers[i] == key :
                    number = int(alpha[key])
        while number >= 2 :
            temp += str(number % 2)
            number = (number // 2)
        temp += str(number)
        if len(temp) != 4 :
            temp += '0' * (4 - len(temp))
        result = temp + result

    print(f'#{tc} {result[::-1]}')
