class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        ans=''
        for i in range(0,len(s)//2):
            ans+=s[i]
            if s==len(s)//len(ans)*ans:return True
        return False