class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}
        for s in strs:
            s_sorted = "".join(sorted(s))
            if s_sorted in strMap:
                strMap[s_sorted].append(s)
            else:
                strMap[s_sorted] = [s]
        
        grouped_strs = []
        for key in strMap:
            grouped_strs.append(strMap[key])

        return grouped_strs 