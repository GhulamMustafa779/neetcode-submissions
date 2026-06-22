class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sorted_s = sorted(s)
        # sorted_t = sorted(t)
        # return sorted_s == sorted_t
        counter = [0]*26
        for sc in s:
            counter[ord(sc)-ord('a')]+=1
        for tc in t:
            counter[ord(tc)-ord('a')]-=1
        for c in counter:
            if c!=0:
                return False
        return True