import sys
sys.stdin = open("example.txt", "r")

def issafe(y,x):
    if 0 <= y <= h-1 and 0 <= x <= w-1:
        return True
    else:
        return False

def DFS(y,x):
    mymap[y][x] = 9
    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]
        if issafe(ny,nx) and mymap[ny][nx] == 0:
            DFS(ny,nx)

h, w = map(int,input().split())

mymap = [[i for i in map(int,input().split())] for i in range(h)]

visited2 = [[0] * w for i in range(h)]
ans = []
dx = [0, 0, 1, -1]
dy = [-1, 1, 0, 0]


while True:
    cnt = 0
    numof1 = 0
    for i in range(h):
        for j in range(w):
            if mymap[i][j] == 0:
                DFS(i, j)

    for i in range(h):
        numof1 += mymap[i].count(1)
    if numof1 == 0:
        break

    for i in range(h):
        for j in range(w):
            for dir in range(4):
                if mymap[i][j] == 1 and mymap[i+dy[dir]][j+dx[dir]] == 9:
                    visited2[i][j] = 1
                    break
    for i in range(h):
        for j in range(w):               
            if visited2[i][j] == 1:
                mymap[i][j] = 9
                cnt += 1

    ans.append(cnt)

print(len(ans))
print(ans[-1] - ans[-2])
