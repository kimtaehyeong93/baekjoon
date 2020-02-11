import sys
sys.stdin = open("example.txt", "r")
def issafe(y,x):
    if 0 <= y <= h-1 and 0 <= x <= w-1:
        return True
    else:
        return False

def DFS(y,x):
    global visited2
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if issafe(ny,nx) and mymap[ny][nx] == 0:
            visited2 = [[0] * w for i in range(h)]
            if DFS2(ny,nx) != None:
                return True

def DFS2(y,x):
    if y == 0 or y == h-1 or x == 0 or x == w-1:
        return True
    visited2[y][x] = 1

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if issafe(ny,nx):
            if mymap[ny][nx] == 0 and visited2[ny][nx] == 0:
                return DFS2(ny,nx)

h, w = map(int,input().split())

mymap = [[i for i in map(int,input().split())] for i in range(h)]

iter = 0
ans = []
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
visited = [[0] * w for i in range(h)]
while True:
    numof1 = 0
    cnt = 0
    for i in range(h):
        numof1 += mymap[i].count(1)
    if numof1 == 0:
        break
        
    for i in range(h):
        for j in range(w):
            if mymap[i][j] == 1:
                if DFS(i,j):
                    visited[i][j] = 1
    for i in range(h):
        for j in range(w):
            if visited[i][j] == 1:
                mymap[i][j] = 0
                cnt += 1
    
    ans.append(cnt)
    iter += 1
print(iter)
print(ans)
