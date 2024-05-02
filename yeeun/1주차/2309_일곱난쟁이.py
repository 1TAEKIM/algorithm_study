import sys
sys.stdin = open('2309.txt', 'r')
input = sys.stdin.readline

height_arr = []
for _ in range(9):
    height_arr.append(int(input()))

height_arr.sort()
height_sum = sum(height_arr)
for i in range(len(height_arr) - 1):
    for j in range(i+1, len(height_arr)):
        if height_arr[i] + height_arr[j] == height_sum - 100:
            for k in range(len(height_arr)):
                if k==i or k==j:
                    continue
                else:
                    print(height_arr[k])
            exit()