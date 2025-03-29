class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        sorted_q = sorted((q,i) for i,q in enumerate(queries))
        result = [0] * len(queries)

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        visited = [[False] * n for _ in range(m)]
        bfs = deque([(0, 0)])
        count = 0
        for q_idx, q in sorted_q:
            if not visited[0][0] and grid[0][0] < q:
                visited[0][0] =True
                bfs.append((0,0))
                count +=1
            while bfs:
                i, j = bfs.popleft()
                for dir_r, dir_c in directions:
                    ni, nj = i + dir_r, j + dir_c
                    if 0 <= ni <m and 0 <= nj <n and not visited[ni][nj] and grid[ni][nj] < q:
                       visited[ni][nj] = True
                       bfs.append((ni,nj))
                       count +=1
            result[idx] = count
        return result  