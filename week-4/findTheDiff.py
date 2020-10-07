class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        pool = {}
        for i in s:
            if i not in pool:
                pool[i] = 0
            else:
                pool[i] += 1
        for i in t:
            if i not in pool or pool[i]<0:
                return i
            else:
                pool[i] -= 1