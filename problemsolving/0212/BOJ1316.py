#백준1316<그룹 단어 체커>
'''
T = int(input())

cnt = 0
for _ in range(T):
    group_word = True
    word = list(input())
    word_dict = {}
    for w in range(len(word)):
        # 만약 w번째 알파벳이 그 전에 입력되어 word_dict의 키값으로 존재한다면, 현재 위치w와 직전 등장한 위치의 차가 1이 아니라면,
        # 연속해서 등장하지 않았다는 의미이므로 group_word에 False값을 할당해 cnt에 1을 더하지 않고 다음 단어로 넘어감
        if word[w] in word_dict.keys():
            if w - word_dict[word[w]] != 1:
                group_word = False
                break
            # 아래의 else문 없이 작동할 수 있다고 생각해서 계속 제출해봤지만, 바로 틀렸다는 결과 받음. 
            # 다시 생각해보니 위의 과정을 거치고 만약 알파벳이 연속되게 위치해 있다는 것이 판명나면,
            # 이번 알파벳의 위치 w가 word_dict에 word[w]에 대한 value로 저장되어야 함. 이 과정을 추가하니 통과
            else:
                word_dict[word[w]] = w
        else:
            word_dict[word[w]] = w

    if group_word == False:
        continue
    cnt += 1

print(cnt)
'''