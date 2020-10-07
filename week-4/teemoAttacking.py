class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
#         1, 5, 10, 15      duration = 4
#         ^
        
#         ans = 0 + 4 + 4 + 4 + 4 = 16
        if not timeSeries:
            return 0
        ans = duration
        for i in range(len(timeSeries)-1):
            ans += min(timeSeries[i+1] - timeSeries[i], duration)
        return ans