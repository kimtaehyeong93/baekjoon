import sys
sys.stdin = open("example.txt", "r")
num = int(input())
length = [[i for i in map(int,input().split())] for j in range(6)]

dir = []
for i in range(6):
    dir.append(length[i][0])
if dir[0:3] == [1, 3, 1]:
    S = length[3][1]*length[4][1] - length[0][1]*length[1][1]
elif dir[0:3] == [3, 1, 4]:
    S = length[2][1]*length[3][1] - length[0][1]*length[5][1]
elif dir[0:3] == [1, 4, 2]:
    S = length[1][1]*length[2][1] - length[4][1]*length[5][1]
elif dir[0:3] == [4, 2, 3]:
    S = length[1][1]*length[0][1] - length[3][1]*length[4][1]
elif dir[0:3] == [2, 3, 1]:
    S = length[0][1]*length[5][1] - length[2][1]*length[3][1]
elif dir[0:3] == [3, 1, 3]:
    S = length[5][1]*length[4][1] - length[1][1]*length[2][1]
print(S*num)