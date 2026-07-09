class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        if size <= 1:
            return size
        
        l = 0
        r = 1
        maxLen = 1
        temp = s[l]
        while r < size:
            if s[r] in temp:
                maxLen = max(maxLen, len(temp))
                while l < r:
                    if s[l] == s[r]:
                        break
                    else:
                        l += 1
                l += 1
                r = l + 1
                temp = s[l]
            else:
                temp += s[r]
                r += 1

        maxLen = max(maxLen, len(temp))
        return maxLen
                        
            