class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in '([{':
                stack.append(char)
            elif char == ')':
                if stack and stack.pop() == '(':
                    continue
                else:
                    return False
            elif char == '}':
                if stack and stack.pop() == '{':
                    continue
                else:
                    return False      
            elif char == ']':
                if stack and stack.pop() == '[':
                    continue
                else:
                    return False
        if stack:
            return False
        else:
            return True