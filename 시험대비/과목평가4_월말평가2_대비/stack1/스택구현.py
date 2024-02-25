'''
삽입 : push(append)
삭제 : pop
스택이 공백인지 아닌지 확인하는 연산 : isEmpty
스택의 pot에 있는 item(원소)을 반환하는 연산 : peek
'''

s = []
def push(item) :
    s.append(item)

push(6)
print(s)


def push(item, size) :
    global top
    top += 1
    if top == size :
        print('overflow!')
    else :
        stack[top] = item

size = 10
stack = [0] * size
top = -1

push(10, size)
top += 1
stack[top] = 20

def pop() :
    global top
    if top == -1 :
        print('underflow')
        return 0
    else :
        top = -1
        return stack[top+1]
print(pop())

if top > -1 :
    top -= 1
    print(stack[top+1])


