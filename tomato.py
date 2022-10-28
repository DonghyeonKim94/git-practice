# 7569 토마토
from collections import deque

dxy = [(-1, 0), (1, 0), (0, -1), (0, 1)]

M, N, H = map(int, input().split())
tomato = []
for i in range(H):
    tomato.append([list(map(int, input().split())) for _ in range(N)])

queue = deque([])
cnt = M * N * H
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == -1:
                cnt -= 1
            elif tomato[i][j][k] == 1:
                cnt -= 1
                queue.append((i, j, k, 0))

result = 0
while queue:
    if not cnt:
        break

    v = queue.popleft()

    for d in dxy:
        nx = v[1] + d[0]
        ny = v[2] + d[1]
        if 0 <= nx < N and 0 <= ny < M and not tomato[v[0]][nx][ny]:
            tomato[v[0]][nx][ny] = 1
            cnt -= 1
            result = v[3] + 1
            queue.append((v[0], nx, ny, v[3] + 1))

    for h in (-1, 1):
        nh = v[0] + h
        if 0 <= nh < H and not tomato[nh][v[1]][v[2]]:
            tomato[nh][v[1]][v[2]] = 1
            cnt -= 1
            result = v[3] + 1
            queue.append((nh, v[1], v[2], v[3] + 1))

if cnt:
    print(-1)
else:
    print(result)