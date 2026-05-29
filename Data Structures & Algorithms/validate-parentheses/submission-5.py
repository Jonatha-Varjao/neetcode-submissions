class Solution:
    def isValid(self, s: str) -> bool:
        def peek(stack):
            if stack:
                return stack[-1]
            return False

        stack = []

        if len(s) == 1 :
            return False

        for char in s:
            print(char,stack)
            if char == "(" or char == "{" or char == "[":
                stack.append(char) 
            elif char == ")" and peek(stack) == "(" :
                stack.pop()
            elif char == "}" and peek(stack) == "{":
                stack.pop()
            elif char == "]" and peek(stack) == "[":
                stack.pop()
            else:
                return False
        
        return True if not stack else False
