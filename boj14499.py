import sys
sys.stdin = open("example.txt", "r")

N, M, y, x, K = map(int,input().split())

mymap = [[0] * M for _ in range(N)]
mapnumber = [[i for i in map(int,input().split())] for _ in range(N)]

for i in range(N):
    for j in range(M):
        mymap[i][j] = mapnumber[i][j]

dice = [0] * 7

def east():
    dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]

def west():
    dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]

def north():
    dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]

def south():
    dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

dx = [0, 1, -1, 0, 0]
dy = [0, 0, 0, -1, 1]

cmd = [i for i in map(int,input().split())]
for i in cmd:
    if 0 <= y+dy[i] <= N-1 and 0 <= x+dx[i] <= M-1:
        pass
    else:
        continue

    if i == 1:
        east()
        if mymap[y+dy[i]][x+dx[i]] == 0:
            mymap[y+dy[i]][x+dx[i]] = dice[6]
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
        else:
            dice[6] = mymap[y+dy[i]][x+dx[i]]
            mymap[y+dy[i]][x+dx[i]] = 0
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
    elif i == 2:
        west()
        if mymap[y+dy[i]][x+dx[i]] == 0:
            mymap[y+dy[i]][x+dx[i]] = dice[6]
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
        else:
            dice[6] = mymap[y+dy[i]][x+dx[i]]
            mymap[y+dy[i]][x+dx[i]] = 0
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
    elif i == 3:
        north()
        if mymap[y+dy[i]][x+dx[i]] == 0:
            mymap[y+dy[i]][x+dx[i]] = dice[6]
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
        else:
            dice[6] = mymap[y+dy[i]][x+dx[i]]
            mymap[y+dy[i]][x+dx[i]] = 0
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
    else:
        south()
        if mymap[y+dy[i]][x+dx[i]] == 0:
            mymap[y+dy[i]][x+dx[i]] = dice[6]
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
        else:
            dice[6] = mymap[y+dy[i]][x+dx[i]]
            mymap[y+dy[i]][x+dx[i]] = 0
            y = y+dy[i]
            x = x+dx[i]
            print(dice[1])
