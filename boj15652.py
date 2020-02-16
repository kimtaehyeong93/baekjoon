N , M = map(int,input().split())
lst = []

def backtracking(n, m):
    if len(lst) == m:
        print(*lst)
        return
    for i in range(1,n+1):
        if not lst:
            lst.append(i)
            backtracking(n, m)
            lst.pop()
        else:
            if i >= lst[-1]:
                lst.append(i)
                backtracking(n, m)
                lst.pop()
backtracking(N, M)