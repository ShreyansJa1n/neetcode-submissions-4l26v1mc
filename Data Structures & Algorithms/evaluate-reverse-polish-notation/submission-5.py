class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in range(len(tokens)):
            if tokens[i] in "+-*/":
                val2 = stack.pop()
                val1 = stack.pop()
                if tokens[i] == "+":
                    stack.append(val1+val2)
                elif tokens[i] == "-":
                    stack.append(val1-val2)
                elif tokens[i] == "*":
                    stack.append(val1*val2)
                if tokens[i] == "/":
                    stack.append(int(val1/val2))
            else:
                stack.append(int(tokens[i]))
        return stack[-1]