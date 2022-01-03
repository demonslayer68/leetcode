from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, time: list[int]) -> int:
        time = [i % 60 for i in time]
        counter = Counter(time)
        if 0 in counter and counter[0] > 1:
            count = (counter[0] * (counter[0] - 1)) / 2
        else:
            count = 0

        if 30 in counter:
            count = count + (counter[30] * (counter[30] - 1)) / 2
        for key in counter:
            if key >= 30 or key == 0:
                continue
            if 60 - key in counter:
                count = count + counter[key] * counter[60 - key]
        return int(count)


