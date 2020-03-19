import math

n = int(input())
i = 0

while i < n:
    i += 1
    j = int(math.sqrt(i))
    if j*j == i:
        print(i)