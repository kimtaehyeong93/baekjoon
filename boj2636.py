import sys
sys.stdin = open("example.txt", "r")
def issafe(y,x):
    if 0 <= y <= h-1 and 0 <= x <= w-1:
        return True
    else:
        return False

def DFS(y,x):
    if y == 0 or y == h - 1 or x == 0 or x == w - 1:
        return 1
    visited[y][x] = 1
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if issafe(ny,nx) and mymap[ny][nx] == 0 and visited[ny][nx] == 0:
            return DFS(ny,nx)

h, w = map(int,input().split())

mymap = [[i for i in map(int,input().split())] for i in range(h)]

ans = []
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
meltingpoint = [[0] * w for i in range(h)]
while True:
    numof1 = 0
    cnt = 0
    for i in range(h):
        numof1 += mymap[i].count(1)
        if numof1 != 0:
            break
    else:
        break
        
    for i in range(h):
        for j in range(w):
            if mymap[i][j] == 1:
                visited = [[0] * w for i in range(h)]
                if DFS(i,j) == 1:
                    meltingpoint[i][j] = 1
    for i in range(h):
        for j in range(w):
            if meltingpoint[i][j] == 1:
                mymap[i][j] = 0
                cnt += 1
    
    ans.append(cnt)

print(len(ans))
print(ans[-1] - ans[-2])
