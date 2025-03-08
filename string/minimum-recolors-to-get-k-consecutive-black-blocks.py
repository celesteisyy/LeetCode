class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        white = blocks[:k].count("W")
        min_rec = white
        for i in range(k,len(blocks)):
            if blocks[i-k] == "W":
                white -= 1
            if blocks[i] == "W":
                white +=1
            min_rec = min(min_rec, white)
        return min_rec
