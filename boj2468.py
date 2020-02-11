import sys
# sys.stdin = open("example.txt", "r")
sys.setrecursionlimit(1000001)

def DFS(y,x):
    global N
    visited[y][x] = 1
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N-1 and 0 <= nx <= N-1:
            if mymap[ny][nx] != 0 and visited[ny][nx] == 0:
                DFS(ny,nx)

N = int(input())

arr = [[i for i in map(int,input().split())] for j in range(N)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

height = []
for i in range(N):
    height += arr[i]
height = set(height)
height = list(height)
height += [0]

ans = [0] * len(height)
for h in range(len(height)):
    mymap = [arr[i][:] for i in range(N)]
    for i in range(N):
        for j in range(N):
            if mymap[i][j] <= height[h]:
                mymap[i][j] = 0
    visited = [[0] * N for i in range(N)]
    
    for i in range(N):
        for j in range(N):
            if mymap[i][j] != 0 and visited[i][j] == 0:
                DFS(i,j)
                ans[h] += 1
print(max(ans))






