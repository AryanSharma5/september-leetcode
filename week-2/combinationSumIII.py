import functools
class Solution:
    # @functools.lru_cache(maxsize = None)
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
    #     arr = list([i for i in range(1, 10)])
    #     ans = []
    #     for i in range(2**len(arr)):
    #         temp = []
    #         for j in range(len(arr)):
    #             if i&(1<<j) > 0:
    #                 temp.append(arr[j])
    #         if len(temp) == k:
    #             ans.append(temp)
    #     res = []
    #     for i in ans:
    #         if sum(i) == n:
    #             res.append(i)
    #     return res
    
        result = []
        intermediate = []
        self.backtrack(result, intermediate, 1, k, n)
        return result

    def backtrack(self, result, intermediate, start, k, n):
        if not n and not k:
            result.append(intermediate[:])
            return
        i = start
        while i<=10-k and i<=n:
            intermediate.append(i)
            self.backtrack(result, intermediate, start+1, k-1, n-i)
            intermediate.pop()
            i += 1