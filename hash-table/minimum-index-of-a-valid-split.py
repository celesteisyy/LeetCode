class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count, candidate = 0, None
        for num in nums:
            if count == 0:
                candidate = num
                count = 1
            elif candidate == num:
                count += 1
            else: count -=1
        dominate = candidate
        total = nums.count(dominate)
        prefix_count = 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] == dominate:
                prefix_count +=1
            if prefix_count *2 >(i+1) and (total - prefix_count)*2 > (n-i-1):
                return i
        return -1
