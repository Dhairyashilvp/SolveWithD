class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            # if not stack:
            #     stack.append(c)
            if c in ["(","{","["]:
                stack.append(c)
            elif stack == []:
                return False
            elif (ord(c) != ord(stack[-1]) + 1) and (ord(c) != ord(stack[-1]) + 2):
                return False
            else:
                stack.pop()
            
        return stack == []
        # brackets = []
        # for i in s:
        #     if i == "(" or i == "[" or i == "{":
        #         brackets.append(i)
        #     else:
        #         if brackets == []:
        #             return False
        #         elif brackets[-1] != chr(ord(i) - 1) and brackets[-1] != chr(ord(i) - 2):
        #             return False
        #         else:
        #             brackets.pop()
        # return brackets == []
        # stack = []        
        # for c in s:
        #     if c in ['(', '[', '{']:
        #         stack.append(c)
        #     elif c == ')' and (not stack or stack.pop() != '('):
        #         return False
        #     elif c == ']' and (not stack or stack.pop() != '['):
        #         return False
        #     elif c == '}' and (not stack or stack.pop() != '{'):
        #         return False
            
        # return not stack
                