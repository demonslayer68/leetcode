class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        replacements = {}
        output = ""
        i = 0
        j = 0
        # sort, so that you can pick the replacements in order
        sorted_indices = sorted(indices)
        sorted_sources = [x for _, x in sorted(zip(indices, sources), key=lambda pair: pair[0])]
        sorted_targets = [x for _, x in sorted(zip(indices, targets), key=lambda pair: pair[0])]
        while i < len(s) and j < len(indices):
            # if this is the case, either use the replacement or discard it
            if sorted_indices[j] == i:
                # use
                if i + len(sorted_sources[j]) <= len(s) and s[i:i + len(sorted_sources[j])] == sorted_sources[j]:
                    output += sorted_targets[j]
                    i += len(sorted_sources[j])
                # discard
                else:
                    output += s[i]
                    i += 1
                j += 1
            # no replacement
            else:
                output += s[i]
                i += 1
        output += s[i:]
        return output
