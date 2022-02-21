#SWEA1221<GNS>

T = int(input())
nn = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
ps_dict = {}
for idx in range(len(nn)):
    ps_dict[nn[idx]] = idx
for _ in range(1, T+1):
    a, b = input().split()
    b = int(b)
    a_list = list(input().split())
    cnt_list = [0] * 7
    for i in range(b):
        for n in nn:
            if a_list[i] == n:
                cnt_list[nn.index(n)] += 1
    print(a,end=' ')
    for n in nn:
        print(n*cnt_list[cnt_list.index(n)],end=' ')
