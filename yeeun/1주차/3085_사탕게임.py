import sys
sys.stdin = open('3085.txt', 'r')
input = sys.stdin.readline

def count_candy(board):
    max_cnt = 1
    # 열에서 연속된 사탕 세기
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            # 색깔이 같은 사탕이 있으면 cnt +1
            if board[i][j] == board[i][j-1]:
                cnt += 1
            # 색깔이 같지 않으면 cnt 초기화
            else:
                cnt = 1
            # max_cnt: 연속된 사탕 열 중 가장 긴 것
            max_cnt = max(max_cnt, cnt)

    # 행에서 연속된 사탕 세기
    for i in range(n):
        cnt = 1
        for j in range(1, n):
            # 색깔이 같은 사탕이 있으면 cnt +1
            if board[j][i] == board[j-1][i]:
                cnt += 1
            # 색깔이 같지 않으면 cnt 초기화
            else:
                cnt = 1
            # max_cnt: 연속된 사탕 행 중 가장 긴 것
            max_cnt = max(max_cnt, cnt)
    # 행, 열 통틀어서 가장 길게 연속된 사탕 수 반환
    return max_cnt

n = int(input())
board = [list(input()) for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        # 인덱스가 벗어나지 않는지 검사
        if i + 1 < n:
            # 인접한 사탕을 교환 후 최대 연속 사탕 수 계산
            board[i][j], board[i+1][j] = board[i+1][j], board[i][j]
            ans = max(ans, count_candy(board))
            # 다시 되돌려놓기
            board[i][j], board[i + 1][j] = board[i + 1][j], board[i][j]
        if j + 1 < n:
            board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
            ans = max(ans, count_candy(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]

print(ans)