#SWEA13240
#20개 중 14개 맞았다는데 ㅎ...

T = int(input())
for _ in range(1, T+1):
    H, W, N = map(int, input().split())
    arr_word = list(input().split())
    arr_len = [len(arr_word[i]) for i in range(len(arr_word))]
    max_len = 0
    for j in range(len(arr_len)):
        if arr_len[j] > arr_len[max_len]:
            max_len = j

    word_size = 1
    w_size = 0
    h_size = word_size
    b_point = False
    while True:
        for k in range(len(arr_len)):
            w_size += arr_len[k] * word_size
            if (h_size + word_size > H):
                if w_size > W:
                    print(f'#{_} {word_size-1}')
                    b_point = True
                    break
                elif w_size == W:
                    print(f'#{_} {word_size}')
                    b_point = True
                    break

                else:
                    w_size += word_size

            else:
                if w_size >= W:
                    w_size = 0
                    h_size += word_size
                    if w_size == W:
                        w_size = 0
                        h_size += word_size
                    if arr_len[k] * word_size > W:
                        print(f'#{_} 0')
                        b_point = True
                        break
                    else:
                        if (arr_len[k]+1) * word_size <= W:
                            w_size = (arr_len[k]+1) * word_size
                        else:
                            w_size = 0
                            h_size += word_size
                else:
                    w_size += word_size
        if b_point == True:
            break
        else:
            word_size += 1
            w_size = 0
            h_size = word_size


'''
3
41 85 9
samsung i am man HELLO HI MAN 20 20
3 3 3
ABC DEF GHI
4 4 1
AB

1
4 4 1 
AB
'''


