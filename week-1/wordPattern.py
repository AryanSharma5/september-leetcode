class Solution:
    def wordPattern(self, pattern: str, string: str) -> bool:
        patternMap = {}
        j = 0
        for i in pattern:
            if i not in patternMap:
                patternMap[i] = j
                j += 1
        stringMap = {}
        s1 = ''
        for i in pattern:
            s1 += str(patternMap[i])
        j = 0
        for word in string.split():
            if word not in stringMap:
                stringMap[word] = j
                j += 1
        s2 = ''
        for word in string.split():
            s2 += str(stringMap[word])
        return s1 == s2