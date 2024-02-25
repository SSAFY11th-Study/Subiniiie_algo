s = input()

result = []
stack = []
for i in s :
    if i == '(' :
        stack.append(i)
    else :
        a = stack.pop()
        if a == '(' :
            

