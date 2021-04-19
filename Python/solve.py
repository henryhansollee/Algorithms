import sys
sys.stdin = open('input.txt', 'r')

import sys
import copy
sys.setrecursionlimit(100000)

dr = [0, 0, -1, 1]
dc = [-1, 1, 0, 0]

def turn(l):
    tmp_a = []
    for i in range(2 ** l - 1, 2 ** n, 2 ** l):
        for j in range(0, 2 ** l, 1):
            tmp_b = []
            for a in range(j, 2 ** n, 2 ** l):
                for b in range(i, i - 2 ** l, -1):
                    tmp_b.append(lists[b][a])
            tmp_a.append(tmp_b)
    return tmp_a

def melt(melt_list):
    tmp = []
    for r in range(2 ** n):
        for c in range(2 ** n):
            cnt = 0
            for k in range(4):
                nr, nc = r + dr[k], c + dc[k]
                if 0 <= nr < 2 ** n and 0 <= nc < 2 ** n:
                    if melt_list[nr][nc] > 0:
                        cnt += 1
            if cnt < 3 and 0 < melt_list[r][c]:
                tmp.append([r, c])
    for rr, cc in tmp:
        melt_list[rr][cc] -= 1

def dfs(x, y):
    global cnt
    cnt += 1
    for k in range(4):
        nx, ny = x + dr[k], y + dc[k]
        if 0 <= nx < 2 ** n and 0 <= ny < 2 ** n:
            if lists[nx][ny] > 0:
                lists[nx][ny] = 0
                dfs(nx, ny)

n, q = map(int, input().split())
lists = [list(map(int, input().split())) for _ in range(2 ** n)]
l_list = list(map(int, input().split()))

for l in l_list:
    lists = copy.deepcopy(turn(l))
    melt(lists)

ans_a = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        ans_a += lists[i][j]
print(ans_a)

ans_b = 0
for i in range(2 ** n):
    for j in range(2 ** n):
        cnt = 0
        if lists[i][j] > 0:
            lists[i][j] = 0
            dfs(i, j)
            if ans_b < cnt:
                ans_b = cnt
print(ans_b)
