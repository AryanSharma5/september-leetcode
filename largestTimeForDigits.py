class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        permutes = []
        self.findPermutations(A, permutes, len(A))
        new = sorted([''.join([str(i) for i in per]) for per in permutes], reverse = True)        
        #print(new)
        for per in new:
            if per[:2]<='23' and per[2:]<='59':
                #print(per[:2] + ':' + per[2:])
                return per[:2] + ':' + per[2:]
        return ''
    
    def findPermutations(self, A, permutes, n):
        if n==1:
            permutes.append(A[:])
            return
        for i in range(n):
            self.findPermutations(A, permutes, n-1)
            if n&1:
                A[0], A[n-1] = A[n-1], A[0]
            else:
                A[i], A[n-1] = A[n-1], A[i]