class Solution:
    def isValid(self, s: str) -> bool:
        i = 0
        stack = collections.deque()
        map = {
            ')': "(",
            '}': "{",
            ']': "[",
        }
        while i < len(s):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            elif stack and stack[-1] == map[s[i]]:
                stack.pop()
            elif not stack or stack[-1] != map[s[i]]:
                return False
            i += 1

        return True if len(stack) == 0 else False


