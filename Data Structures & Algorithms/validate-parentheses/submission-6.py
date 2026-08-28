from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: 
            return False
        stack = deque()
        for element in s: 
            if element == "(": 
                stack.append(element)
            elif element == "{": 
                stack.append(element)
            elif element == "[": 
                stack.append(element)
            else:
                if not stack: 
                    return False
                if ord(element) - 2 == ord(stack[-1]) or ord(element) - 1 == ord(stack[-1]):
                    stack.pop()
                else: 
                    return False
        if not stack: 
            return True
        else:
            return False
        
        