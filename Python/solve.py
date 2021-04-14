import sys
sys.stdin = open('input.txt', 'r')

# SWEA: 2382. 미생물 격리

# 정사각형 구역 안에 K개의 미생물 군집
# 가로 N개, 세로 N개, 총 N * N의 동일한 크기의 정사각형 셀
# 미생물들이 구역을 벗어나지 못하게 가장자리에 약품을 칠해 놈

# 1. 군집의 위치, 미생물의 수, 이동 방향 주어짐
# 2. 약품에는 없음
# 3. 이동 방향은 상: 1, 하: 2, 좌: 3, 우: 4
# 4. 1시간마다 다음 셀로 이동
# 5. 약품으로 가면 절반이 죽고, 이동방향 반대로 바뀜
# 6. 홀수인 경우: 살아남은 미생물 수 = 원래 미생물 수를 2로 나눈 후 소수점 이하를 버림 한 값
# 7. 두 개 이상의 군집이 한 셀에 모이면 합쳐짐
# 8. 숫자는 더하고, 방향은 더 큰 군집꺼로
# 9. 합쳐질 때 미생물 수가 같은 경우는 안주어지므로 고려하지 않아도 됨

# M 시간 동안 격리
# M 시간 후 남아있는 미생물의 수 구하기

# ----------

# Step 1. 입력과 맵 그리기
t = int(input())
for tc in range(1, t+1):
    n, m, k = map(int, input().split())

    lists = [[[0, 0, []] for _ in range(n)] for _ in range(n)]

    for _ in range(k):
        r, c, a, d = map(int, input().split())

        # Step 2. 미생물들 그리기
        lists[r][c] = [a, d, []]

    dr = [0, -1, 1, 0, 0]
    dc = [0, 0, 0, -1, 1]

    # Step 3. 시간으로 반복문 돌림
    for time in range(m):

        # Step 4. 맵을 탐색해서 미생물을 타겟함
        for r in range(n):
            for c in range(n):
                if lists[r][c] != [0, 0, []]:

                    # Step 5. 이동을 시작함
                    for k in range(1, 5):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if 0 <= nr < n and 0 <= nc < n:
                            if nr == 0 or nc == 0 or nr == n-1 or nc == n-1:
                                lists[r][c][0] = int(lists[r][c][0]/2)
                                if lists[r][c][1] == 1:
                                    lists[r][c][1] = 2
                                elif lists[r][c][1] == 2:
                                    lists[r][c][1] = 1
                                elif lists[r][c][1] == 3:
                                    lists[r][c][1] = 4
                                elif lists[r][c][1] == 4:
                                    lists[r][c][1] = 3

                            lists[nr][nc][2].append(lists[r][c])
                            temp_A = -999999999
                            temp_B = 0
                            temp_C = 0
                            for z in range(len(lists[nr][nc][2])):
                                if lists[nr][nc][2][z][0] > temp_A:
                                    temp_A = lists[nr][nc][2][z][0]
                                    temp_B = lists[nr][nc][2][z][1]
                                temp_C += lists[nr][nc][2][z][0]
                            lists[nr][nc][0] = temp_C
                            lists[nr][nc][1] = temp_B
                            lists[nr][nc][2] = []
                            lists[r][c] = [0, 0, []]

    ans = 0
    for i in range(n):
        for j in range(n):
            print(lists[i][j], end=' ')
            ans += lists[i][j][0]
        print()
    print()

    print("#{} {}".format(tc, ans))




