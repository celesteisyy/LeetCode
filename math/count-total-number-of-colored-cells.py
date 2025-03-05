class Solution(object):
    def coloredCells(self, n):
        """
        :type n: int
        :rtype: int
        """
        cells = 1
        for i in range(1, n + 1):
            added_cells = 4*(i-1)
            cells = cells+added_cells
        return cells