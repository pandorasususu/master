#SWEA2005<파스칼의 삼각형>
T = int(input())
for _ in range(1, T+1):
    N = int(input())
    for i in range(len(N)):
        if i = 0:
            print(1)
        else:
            ans = [1,1]

            
n = int(input())

for _ in range(n):
    a = int(input())
    if a == 1:
        print(f'#1\n1')
    elif a == 2:
        print(f'#2\n1\n1 1')
    else:
        print(f'#{a}\n1\n1 1')
        ans_list = [[1], [1, 1]]
        while len(ans_list) != a:
            stop = len(ans_list)-1
            nxt_list = [1,1]
            for idx2 in range(1, len(ans_list)):
                nxt_num = ans_list[stop][idx2 - 1] + ans_list[stop][idx2]
                nxt_list.insert(idx2, nxt_num)
            ans_list.append(nxt_list)
            print(' '.join(list(map(str, ans_list[len(ans_list) - 1]))))