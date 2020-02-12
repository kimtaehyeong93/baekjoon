import sys
sys.stdin = open("example.txt", "r")

def DFS(n):
    for i in range(n,num+2):
        for j in range(num+2):
            if mymap[i][j] == 1:
                temp_time += stop_time[j]
                temp_num += j
                DFS[j]

    ans_time.append([temp_time[:]])
    ans_num.append([temp_num[:]])
    temp_time.clear()
    temp_num.clear()

dis = int(input())
num = int(input())
stop_dis = [i for i in input().split()]
stop_time = [i for i in input().split()]
stop_time.insert(0,0)
stop_time.append(0)

mymap = [[0] * (num + 2) for i in range(num + 2)]

for i in range(num+2):
    for j in range(i+1,num+2):
        if stop_dis[j] - stop_dis[i] <= dis:
            mymap[i][j] = 1

ans_time = []
ans_num = []
temp_time = []
temp_num = []

DFS(0)







