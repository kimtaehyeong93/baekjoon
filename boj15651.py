N, M = map(int,input().split())

lst = []
def backtracking(N, M):
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1, N+1):
        lst.append(i)
        backtracking(N, M)
        lst.pop()

backtracking(N, M)