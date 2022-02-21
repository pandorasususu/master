#SWEA12741<두 전구>
#엄청 쉬운 문제인데 자꾸만 시간이 초과되어서 틀림.
#예제가 3만개이기 때문에, 매 test case를 print해서 시간이 오래 걸렸던 것
#매 test_case의 답을 list에 저장하고, 이를 한번에 출력하니 단번에 통과
T = int(input())

fin = []

for _ in range(T):
    a, b, c, d = map(int, input().split())
    base = [0] * (max(a,b,c,d)+1)
    for i in range(a, b+1):
        base[i] += 1
    for j in range(c, d+1):
        base[j] += 1

    ans = [k for k in range(len(base)) if base[k] == 2]
    if len(ans) == 0:
        fin.append(0)
    else:
        fin.append(max(ans) - min(ans))

for idx in range(len(fin)):
    print(f'#{idx+1} {fin[idx]}')