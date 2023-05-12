import sys
n = int(sys.stdin.readline())
list_n = list(map(int, sys.stdin.readline().split()))
max = -1000000
min = 1000000
for i in range(0, n):
    if list_n[i] < min:
        min = list_n[i]
    if list_n[i] > max:
        max = list_n[i]
print(max, min)
   
