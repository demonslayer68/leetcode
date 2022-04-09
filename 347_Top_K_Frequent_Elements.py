from collections import Counter
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #cnt = Counter(nums)
        cnt = defaultdict(int)
        for i in nums:
            cnt[i] += 1
        sorted_cnt = sorted(cnt, key=cnt.get, reverse=True)[:k]
        return sorted_cnt
