# 일곱 난쟁이 찾기 / 키의 합이 100

# 아홉 난쟁이의 키 입력
# 일곱 난쟁이의 키를 오름차순 출력 (반드시 존재)

# 테스트
# tall = [20, 7, 23, 19, 10, 15, 25, 8, 13]

# 입력
tall = []
for _ in range(9):
    tmp = int(input())
    tall.append(tmp)

# 정렬
tall.sort()
# 합
tall_sum = sum(tall)

# 전체 합에서 2명을 뺏을 때 100이 되는 경우 찾아서 제거
flag = 0
for i in range(9):
    for j in range(i + 1, 9):
        if tall_sum - (tall[i] + tall[j]) == 100:

            a, b = tall[i], tall[j]
            tall.remove(a)
            tall.remove(b)

            flag = 1
            break

    if flag == 1:
        break

for i in range(7):
    print(tall[i])



