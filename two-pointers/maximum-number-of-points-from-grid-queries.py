class Solution:
    def maxPoints(self, grid: List[List[int]], queries: List[int]) -> List[int]:
        m, n = len(grid), len(grid[0])
        result = [0]* len(queries)
        directions = [(1,0),(-1,0),(0,1),(0,-1)] #down, up, left, right
        for q_idx, q in enumerate(queries):
            visited = [[False]*n for _ in range(m)]
            visited[0][0] = True
            count = 0
            bfs = deque([(0,0)])
            while bfs:
                current_m, current_n = bfs.popleft()
                if grid[current_m][current_n] >= q:
                    continue
                count +=1
                for dir_r, dir_c in directions:
                    new_m,new_n = current_m + dir_r, current_n + dir_c
                    if (0 <= new_m < m and 0 <= new_n < n and not visited[new_m][new_n] and grid[new_m][new_n] < q):
                        bfs.append((new_m,new_n))
                        visited[new_m][new_n] = True
            result[q_idx] = count
        return result

            
            

            

