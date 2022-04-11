class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closing = [')', '}', ']']
        pairs = {'(': ')', '{': '}', '[': ']'}
        for elem in s:
            if elem in closing:
                if not stack or pairs[stack.pop()] != elem:
                    return False
            else:
                stack.append(elem)

        return not len(stack)
