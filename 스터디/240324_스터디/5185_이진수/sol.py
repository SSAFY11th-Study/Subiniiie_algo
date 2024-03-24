import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1) :
    N, numbers = map(str, input().split())

    N = int(N)
    result = ''
    alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    for i in range(N) :
        if numbers[i] in '0123456789' :
            number = int(numbers[i])
        else :
            for key in alpha.keys() :
                if numbers[i] == key :
                    number = int(alpha[key])
        temp = ''
        while number >= 2 :
            temp += str(number % 2)
            number = (number // 2)
        temp += str(number)

        if len(temp) != 4 :
            temp += '0' * (4 - len(temp))

        result = temp + result
    print(f'#{tc} {result[::-1]}')

# 16진수 -> 8진수
# 16 -> 10 -> 8
    for i in range(N) :
        if numbers[i] in '01234567' :
            number = int(numbers[i])
        else :
            for key in alpha.keys() :
                if numbers[i] == key :
                    number = int(alpha[key])
        temp = ''
        while number >= 8 :
            temp += str(number % 8)

