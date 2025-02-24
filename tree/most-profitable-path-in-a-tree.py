class Solution(object):
    def mostProfitablePath(self, edges, bob, amount):
        """
        :type edges: List[List[int]]
        :type bob: int
        :type amount: List[int]
        :rtype: int
        """
        n = len(amount)
        graph = [[] for _ in range(n)]
        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        bobTime = [float('inf')]*n
        def dfs_bob(cur, parent, time):
            if cur == 0:
                bobTime[cur] = time
                return True
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                if dfs_bob(nxt, cur, time+1):
                    bobTime[cur] = time
                    return True
            return False

        dfs_bob(bob, -1, 0)
        self.res = -float('inf')

        def dfs_alice(cur,parent, time, profit):
            if time < bobTime[cur]:
                profit += amount[cur]
            elif time == bobTime[cur]:
                profit += amount[cur] // 2
            
            if cur != 0 and len(graph[cur]) == 1:
                self.res = max(self.res,profit)
                return
            
            for nxt in graph[cur]:
                if nxt == parent:
                    continue
                dfs_alice(nxt,cur,time +1,profit)
        dfs_alice(0,-1,0,0)
        return self.res