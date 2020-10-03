class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        i = len(s)-1
        ans = 0
        while i>=0:
            if s[i]==' ' and ans>0:
                break
            while i>=0 and s[i]==' ':
                i -= 1
            if i>=0:    
                ans += 1
            else:
                break
            i-=1
        return ans