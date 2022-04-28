# 5248. [파이썬 S/W 문제해결 구현] 6일차 - 그룹 나누기

tc = int(input())
for _ in range(1, tc+1):
    students, request = map(int,input().split())
    arr = list(map(int, input().split()))
    group = []
    for i in range(0, len(arr), 2):
        a, b = arr[i], arr[i+1]
        if not group:
            group.append([a, b])
        else:
            for j in range(len(group)):
                if b in group[j]:
                    group[j].append(a)
                    break
                elif a in group[j]:
                    group[j].append(b)
                    break
            else:
                group.append([a, b])
    students_in_group = 0
    for k in range(len(group)):
        students_in_group += len(group[k])
    print(f'#{_} {len(group) + students - students_in_group}')
'''
4
5 2
1 2 3 4
5 3
1 2 2 3 4 5
7 4
2 3 4 5 4 6 7 4
0 0

'''