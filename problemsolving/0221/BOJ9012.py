#BOJ9012<괄호>
#스택 기본 개념

T = int(input())

def func(arr):
    vps = []
    for i in range(len(arr)):
        if arr[i] == '(':
            vps.append('(')
        else:
            if len(vps) == 0:
                return 'NO'
            else:
                vps.pop()
    else:
        if len(vps) != 0:
            return 'NO'
        return 'YES'

for _ in range(1, T+1):
    arr = list(input())
    print(func(arr))
