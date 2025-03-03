class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """
        left = list()
        right = list()
        mid = list()
        for num in nums:
            if pivot < num:
                right.append(num)
            elif pivot > num:
                left.append(num)
            else: mid.append(num)
        return left + mid + right
            
        