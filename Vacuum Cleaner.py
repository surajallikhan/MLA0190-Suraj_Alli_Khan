from collections import deque

grid = [
    "##########",
    "#S..#..D##",
    "#..##..D##",
    "#D..#....#",
    "##..##..D#",
    "#D.......#",
    "##########"
]

n, m = len(grid), len(grid[0])
start = None
dirt = []

for i in range(n):
    for j in range(m):
        if grid[i][j] == 'S':
            start = (i, j)
        if grid[i][j] == 'D':
            dirt.append((i, j))

def nbrs(x, y):
    for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
        nx, ny = x+dx, y+dy
        if 0 <= nx < n and 0 <= ny < m and grid[nx][ny] != '#':
            yield nx, ny

def bfs(src):
    q = deque([src])
    dist = {src: 0}
    parent = {src: None}
    while q:
        x, y = q.popleft()
        for nx, ny in nbrs(x, y):
            if (nx, ny) not in dist:
                dist[(nx, ny)] = dist[(x, y)] + 1
                parent[(nx, ny)] = (x, y)
                q.append((nx, ny))
    return dist, parent

def build_path(parent, target):
    p, cur = [], target
    while cur is not None:
        p.append(cur)
        cur = parent[cur]
    return p[::-1]

pos = start
remaining = set(dirt)
full_path = [pos]

while remaining:
    dist, par = bfs(pos)
    nxt = min(remaining, key=lambda c: dist[c])
    seg = build_path(par, nxt)
    full_path += seg[1:]
    pos = nxt
    remaining.remove(nxt)

print("Total moves:", len(full_path)-1)
print("Path:")
for r, c in full_path:
    print(r, c)