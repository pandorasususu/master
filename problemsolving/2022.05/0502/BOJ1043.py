#BOJ1043<거짓말>

#kt = know truth
num_ppl, num_pty = map(int, input().split())
kt_ppl, *kt_ppl_list = map(int, input().split())
parties = []
for _ in range(num_pty):
    pty = list(map(int, input().split()))
    parties.append(pty)

if kt_ppl == 0:
    print(len(parties))
else:
    exception = 0
    for kt_person in kt_ppl_list: #진실을 아는 사람들을 순회
        for i in range(len(parties)): #파티 순회
            party = parties[i]
            if kt_person in party[1:]: #만약 해당 파티에 진실을 아는 사람이 포함되어 있으면
                for j in range(1, len(party)): #이미 진실을 아는 사람 제외하고 다른 사람도 진실을 아는 사람들 리스트에 추가
                    if party[j] not in kt_ppl_list:
                        kt_ppl_list.append(party[j])

    for party in parties: #다시 파티 순회
        for kt_person in kt_ppl_list:
            if kt_person in party[1:]: #만약 파티에 진실을 아는 사람이 있으면
                exception += 1 #진실을 말하면 안되는 파티, exception을 1 증가시키고 다음 파티로 넘어감
                break

    print(len(parties) - exception)

