# 13068. 5203. [파이썬 S/W 문제해결 구현] 3일차 - 베이비진 게임

tc = int(input())

for _ in range(1, tc+1):
    arr = list(map(int, input().split()))
    result = 0
    player1 = []
    player1_cards = [0] * 14
    player2 = []
    player2_cards = [0] * 14

    for idx in range(len(arr)):
        if result != 0:
            break

        if not idx % 2:
            player1.append(arr[idx])
            player1_cards[arr[idx]+2] += 1
        else:
            player2.append(arr[idx])
            player2_cards[arr[idx]+2] += 1

        if len(player1) >= 3:
            p1_cards = player1_cards[:]
            p2_cards = player2_cards[:]

            for one in range(2, len(p1_cards)-2):
                if (p1_cards[one] >= 3) or (p1_cards[one] >= 1 and p1_cards[one+1] >= 1 and p1_cards[one+2] >= 1):
                    result = 1
                    break
            for two in range(2, len(p2_cards)-2):
                if (p2_cards[two] >= 3) or (p2_cards[two] >= 1 and p2_cards[two+1] >= 1 and p2_cards[two+2] >= 1):
                    result = 2
                    break

    print(f'#{_} {result}')
