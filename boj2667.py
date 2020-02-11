import sys
sys.stdin = open("example.txt", "r")

def DFS(y,x):
    global ans, mymap, temp
    mymap[y][x] = 0
    temp += 1

    for dir in range(4):
        ny = y + dy[dir]
        nx = x + dx[dir]

        if 0 <= ny <= N-1 and 0 <= nx <= N-1 and mymap[ny][nx] == 1:
            DFS(ny,nx)



dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
mymap = []
for _ in range(N):
    mymap.append(list(map(int,list(input()))))

ans = []

for i in range(N):
    for j in range(N):
        mymap[i][j] = int(mymap[i][j])
        if mymap[i][j] == 1:
            temp = 0
            DFS(i,j)
            ans.append(temp)
ans.sort()
print(len(ans))
for i in range(len(ans)):
    print(ans[i])

