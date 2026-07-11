class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        tMap = {}
        for i in range(len(t)):
            tMap[t[i]] = tMap.get(t[i], 0) + 1

        have, need = 0, len(tMap)

        sMap = {}
        l = 0
        res, minLen = [-1, -1], float('inf')
        for r in range(len(s)):
            c = s[r]
            sMap[c] = sMap.get(c, 0) + 1
            if c in tMap and tMap[c] == sMap[c]:
                have += 1
            
            while have == need:

                if (r - l + 1) < minLen:
                    res = [l, r]
                    minLen = r - l + 1

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1

        l, r = res
        return s[l: r + 1] if minLen != float('-inf') else ""
