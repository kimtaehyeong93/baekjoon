import sys
sys.stdin = open("example.txt")

pi = [0]
length = int(input())
data = input()
i = 0
j = 1
while j < length:
    if data[i] == data[j]:
        pi.append(pi[-1] + 1)
        i += 1
        j += 1
    else:
        i = 0
        if data[0] == data[j]:
            pi.append(1)
            j += 1
        else:
            pi.append(0)
            j += 1

print(length-pi[-1])
