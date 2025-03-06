For the `find-missing-and-repeat` question, i found another better (also clearer) solution:

```python
class Solution(object):
    def findMissingAndRepeatedValues(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: List[int]
        """
        count = [1] + [0] * len(grid)**2  
        for row in grid:
            for num in row:
                count[num] += 1
        return [count.index(2), count.index(0)]
```
