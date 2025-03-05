class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        cells = 0
        for i in range(1, n + 1):
            cells += i ** 2
        return cells