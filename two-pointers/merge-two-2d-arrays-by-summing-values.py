class Solution(object):
    def mergeArrays(self, nums1, nums2):
        """
        :type nums1: List[List[int]]
        :type nums2: List[List[int]]
        :rtype: List[List[int]]
        """
        d = {}
        for id, val in nums1:
            d[id] = d.get(id, 0) + val
        for id, val in nums2:
            d[id] = d.get(id, 0) + val
        return [[id, d[id]] for id in sorted(d.keys())]
