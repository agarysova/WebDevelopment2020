n = int(input())
s = 0

for i in range(1, n + 1):
    j = int(input())
    if j == 0:
        s += 1
print(s)