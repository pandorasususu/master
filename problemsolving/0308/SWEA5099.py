#SWEA5099

def pizza(arr):
    global result
    Q = []
    p = arr.pop(0)
    Q.append(p)

    while Q:
        if len(arr) == 0 and len(Q) == 1:
            result = Q[0][0]
            return
        elif len(arr) != 0 and len(Q) < N:
            Q.append(arr.pop(0))
        else:
            last = Q.pop(0)
            last[1] //= 2
            if last[1] == 0:
                continue
            else:
                Q.append(last)

t = int(input())

for _ in range(1, t+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    for i in range(M):
        arr[i] = [i, arr[i]]
    result = 0

    pizza(arr)
    print(f'#{_} {result+1}') #+1하는 이유는 피자의 번호가 0이 아닌 1부터 시작하기 때문


'''
3
3 5
7 2 6 5 3
5 10
5 9 3 9 9 2 5 8 7 1
5 10
20 4 5 7 3 15 2 1 2 2
'''