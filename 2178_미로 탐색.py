"""
문제
N×M크기의 배열로 표현되는 미로가 있다.

1	0	1	1	1	1
1	0	1	0	1	0
1	0	1	0	1	1
1	1	1	0	1	1
미로에서 1은 이동할 수 있는 칸을 나타내고, 0은 이동할 수 없는 칸을 나타낸다. 이러한 미로가 주어졌을 때, (1, 1)에서 출발하여 (N, M)의 위치로 이동할 때 지나야 하는 최소의 칸 수를 구하는 프로그램을 작성하시오. 한 칸에서 다른 칸으로 이동할 때, 서로 인접한 칸으로만 이동할 수 있다.

위의 예에서는 15칸을 지나야 (N, M)의 위치로 이동할 수 있다. 칸을 셀 때에는 시작 위치와 도착 위치도 포함한다.

입력
첫째 줄에 두 정수 N, M(2 ≤ N, M ≤ 100)이 주어진다. 다음 N개의 줄에는 M개의 정수로 미로가 주어진다. 각각의 수들은 붙어서 입력으로 주어진다.

출력
첫째 줄에 지나야 하는 최소의 칸 수를 출력한다. 항상 도착위치로 이동할 수 있는 경우만 입력으로 주어진다.
"""

from sys import stdin
from collections import deque

# 오 -> 아 -> 왼 -> 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
def bfs(y, x):
  q = deque()
  q.append((y, x))
  while(q):
    py, px = q.popleft()
    for k in range(4):
      nx = px + dx[k]
      ny = py + dy[k]
      if 0 <= nx < M and 0 <= ny < N:
        if visited[ny][nx] == False and graph[ny][nx] == 1:
          visited[ny][nx] = True
          graph[ny][nx] = graph[py][px] + 1
          q.append((ny, nx))



N, M = map(int, stdin.readline().split())



graph = []
visited = [[False for _ in range(M)] for _ in range(N)]
for _ in range(N):
  graph.append(list(map(int, stdin.readline().rstrip())))


bfs(0, 0)
print(graph[N-1][M-1])