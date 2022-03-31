'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
#
# n = int(input())
# arr = list(map(int, input().split()))
# p = [i for i in range(n+1)]
# c1 = [0] * (n+1)
# c2 = [0] * (n+1)
#
# for idx in range(0, len(arr), 2):
#     if c1[arr[idx]] == 0:
#         c1[arr[idx]] = arr[idx+1]
#     else:
#         c2[arr[idx]] = arr[idx+1]
# print(p)
# print(c1)
# print(c2)
#
# def func1(v):
#     if v:
#         print(v, end=' ')
#         func1(c1[v])
#         func1(c2[v])
#
# def func2(v):
#     if v:
#         func2(c1[v])
#         print(v, end=' ')
#         func2(c2[v])
#
# def func3(v):
#     if v:
#         func3(c1[v])
#         func3(c2[v])
#         print(v, end=' ')
# func1(1)
# print()
# func2(1)
# print()
# func3(1)

# v = int(input())
# e = v + 1
# arr = list(map(int, input().split()))
# par = [0] * (v+1)
# for i in range(e):
#     p, c = arr[i*2], arr[i*2+1]
#     par[c] = p
#
# '''
# 4
# 2 1 2 4 4 3 4 5
# '''
#
# print(*par)
#
# root = 0
# for i in range(1, v+1):
#     if par[i] == 0:
#         root = i
#         break
# print(root)

'''
def enq(n):
    global last
    last += 1
    tree[last] = n  # 완전이진트리 유지
    c = last    # 새로 추가된 정점을 자식으로
    p = c//2    # 완전이진트리에서의 부모 정점 번호
    while p>=1 and tree[p] < tree[c]:    # 부모가 있고, 자식의 키값이 더 크면 교환
        tree[p], tree[c] = tree[c], tree[p]
        c = p
        p = c//2


def deq():
    global last
    tmp = tree[1]   # 루트의 key값
    tree[1] = tree[last]    # 마지막 정점의 키를 루트에 복사
    last -= 1               # 마지막 정점 삭제
    # 부모>자식 규칙 유지
    p = 1
    c = p * 2   # 왼쪽자식노드 번호
    while c <= last:    # 왼쪽자식이 있으면
        if c+1<=last and tree[c]<tree[c+1]:    # 오른쪽 자식노드도 있고 더 크면
            c += 1          # 오른쪽 자식 선택
        if tree[p] < tree[c]:   # 자식의 키값이 더 크면 교환
            tree[p], tree[c] = tree[c], tree[p]
            p = c
            c = p*2
        else:
            break
    return tmp


# 포화이진트리의 정점번호 1~100
tree = [0]*(101)
last = 0        # 마지막 정점 번호
enq(3)
enq(2)
enq(4)
enq(7)
enq(5)
enq(1)
#print(tree[1])
enq(9)
#print(tree[1])
while last>0:
    print(deq(), tree[1])
'''

heap = [0] * 16
# 마지막요소를 가리키는 변수
heapcount = 0

# 최대힙
def heap_push(value):
    global heapcount
    # 완전이진트리를 유지해야 하므로 마지막 자리에 넣어주기
    heapcount += 1
    heap[heapcount] = value
    # 부모노드가 삽입한 요소보다 작으면 자리바꾸기
    current = heapcount
    parent = current // 2
    # 부모노드 값이 작으면 계속 반복
    # 자리를 바꾸고 나서 부모노드와 비교해서
    # 부모노드가 작으면 자리 바꾸기 작업을 계속수행....
    # 스스로가 루트이면 멈춰!
    while parent > 0 and heap[parent] < heap[current]:
        heap[parent], heap[current] = heap[current], heap[parent]
        # 바꿨으니 부모노드가 현재노드가 되는것이고
        # 새로운 부모노드 인덱스 계산해주기
        current = parent
        parent = current // 2


def heappop():
    global heapcount
    result = heap[1]
    # 맨 마지막 요소를 루트로 올림
    heap[1] = heap[heapcount]
    # 마지막 요소는 뺐으니
    heap[heapcount] = 0
    heapcount -= 1
    # 자식 요소 중에 큰 값과 비교해서 작으면 교체
    parent = 1
    child = parent * 2
    #만약에 오른쪽 자식이 있으면, 왼쪽 자식과 오른쪽 자식을 비교해서
    # child를 결정
    if child + 1 <= heapcount :
        if heap[child+1] > heap[child]:
            child += 1
    #child : 자식중에 더 큰 값을 가진 자식의 인덱스
    while child <= heapcount and heap[child] > heap[parent]:
        heap[child], heap[parent] = heap[parent],  heap[child]
        parent = child
        child = parent * 2
        if child + 1 <= heapcount:
            if heap[child + 1] > heap[child]:
                child += 1
    return result

heap_push(7)
print(heap)
heap_push(2)
print(heap)
heap_push(4)
print(heap)
heap_push(3)
print(heap)
heap_push(1)
print(heap)
heap_push(6)
print(heap)
heap_push(5)
print(heap)
heap_push(8)
print(heap)
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
print(heappop())
