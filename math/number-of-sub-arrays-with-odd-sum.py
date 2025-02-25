class Solution(object):
    def numOfSubarrays(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        m = 10**9 +7 
        evenCount = 1
        oddCount = 0

        prefixSum = 0
        result = 0

        for num in arr:
            prefixSum += num
            if prefixSum % 2 == 0:
                result += oddCount
                evenCount += 1
            else:
                result += evenCount
                oddCount +=1

            result %= m

        return result % m