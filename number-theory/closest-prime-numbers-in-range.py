class Solution(object):
    def closestPrimes(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        sieve = [True] * (right + 1)
        sieve[0] = sieve[1] = False
        for p in range(2,int(right ** 0.5) + 1):
            if sieve[p]:
                for i in range(p**2, right+1,p):
                    sieve[i] = False
        prev = -1
        gap = float("inf")
        ans = [-1,-1]
        for num in range(left, right+1):
            if sieve[num]:
                if prev !=-1 and num - prev < gap:
                    gap = num -prev
                    ans = [prev,num]
                prev = num
        return ans