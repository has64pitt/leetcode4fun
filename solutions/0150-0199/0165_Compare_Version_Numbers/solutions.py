class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        version1 = version1.split('.')
        version2 = version2.split('.')

        
        N1 = len(version1)
        N2 = len(version2)
        
        N = max(N1, N2)
        
        for _ in range(N1, N):
            version1.append('0')

        for _ in range(N2, N):
            version2.append('0')
            
        for v1, v2 in zip(version1, version2):
            v1 = int(v1)
            v2 = int(v2)
            if v1 < v2:
                return -1
            elif v1 > v2:
                return 1
            

        return 0