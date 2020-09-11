class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        # version1: 7.05.002.4               version2: 7.5.3
        v1, v2 = version1.split('.'), version2.split('.')
        for i in range(max(len(v1), len(v2))):
            ver1, ver2 = int(v1[i]) if i<len(v1) else 0, int(v2[i]) if i<len(v2) else 0
            if ver1<ver2:
                return -1
            elif ver1 > ver2:
                return 1
        return 0