from collections import deque

class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        m, n = len(grid), len(grid[0])
        direc = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        qe = deque([(0, 0, health)])  
        visited = set([(0, 0, health)])
        while qe:
            r, c, h = qe.popleft()
            if r == m - 1 and c == n - 1 and h >= 1:
                return True
            
            for dr, dc in direc:
                nr, nc = r + dr, c + dc
                
                if 0 <= nr < m and 0 <= nc < n:
                    nh = h - 1 if grid[nr][nc] == 1 else h
                    if nh > 0 and (nr, nc, nh) not in visited:
                        qe.append((nr, nc, nh))
                        visited.add((nr, nc, nh))
        return False