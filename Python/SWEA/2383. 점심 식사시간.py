# SWEA: 2383. 점심 식사시간

# N*N 크기의 정사각형 모양의 방에 사람들이 있음
# 점심을 먹기 위해 아래 층으로 내려가야함
# 최대한 빠른 시간 내에 내려가야함

# P = 사람들
# S = 계단 입구 위치
# 이동 완료 시간 = 모든 사람들이 아래 층으로 이동을 완료한 시간
# 이동 완료 시간 = 계단 입구까지 가는 시간 + 내려가는 시간

# 1. 계단 입구까지 가는 시간
# 이동 시간(분) = | PR - SR | + | PC - SC |

# 2. 계단을 내려가는 시간
# 계단 입구에 도착하면 1분 후 내려감
# 계단에 동시에 최대 3명까지만 올라가 있을 수 있음
# 이미 3명이 내려가고 있으면 그 중 한명이 다 내려갈 때까지 입구에서 대기
# 계단의 길이가 K 완전히 내려가는데 K 분

# 모든 사람들이 계단을 내려가 이동이 완료되는 시간이 최소가 되는 경우
# 소요시간 출력

# 계단의 입구는 반드시 2개, 서로 위치가 겹치지 않음
# 초기 사람의 위치와 계단 입구의 위치는 겹치지 않음

# 1: 사람
# 2 이상: 계단의 입구

# ----------

from copy import deepcopy

# Step 1. 입력
t = int(input())
for tc in range(1, t+1):
    n = int(input())
    lists = [list(map(int, input().split())) for _ in range(n)]

    # Step 2. 계단 정보 담아 놓기
    stairs_index, stairs_dist = [], []
    for i in range(n):
        for j in range(n):
            if lists[i][j] >= 2:
                stairs_index.append([i, j])
                stairs_dist.append(lists[i][j])

    # Step 3. 사람과 계단 입구 길이 담아 놓기
    people = []
    for i in range(n):
        for j in range(n):
            if lists[i][j] == 1:
                people.append([abs(i - stairs_index[0][0]) + abs(j - stairs_index[0][1]), abs(i - stairs_index[1][0]) + abs(j - stairs_index[1][1])])

    # Step 4. 케이스 만들어 놓기
    cases = []
    def dfs(index, temp):
        global people, cases
        if index == len(people):
            cases.append(deepcopy(temp))
        else:
            for stair_num in range(2):
                temp.append([0, people[index][stair_num] + stairs_dist[stair_num], stair_num])
                dfs(index + 1, temp)
                temp.pop()

    dfs(0, [])
    ans = 999999999

    # Step 5
    for case in cases:
        time = 0
        stairs = [0, 0]

        def check(case):
            for c in case:
                if c[0] <= c[1]:
                    return True
            return False

        while check(case):
            queue = []
            for i in range(len(case)):
                if case[i][0] < case[i][1] - stairs_dist[case[i][2]]:
                    case[i][0] += 1
                elif case[i][0] == case[i][1] - stairs_dist[case[i][2]]:
                    if stairs[case[i][2]] < 3:
                        stairs[case[i][2]] += 1
                        case[i][0] += 1
                    elif stairs[case[i][2]] == 3:
                        queue.append(i)
                elif case[i][1] - stairs_dist[case[i][2]] < case[i][0] <= case[i][1]:
                    case[i][0] += 1
                    if case[i][0] > case[i][1]:
                        stairs[case[i][2]] -= 1
            for q in queue:
                if stairs[case[q][2]] < 3:
                    stairs[case[q][2]] += 1
                    case[q][0] += 1

            time += 1

        ans = min(ans, time)

    print("#{} {}".format(tc, ans))