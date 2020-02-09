import sys
sys.stdin = open("example.txt", "r")
N, K = map(int,input().split())
boy = [0] * 7
girl = [0] * 7
lst = [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    if lst[i][0] == 0:
        girl[lst[i][1]] += 1
    else:
        boy[lst[i][1]] += 1

ans = 0
for i in range(1,7):
    if girl[i] == 0:
        ans += 0
    elif girl[i] % K == 0:
        ans += girl[i] // K
    else:
        ans += girl[i] // K + 1
    if boy[i] == 0:
        ans += 0
    elif boy[i] % K == 0:
        ans += boy[i] // K
    else:
        ans += boy[i] // K + 1
print(ans)
    


