import sys
sys.stdin = open("example.txt", "r")

dis = int(input())
num = int(input())
stop_dis = [i for i in map(int,input().split())]
stop_time = [i for i in map(int,input().split())]
stop_time.insert(0,0)
stop_time.append(0)
stop_dis.insert(0,0)
mymap = [[0] * (num + 2) for i in range(num + 2)]
visited = [0] * (num + 2)
parent = [0] * (num + 2)
minsum = 987654321
visited[0] = 1

for i in range(num+2):
    for j in range(i+1,num+2):
        if sum(stop_dis[i:j+1]) - stop_dis[i] <= dis:
            mymap[i][j] = 1

def backtracking(here, sofar):
    global minsum, stack
    if here == num + 1:
        if minsum > sofar:
            minsum = sofar
            stack = parent[:]
        return
    for next in range(here, num + 2):
        if mymap[here][next] and not visited[next] and sofar + stop_time[next] < minsum:
            visited[next] = 1
            parent[next] = here
            backtracking(next,sofar + stop_time[next])
            visited[next] = 0
    
temp = []
backtracking(0, stop_time[0])
print(minsum)
temp.append(num +1)
route = []
for i in range(num + 2):
    temp.append(stack[temp[-1]])
    if temp[-1] == 0:
        break
for i in range(len(temp)):
    route.append(temp.pop())
print(len(route)-2)
print(*route[1:-1])



