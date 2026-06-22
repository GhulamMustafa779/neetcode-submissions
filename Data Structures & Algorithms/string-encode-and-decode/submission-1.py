class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""

        result = ""
        for st in strs:
            result += str(len(st)) + ','

        result += '#'
        for st in strs:
            result+=st

        return result

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        
        sizes = []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1

        i += 1
        res = []
        for sz in sizes:
            res.append(s[i:i + sz])
            i+=sz
        
        return res


        