N, M = map(int,input().split())
visited = [0] * (N+1)
lst = []
def backtracking(n, m):
    global lst
    if len(lst) == M:
        print(*lst)
        return
    for i in range(1,N+1):    
        if visited[i] == 0 and i not in lst:
            visited[i] == 1
            lst.append(i)
            backtracking(n, m)
            visited[i] == 0
            lst.pop()

backtracking(N, M)
             
            


            

