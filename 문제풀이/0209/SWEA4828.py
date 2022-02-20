#SWEA4828<min-max>
'''
T = int(input())

for _ in range(1,T+1):
    N = int(input())
    num_list = list(map(int, input().split()))
    for idx1 in range(len(num_list)-1,0,-1): #버블 정렬 사용해서 오름차순으로 정렬
        for idx2 in range(idx1):
            if num_list[idx2] > num_list[idx2+1]:
                num_list[idx2], num_list[idx2+1] = num_list[idx2+1], num_list[idx2]
    print(f'#{_} {num_list[len(num_list)-1] - num_list[0]}') #최대값과 최소값 차이 출력
'''