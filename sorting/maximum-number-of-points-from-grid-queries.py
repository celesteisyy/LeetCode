# Tried BFS method but cooked with 17/21... So... Here's the DFS solution:
class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0] * len(queries)
        directions = [(1,0),(-1,0),(0,1),(0,-1)]
        for idx, q in enumerate(queries):
            if grid[0][0] >= q:
                result[idx] = 0
                continue
            visited = [[False]*n for _ in range(m)]
            dfs = [(0,0)]
            visited[0][0] = True
            count = 0

            while dfs:
                i,j = dfs.pop()
                if grid[i][j] >= q:
                    continue
                count += 1
                for dir_r, dir_c in directions:
                    ni, nj = i + dir_r, j + dir_c
                    if 0 <= ni < m and 0 <= nj < n and not visited[ni][nj] and grid[ni][nj] < q:
                        visited[ni][nj] = True
                        dfs.append((ni,nj)) 
            
            result[idx] = count
        return result
