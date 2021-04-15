# SWEA: 1949. 등산로 조성

# --- 문제요약 ---

# N * N 크기의 부지
# 최대한 긴 등산로 만들 계획
# 숫자는 지형의 높이

# 규칙 1. 가장 높은 봉우리에서 시작
# 규칙 2. 높은 지형에서 낮은 지형으로 가로 또는 세로 방향으로 연결
# 규칙 3. 높이가 같은 곳이나 대각선 연결 불가
# 규칙 4. 딱 한 곳을 정해서 K 깊이만큼 깎을 수 있음

# 가장 긴 등산로의 길이 찾기

# --- 문제풀이 ----

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

# Step 5. 길 만드는 함수 만들기
def make_loads(location, load, cut):
    global ans, n
    r, c = location[0], location[1]
    if len(load) > ans:
        ans = len(load)
    for z in range(4):
        nr, nc = r + dr[z], c + dc[z]
        if 0 <= nr < n and 0 <= nc < n:
            if [nr, nc] not in load:
                gab = lists[r][c] - lists[nr][nc]
                if gab > 0:
                    load.append([nr, nc])
                    make_loads([nr, nc], load, cut)
                    load.pop()
                elif -k < gab <= 0:
                    if not cut:
                        load.append([nr, nc])
                        temp = lists[nr][nc]
                        lists[nr][nc] = lists[r][c] - 1
                        make_loads([nr, nc], load, True)
                        lists[nr][nc] = temp
                        load.pop()

# Step 1. 입력
t = int(input())
for tc in range(1, t+1):
    n, k = map(int, input().split())
    lists = [list(map(int, input().split())) for _ in range(n)]

    # Step 2. 가장 높은 봉우리 찾기
    max_point = -999999999
    for i in range(n):
        if max_point < max(lists[i]):
            max_point = max(lists[i])

    # Step 3. 시작점 후보들 찾기
    start_candidate = []
    for i in range(n):
        for j in range(n):
            if lists[i][j] == max_point:
                start_candidate.append([i, j])

    # Step 4. 길 만들며 이동
    ans = 0
    for start in start_candidate:
        make_loads(start, [[start[0], start[1]]], False)

    # Step 6. 출력
    print("#{} {}".format(tc, ans))