class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        output = {}
        for elem in strs:
            # convert to tuple, since its immutable, so can be used as a key
            tup = tuple(sorted(elem))
            if tup in output:
                output[tup].append(elem)
            else:
                output[tup] = [elem]
        return output.values()
