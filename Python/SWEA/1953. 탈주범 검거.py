# SWEA: 1953. 탈주범 검거

# --- 문제 분석 ---

# 터널끼리 연결이 되어 있는 경우 이동이 가능
# 탈주범이 있을 수 있는 위치의 개수를 계산하여야 함
# 탈주범은 시간당 1의 거리를 움직일 수 있음
# 지하 터널은 총 7 종류의 터널 구조물로 구성

# 1: 상, 하, 좌, 우
# 2: 상, 하
# 3: 좌, 우
# 4: 상, 우
# 5: 하, 우
# 6: 하, 좌
# 7: 상, 좌

# 지하 터널 지도와 맨홀 뚜껑의 위치, 경과된 시간이 주어질 때
# 탈주범이 위치할 수 있는 장소의 개수를 계산

# 지도의 세로 N, 가로 M
# 맨홀 뚜껑의 세로 R, 가로 C
# 소요된 시간 L

# --- 문제 풀이 ---

# 1. 시작 위치(r, c)에서 출발
# 2. 시간을 흐름에 체크 이중 리스트에 체크

# Step 1. 입출력
t = int(input())
for tc in range(1, t+1):
    n, m, r, c, l = map(int, input().split())
    lists = [list(map(int, input().split())) for _ in range(n)]

    ans = 0
    check = [[0] * m for _ in range(n)]
    check[r][c] = 1

    for _ in range(l):
        for i in range(n):
            for j in range(m):
                if check[i][j] == 0 and lists[i][j] != 0:
                    if lists[i][j] == 1:
                        check[i - 1][j] = 1
                        check[i + 1][j] = 1
                        check[i][j - 1] = 1
                        check[i][j + 1] = 1
                    elif lists[i][j] == 2:
                        check[i - 1][j] = 1
                        check[i + 1][j] = 1
                    elif lists[i][j] == 3:
                        check[i][j - 1] = 1
                        check[i][j + 1] = 1
                    elif lists[i][j] == 4:
                        check[i - 1][j] = 1
                        check[i][j + 1] = 1
                    elif lists[i][j] == 5:
                        check[i + 1][j] = 1
                        check[i][j + 1] = 1
                    elif lists[i][j] == 6:
                        check[i + 1][j] = 1
                        check[i][j - 1] = 1
                    elif lists[i][j] == 7:
                        check[i - 1][j] = 1
                        check[i][j - 1] = 1

    print(check)

    print("#{} {}".format(tc, ans))