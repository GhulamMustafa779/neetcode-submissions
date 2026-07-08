class Solution:

    def encode(self, strs: List[str]) -> str:
        st = ""
        for s in strs:
            st += str(len(s)) + "#"
        
        st = st + "$"
        for s in strs:
            st += s
        
        return st

    def decode(self, s: str) -> List[str]:
        sizes = []
        res = []

        i = 0
        while s[i] != "$":
            num = ""
            while s[i] != "#":
                num += s[i]
                i += 1

            sizes.append(int(num))
            i += 1
        
        i += 1
        for szs in sizes:
            res.append(s[i:i+szs])
            i += szs
        
        return res
 