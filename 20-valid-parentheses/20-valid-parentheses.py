class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i == '(' or i == '{' or i == '[':
                stack.append(i)
            elif i == ')' and stack != []:
                if stack.pop() != '(':
                    return False
            elif i == ']' and stack != []:
                if stack.pop() != '[':
                    return False
            elif i == '}' and stack != []:
                if stack.pop() != '{':
                    return False
            else:
                return False

        if stack != []:  
            return False
        return True 