class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for i in range(len(tokens)):
            token = tokens[i]
            if token in operators:
                res = 0
                el1 = int(stack.pop())
                el2 = int(stack.pop())
                if token == '+':
                    res = el2 + el1
                elif token == '-':
                    res = el2 - el1
                elif token == '*':
                    res = el2 * el1
                elif token == '/':
                    res = int(el2 / el1)
                stack.append(str(res))
            else:
                stack.append(tokens[i])
        
        ans = int(stack.pop())
        return ans