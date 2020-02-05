x, y =map(int,input().split())
num = int(input())
store = []
for i in range(num):
    store.append(list(map(int,input().split())))
police = list(map(int,input().split()))

sum = 0
for i in range(num):
    if police[0] == store[i][0]:
        sum += abs(police[1] - store[i][1])
    elif police[0] + store[i][0] == 3:
        sum += y + min(police[1] + store[i][1], x-police[1] + x-store[i][1])
    elif police[0] + store[i][0] == 7:
        sum += x + min(police[1] + store[i][1], y-police[1] + y-store[i][1])
    elif police[0] + store[i][0] == 4:
        sum += police[1] + store[i][1]
    elif police[0] + store[i][0] == 6:
        sum += x - police[1] + y - store[i][1]
    else:
        if police[0] == 2:
            sum += police[1] + y - store[i][1]
        elif police[0] == 3:
            sum += store[i][1] + y - police[1]
        elif police[0] == 1:
            sum += store[i][1] + x - police[1]
        elif police[0] == 4:
            sum += police[1] + x - store[i][1]
print(sum)



# x, y =map(int,input().split())
# num = int(input())
# store = []
# for i in range(num+1):
#     store.append(list(map(int,input().split())))

# store_lo = []
# for i in store:
#     if i[0] == 1:
#         store_lo.append([0, i[1]])    
#     elif i[0] == 2:
#         store_lo.append([y, i[1]])
#     elif i[0] == 3:
#         store_lo.append([i[1], 0])
#     elif i[0] == 4:
#         store_lo.append([i[1], x])

# police = store_lo.pop()
# sum = 0
# for i in range(num):
#     if store_lo[i][0] == 0 and police[0] == 0:
#         sum += abs(store_lo[i][1] - police[0,1])
#     elif store_lo[i][1] == 0 and police[1] ==0:
#         sum += abs(store_lo[i][0] - police[0])
#     elif store_lo[i][0] == y and police[0] == y:
#         sum += abs(store_lo[i][1] - police[1])
#     elif store_lo[i][1] == x and police[1] == x:
#         sum += abs(store_lo[i][0] - police[0])
#     else:
#         dis = [0, 0, 0, 0]
#         dis[0] = police[0] + police[1] + store_lo[i][0] + store_lo[i][1]
#         dis[1] = y - police[0] + x - police[1] + y - store_lo[i][0] + x - store_lo[i][1]
#         dis[2] = police[0] + x - police[1] + store_lo[i][0] + x - store_lo[i][1]
#         dis[3] = y - police[0] + police[1] + y - store_lo[i][0] + store_lo[i][1]
#         sum += min(dis)

# print(sum)

    
   

