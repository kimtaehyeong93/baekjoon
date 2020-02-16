import sys
sys.stdin = open("example.txt", "r")

def DFS(n):
    global ans_time, temp_time, ans_num
    if temp_time >= ans_time:
        return
    here = n
    visited[n] = 1
    temp_time += stop_time[here]
    temp_num.append(here)
    for i in range(here+1, num + 2):
        if mymap[here][i] == 1 and visited[i] == 0:
            DFS(i)
    if temp_num[-1] == 6:
        if ans_time > temp_time:
            ans_time = temp_time
            ans_num = temp_num[:]
    visited[here] = 0
    temp_time -= stop_time[here]
    temp_num.pop()



dis = int(input())
num = int(input())
stop_dis = [i for i in map(int,input().split())]
stop_time = [i for i in map(int,input().split())]
stop_dis.insert(0,0)
stop_time.insert(0,0)
stop_time.append(0)

mymap = [[0] * (num + 2) for i in range(num + 2)]
visited = [0] * (num + 2)

for i in range(num+2):
    for j in range(i+1,num+2):
        if sum(stop_dis[i:j+1]) - stop_dis[i] <= dis:
            mymap[i][j] = 1

temp_time = 0
temp_num = []
ans_num = []
ans_time = sum(stop_time)
DFS(0)

print(ans_time)
print(len(ans_num)-2)
print(*ans_num[1:-1])

