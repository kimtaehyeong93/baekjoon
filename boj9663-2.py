N = int(input())

mymap = [[0] * N for i in range(N)]
mymap_col = [[0] * N for i in range(N)]
mymap_dia1 = [0] * (2*N - 1)
mymap_dia2 = [0] * (2*N - 1)
ans = 0         
cnt = 0
start = 0
def nqueen(n):
    global ans, start, cnt
    if n == 1:
        ans = 1
    elif n == 2:
        ans = 0
    else:
        for i in range(start, n):
            if i >= 1:
                if 1 not in mymap[i-1]:
                    return
            for j in range(n):
                if mymap[i][j] or 1 in mymap_col[j] or mymap_dia1[i+j] or mymap_dia2[i-j+3]:
                    continue            
                else:
                    mymap[i][j] = 1
                    mymap_col[j][i] = 1
                    mymap_dia1[i+j] = 1
                    mymap_dia2[i-j+3] = 1
                    start += 1
                    cnt += 1
                    if cnt % n == 0:
                        ans += 1
                    nqueen(n)
                    mymap[i][j] = 0
                    mymap_col[j][i] = 0
                    mymap_dia1[i+j] = 0
                    mymap_dia2[i-j+3] = 0
                    start -= 1
                    cnt -= 1
                         
nqueen(N)
print(ans)



