class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        fraction = [w / q for w, q in zip(wage, quality)]
        sorted_data = sorted([(f, w, q) for f, w, q in zip(fraction, wage, quality)], key=lambda x: x[0])
        q_heap = []
        qsum = 0
        cost = float("inf")
        for f, w, q in sorted_data:
            qsum += q
            heapq.heappush(q_heap, -q)
            # print(f, w, q, qsum, q_heap)

            if len(q_heap) > k:
                pop_elem = heapq.heappop(q_heap)
                qsum += pop_elem

            if len(q_heap) == k:
                cost = min(cost, f * qsum)

        return cost
