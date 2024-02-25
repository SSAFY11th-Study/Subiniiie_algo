arr = list(map(int, input().split()))

stack = []
def DFS(s) :
    global stack
    stack.append(s)

    while stack :
        now = stack.pop()
        visited[now] = 1

        for next in range(1, 11) :
            if not visited[next] and adjl[now][next] :
                stack.append(next)

visited = [0 for _ in range(len(arr)+1)]
adjl = [[0 for _ in range(11)] for _ in range(11)]

for i in range(len(arr)//2) :
    adjl[arr[i*2]][arr[i*2+1]] = 1
    adjl[arr[i*2+1]][arr[i*2]] = 1

DFS(1)