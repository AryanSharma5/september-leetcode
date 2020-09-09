class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        n = len(A)
        LA = [(i, j) for i in range(n) for j in range(n) if A[i][j] == 1]
        LB = [(i, j) for i in range(n) for j in range(n) if B[i][j] == 1]
        counts = collections.defaultdict(int)
        res = 0
        for i in LA:
            for j in LB:
                counts[(i[0]-j[0], i[1]-j[1])] += 1
                res = max(res, counts[(i[0]-j[0], i[1]-j[1])])
        return res