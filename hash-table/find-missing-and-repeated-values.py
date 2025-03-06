class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        n = len(grid)
        total = n*n
        freq = [0]*(total+1)
        for row in grid:
            for num in row:
                freq[num] +=1
        ans = [None,None]
        for i in range(1, total+1):
            if freq[i] == 2:
                ans[0] = i
            elif freq[i] == 0:
                ans[1] = i
        return ans