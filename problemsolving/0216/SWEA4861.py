#SWEA4861<회문>
#항상 시간을 오래끄는 문제들을 보면, 변수들의 설정을 미세하게 잘못해서 잘못된 것을 알 수 있음
#문제를 꼼꼼하게 보는 습관을 기르자.
#이번에는 회문의 길이를 제한하기 위해서 사용한 변수 때문이었다.
#행과 열이 N, 구해야 하는 회문의 길이가 M 이라면, 특정 행과 열에서는 N-M+1번 만큼의 후보가 나오는데, 이것을 N-M으로 두고 계속 풀고 있었음.
#그리고 전반적으로 문제 푸는 방식이 깔끔하지 않고 for문과 if문이 너무 많다고 생각함.

T = int(input())
for _ in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for r in range(N)]
    b_point = False

    for r in range(N): #row 검사
        for m in range(N-M+1): #길이가 M인 row 내부 list들의 개수
            for c in range(M):
                if arr[r][m+c] == arr[r][m+M-c-1]: #양옆의 글자들이 같은 지 판별
                    if (m + c) == (m+(M//2)-1): #가장 중앙의 글자까지 회문의 조건을 충족할 시
                        print(f'#{_}',end=' ')
                        print(''.join(arr[r][m:m+M])) #회문을 출력하고 반복문 중단
                        b_point = True
                        break
                else: #회문이 아니면 반복문 중단
                    break
        if b_point == True: #회문을 찾았으면 반복문 중단
            break

    for c in range(N): #col검사
        for m in range(N-M+1): #길이가 M인 col 내부 list들의 개수
            for r in range(N):
                if arr[m+r][c] == arr[m+M-r-1][c]: #양옆의 글자들이 같은 지 판별
                    if (m + r) == (m+(M//2)-1): #가장 중앙의 글자까지 회문의 조건을 충족할 시
                        print(f'#{_}',end=' ')
                        for ans_r in range(m, m+M): #회문을 출력하고 반복문 중단
                            print(arr[ans_r][c],end='')
                        print()
                        b_point = True
                        break
                else: #회문이 아니면 반복문 중단
                    break
        if b_point == True: #회문을 찾았으면 반복문 중단
            break

    if b_point == True:
        continue

# arr = [['a1','a2','a3','a4'],['b','b','b','b'],['c','c','c','c'],['d','d','d','d']]
# print(''.join(arr[0][1:3]))
