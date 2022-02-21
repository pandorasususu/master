#백준18870<좌표 압축>
#간단해 보여서 금방 작성했지만, 한 시간 정도 계속 시간초과라는 결과만 볼 수 있었다.
#결국 질문 게시판을 통해 O(n^2)의 코드는 시간초과가 뜬다는 것을 알았고, 딕셔너리를 통해 해결할 수 있었다.
#이 과정에서 .index를 통한 위치찾기는 O(n), dict을 통한 위치 찾기는 O(1)이 걸린다는 것을 알 수 있었다.
'''
import sys
input = sys.stdin.readline

T = int(input())
xy_list = list(map(int, input().split()))
n_list = sorted(list(set(xy_list)))
ans_dict={}
for e in range(len(n_list)):
    if n_list[e] in ans_dict.keys():
        continue
    else:
        ans_dict[n_list[e]] = e

for ee in xy_list:
    print(ans_dict[ee], end=' ')

'''