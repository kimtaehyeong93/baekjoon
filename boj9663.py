N = int(input())

mymap = [[0] * N for i in range(N)]
ans = 0
dx=[1,0,-1,0,1,-1,1,-1]
dy=[0,1,0,-1,1,-1,-1,1]             
cnt = 0
start = 0
def nqueen(n):
    global ans, start
    cnt = 0
    for i in range(n):
        cnt += mymap[i].count(1)
    if cnt == n:
        ans += 1
        return
    for i in range(start, n):
        if i >= 1:
            if 1 not in mymap[i-1]:
                return
        for j in range(n):
            TF = True
            if mymap[i][j]:
                continue
            for k in range(8):
                if not TF:
                    break
                del_x = dx[k]
                del_y = dy[k]
                y = i + del_y
                x = j + del_x
                while 0 <= x <= n-1 and 0 <= y <= n-1:
                    if mymap[y][x]:
                        TF = False
                        break
                    else:
                        y += del_y
                        x += del_x  
            else:
                mymap[i][j] = 1
                start += 1
                nqueen(n)
                mymap[i][j] = 0
                start -= 1
                         
nqueen(N)
print(ans)



