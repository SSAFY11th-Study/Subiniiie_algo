import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, numbers = map(str, input().split())

    alpha = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
    result = ''
    N = int(N)
    if N == 1:
        if numbers in '0123456789':
            numbers = int(numbers)
            while numbers >= 2:
                result += (numbers % 2)
                numbers = numbers // 2
            result += numbers
        else:
            for num in alpha.keys():
                if numbers == num:
                    numbers = alpha[num]
                    while numbers >= 2:
                        result += (numbers % 2)
                        numbers = numbers // 2
                    result += numbers
    else:
        for number in numbers :
            temp = ''
            if number in '0123456789':
                temp_num = int(number)
                while temp_num >= 2:
                    temp += str(temp_num % 2)
                    temp_num = temp_num // 2
                temp += str(temp_num)
                if len(temp) != 4:
                    temp += '0' * (4 - len(temp))
                    result = temp + result
                else:
                    result = temp + result
            else:
                for num in alpha.keys():
                    if number == num:
                        temp_num = alpha[num]
                        while temp_num >= 2:
                            temp += str(temp_num % 2)
                            temp_num = temp_num // 2
                        temp += str(temp_num)
                        if len(temp) != 4:
                            temp += '0' * (4 - len(temp))
                            result = temp + result
                        else:
                            result = temp + result
    print(f'#{tc} {result[::-1]}')






