class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = 10**9 + 7
        
        graph = [[] for _ in range(n)]
        for u, v, t in roads:
            graph[u].append((v, t))
            graph[v].append((u, t))
        
        dist = [float('inf')] * n
        ways = [0] * n
        dist[0] = 0
        ways[0] = 1
        
        pq = [(0, 0)]
        
        while pq:
            curr_time, node = heapq.heappop(pq)

            if curr_time > dist[node]:
                continue

            for neighbor, travel_time in graph[node]:
                time_to_neighbor = curr_time + travel_time
                
                if time_to_neighbor < dist[neighbor]:
                    dist[neighbor] = time_to_neighbor
                    ways[neighbor] = ways[node]
                    heapq.heappush(pq, (time_to_neighbor, neighbor))

                elif time_to_neighbor == dist[neighbor]:
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD
        
        return ways[n - 1]
        