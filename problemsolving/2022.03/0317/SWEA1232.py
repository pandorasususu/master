#1232. [S/W 문제해결 기본] 9일차 - 사칙연산

tc = 10

def solve(v):
    if v:
        solve(c1[v])
        solve(c2[v])
        stack.append(value[v])
        if type(value[v]) == str:
            if stack[-1] in '+-*/':
                if value[v] == '+':
                    stack.pop()
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b+a)
                elif value[v] == '-':
                    stack.pop()
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b-a)
                elif value[v] == '*':
                    stack.pop()
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b*a)
                elif value[v] == '/':
                    stack.pop()
                    a = stack.pop()
                    b = stack.pop()
                    stack.append(b/a)

def solve2(vv):
    if vv:
        solve2(c1[vv])
        solve2(c2[vv])
        print(value[vv], end=' ')


for _ in range(1, tc+1):
    n = int(input())
    value = [0] * (n+1)
    parent = [i for i in range(n+1)]
    c1 = [0] * (n+1)
    c2 = [0] * (n+1)
    for idx in range(n):
        node, *rest = input().split()
        node = int(node)
        if rest[0] in '+-*/':
            value[node] = rest[0]
        else:
            value[node] = int(rest[0])

        if len(rest) != 1:
            rest[1], rest[2] = map(int, rest[1:])
            if not c1[node]:
                c1[node] = rest[1]
                c2[node] = rest[2]
    stack = []
    solve(1)
    print(f'#{_} {int(stack[0])}')
