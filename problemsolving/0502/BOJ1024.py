#BOJ1024<수열의 합>
#그리디로 풀었다고 생각하는데, 실제로 적합한 지는 모르겠음.
#N이 10억 이하라고 주어졌으므로 최대한 적은 계산만으로 답에 근접하려고 노력함.
#그 과정에서 min_len이 N이상일 경우에는 조건에 부합하는 답을 구할 수 없을 것이라 생각해 미리 제외했음.
#그러나 1, 2와 같이 주어질 때 답을 구할 수 없으므로 이를 고려해 조건을 변경함.
N, L = map(int, input().split())
target = N
min_len = L
result = - 1

while True:
    if min_len > 100:
        break

    start = (target // min_len) - (min_len//2)
    end = target // min_len
    if start < 0:
        start = 0

    for num1 in range(start, end+1):
        sumV = 0
        for num2 in range(min_len):
            sumV += (num1 + num2)
        if sumV == N:
            result = 'not -1'
            for num3 in range(num1, num1+min_len):
                print(num3, end=' ')
            break
    if result != -1:
        break
    min_len += 1

if result == -1:
    print(result)



