# SWEA: 1952. 수영장

# --- 문제 요약 ---

# 가장 적은 비용으로 수영장을 이용할 방법을 찾고 있음

# 1일 이용권: 1일 이용 가능
# 1달 이용권: 1달 이용 가능, 매달 1일부터 시작
# 3달 이용권: 연속된 3달 이용 가능, 매달 1일부터 시작, 해가 지나면 없어지고 새로 사야함
# 1년 이용권: 1년 이용 가능, 매년 1월 1일 시작

# 입력으로 각 이용권의 요금과 각 달의 계획이 주어짐
# 가장 적은 비용으로 수영장을 이용할 수 있는 방법을 찾고, 그 비용을 출력

# --- 문제 풀이 ---

def search_plan(depth, price):
    global months, tickets, ans
    if depth >= 11:
        ans = min(ans, price)
        return
    search_plan(depth + 1, price + (months[depth] * tickets[0]))
    search_plan(depth + 1, price + tickets[1])
    search_plan(depth + 3, price + tickets[2])

# Step 1. 입출력
t = int(input())
for tc in range(1, t+1):
    tickets = list(map(int, input().split()))
    months = list(map(int, input().split()))
    ans = tickets[3]

    # Step 2. 방법 찾는 함수 만들기
    search_plan(0, 0)

    print("#{} {}".format(tc, ans))