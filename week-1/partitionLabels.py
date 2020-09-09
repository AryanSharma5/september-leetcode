class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        last = {c:i for i,c in enumerate(S)}
        start = end = 0
        output = []
        for i,c in enumerate(S):
            end = max(end,last[c])
            if i == end:
                output.append(end-start+1)
                start = i + 1
        return output