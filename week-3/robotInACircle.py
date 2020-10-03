class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        fullinstructions = instructions*4
        dirs = [[0,1], [-1,0], [0,-1], [1,0]]
        d = 0
        r, c = 0, 0
        for inst in fullinstructions:
            if inst == "G":
                r, c = r+dirs[d][0], c+dirs[d][1]
            elif inst == "L":
                d = (d+1)%4
            else:
                d = (d+3)%4
        return r==0 and c==0