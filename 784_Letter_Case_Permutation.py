class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        output = [""]
        for char in s:
            if char.isalpha():
                output = [ x + y for x in output for y in [char.upper(), char.lower()] ]
            else:
                output = [ x + char for x in output ]
        return output