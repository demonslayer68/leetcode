class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        output = 0
        for word in words:
            i = j = 0
            while j < len(word):
                count = 0
                wordcount = 1
                while j < len(word) - 1 and word[j] == word[j + 1]:
                    wordcount += 1
                    j += 1
                while i < len(s) and s[i] == word[j]:
                    i += 1
                    count += 1
                if count < wordcount or count < 3 and count != wordcount:
                    break
                j += 1
            if j == len(word) and i == len(s):
                output += 1
        return output

