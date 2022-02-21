#BOJ10828<스택>
#스택 기본 개념
T = int(input())

arr = [list(input().split()) for _ in range(T)]
stack = [0] * 10000
top = -1
for i in range(len(arr)):
    if arr[i][0] == 'push':
        top += 1
        stack[top] = int(arr[i][1])
    elif arr[i][0] == 'pop':
        if top == -1:
            print(-1)
        else:
            print(stack[top])
            top -= 1
    elif arr[i][0] == 'size':
        print(top+1)
    elif arr[i][0] == 'empty':
        if top == -1:
            print(1)
        else:
            print(0)
    elif arr[i][0] == 'top':
        if top == -1:
            print(top)
        else:
            print(stack[top])
