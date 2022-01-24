class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        firstupper = word[0].isupper()
        upper = 1
        lower = 1
        for i in range(1, len(word)):
            if word[i].isupper():
                lower = 0
            else:
                upper = 0
            if not upper and not lower or upper and not firstupper:
                return False
        return True
