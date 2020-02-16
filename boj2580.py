import sys
sys.stdin = open("example.txt")

def sumrow(a):
    for i in range(len(a)):
        if sum(a[i]) != 45:
            return False
    return True

def sumcol(a):
    for i in range(len(a)):
        k = 0
        for j in range(len(a)):
            k += a[j][i]
        if k != 45:
            return False

def sumsq(a):
    for i in range(0, 9 ,3):
        for j in range(0, 9, 3):
            k = 0
            for m in range(3):
                for n in range(3):
                    k += a[i+m][j+n]
            if k != 45:
                return False
    return True

def permu(a):
    global visited, lst, temp
    if len(a) == 1:
        lst.append(a)
        return
    else:
        for i in range(len(a)):
            if visited[i] == 0:
                temp.append(a[i])
                visited[i] = 1
                permu(a)
                visited[i] = 0
                temp.pop()
        if len(temp) == len(a):
            lst.append(temp[:])

def backtracking(sdoku):
    global visited, lst, temp, start
    for i in range(start,9):
        cnt = sdoku[i].count(0)
        if cnt:
            sdoku_set = set(sdoku[i])
            addnum = list(sample - sdoku_set)
            visited = [0] * len(addnum)
            lst = []
            temp = []
            permu(addnum)
            for m in lst:
                idx = [0] * len(m)
                for n in range(len(m)):
                    idx[n] = sdoku[i].index(0)
                    sdoku[i][idx[n]] = m[n]
                start += 1
                backtracking(sdoku)
                for n in range(len(m)):
                    sdoku[i][idx[n]] = 0
                start -= 1
    
    if not sumrow(sdoku) or not sumcol(sdoku) or not sumsq(sdoku):
        return
    else:
        for i in range(9):
            ans[i] = sdoku[i][:]


sdoku = [[i for i in map(int,input().split())] for j in range(9)]
sample = {1, 2, 3, 4, 5, 6, 7, 8, 9}
sdoku_col = [[0] * 9 for j in range(9)]
ans = [0] * 9

# for i in range(9):
#     for j in range(9):
#         sdoku_col[i][j] = sdoku[j][i]

# while True:
#     sdoku_temp = sdoku
#     for i in range(9):
#         a = sdoku[i].count(0)
#         if a == 1:
#             idx = sdoku[i].index(0)
#             sdoku[i][idx] = 45 - sum(sdoku[i])
#             sdoku_col[idx][i] = sdoku[i][idx]

#     for i in range(9):
#         b = sdoku_col[i].count(0)
#         if b == 1:
#             idx = sdoku_col[i].index(0)
#             sdoku_col[i][idx] = 45 - sum(sdoku[i])
#             sdoku[idx][i] = sdoku[i][idx]

# for i in range(0,9,3):
#     for j in range(0,9,3):
#         sdoku_sq = []
#         for m in range(3):
#             for n in range(3):
#                 sdoku_sq.append(sdoku[i+m][j+n])
#         c = sdoku_sq.count(0)
#         if c == 1:
#             idx = sdoku_sq.index(0)
#             sdoku[i + idx//3][j + idx%3] = 45 - sum(sdoku_sq)
#             sdoku_col[j + idx%3][i + idx//3] = sdoku[i + idx//3][j + idx%3]
    
#     sdoku_temp2 = sdoku
#     if sdoku_temp == sdoku_temp2:
#         break
start = 0
backtracking(sdoku)
print(ans)

                    