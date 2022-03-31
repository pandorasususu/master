#14069. [모의 SW 역량테스트] 요리사

tc = int(input())

def variation(idx):
    global minV
    if idx == N:
        if position.count(1) == N//2:
            a_list, b_list = [], []
            for f in range(len(food)):
                if position[f]:
                    a_list.append(food[f])
                else:
                    b_list.append(food[f])
            a_sum = 0
            for a_f_1 in a_list:
                for a_f_2 in a_list:
                    a_sum += arr[a_f_1][a_f_2]
            b_sum = 0
            for b_f_1 in b_list:
                for b_f_2 in b_list:
                    b_sum += arr[b_f_1][b_f_2]

            if abs(a_sum-b_sum) < minV:
                minV = abs(a_sum-b_sum)
    else:
        position[idx] = 1
        variation(idx+1)

        position[idx] = 0
        variation(idx+1)

# def DFS()

for _ in range(1, tc+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    position = [0] * N
    food = [i for i in range(N)]
    var_list = []
    minV = 20000
    variation(0)
    print(f'#{_} {minV}')

#live answer
'''
def DFS(n, alst, blst):
    global ans
    if n==N:
        if len(alst)==len(blst):
            asum = bsum = 0
            for i in range(len(alst)):
                for j in range(len(alst)):
                    asum += arr[alst[i]][alst[j]]
                    bsum += arr[blst[i]][blst[j]]
            if ans > abs(asum-bsum):
                ans = abs(asum-bsum)
        return

    DFS(n+1, alst+[n], blst)
    DFS(n+1, alst, blst+[n])

# T = 10
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 12345678
    DFS(0, [], [])
    print(f'#{test_case} {ans}')

'''