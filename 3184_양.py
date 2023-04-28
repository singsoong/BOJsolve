"""
문제
미키의 뒷마당에는 특정 수의 양이 있다. 그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.

마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.

한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.

아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.

입력
첫 줄에는 두 정수 R과 C가 주어지며(3 ≤ R, C ≤ 250), 각 수는 마당의 행과 열의 수를 의미한다.

다음 R개의 줄은 C개의 글자를 가진다. 이들은 마당의 구조(울타리, 양, 늑대의 위치)를 의미한다.

출력
하나의 줄에 아침까지 살아있는 양과 늑대의 수를 의미하는 두 정수를 출력한다.
"""

from sys import stdin
from collections import deque

# 오 아 왼 위
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

# R: row(y) C: column(x)
R, C = map(int, stdin.readline().rstrip().split(" "))
graph = [[0 for _ in range(C+1)] for _ in range(R+1)]
visited = [[False for _ in range(C+1)] for _ in range(R+1)]


# bfs
def bfs(y, x, sheep, wolf):
  q = deque()
  q.append((y, x))
  s = sheep # 양
  w = wolf # 늑대
  while q:

    py, px = q.popleft()
    for k in range(4):
      nx = px + dx[k]
      ny = py + dy[k]
      if 0 <= nx <= C and 0 <= ny <= R:
        if visited[ny][nx] == False and graph[ny][nx] == ".":
          visited[ny][nx] = True
          q.append((ny, nx))
        elif visited[ny][nx] == False and graph[ny][nx] == "o":
          visited[ny][nx] = True
          s += 1
          q.append((ny, nx))
        elif visited[ny][nx] == False and graph[ny][nx] == "v":
          visited[ny][nx] = True
          q.append((ny, nx))
          w += 1
  if s > w:
    return s, 0
  else:
    return 0, w

wolf = 0
sheep = 0
for i in range(R):
  sentence = stdin.readline().rstrip()
  for j in range(len(sentence)):
    graph[i+1][j+1] = sentence[j]

for y in range(1, R+1):
  for x in range(1, C+1):
    if visited[y][x] == False and graph[y][x] == ".":
      visited[y][x] = True
      s, w = bfs(y, x, 0, 0)
      sheep += s
      wolf += w
    elif visited[y][x] == False and graph[y][x] == "o":
      visited[y][x] = True
      s, w = bfs(y, x, 1, 0)
      sheep += s
      wolf += w
    elif visited[y][x] == False and graph[y][x] == "v":
      visited[y][x] = True
      s, w = bfs(y, x, 0, 1)
      sheep += s
      wolf += w

print(sheep, wolf)