class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]
        added = False
        temp = []
        for i in intervals:
            if not added and newInterval[0] < i[0]:
                temp.append(newInterval)
                added = True
            
            temp.append(i)
        if not added:
            temp.append(newInterval)
        res = []
        for i in temp:
            if res and i[0] <= res[-1][-1]:
                res[-1][-1] = max(i[1], res[-1][-1])
            else:
                res += [i]
        return res