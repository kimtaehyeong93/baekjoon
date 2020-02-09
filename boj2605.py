import sys
sys.stdin = open("example.txt", "r")
N = int(input())
ans = []
foodorder = list(map(int,input().split()))
for i in range(0,N):
    ans.insert(i-foodorder[i], i+1)

print(*ans)

