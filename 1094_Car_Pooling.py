class Solution:
    def carPooling(self, trips: list[list[int]], capacity: int) -> bool:
        tolist = []
        trips.sort(key=lambda x: x[1])
        for i in range(len(trips)):
            start = trips[i][1]
            while len(tolist) and tolist[0][2] <= start:
                capacity += tolist.pop(0)[0]
            capacity -= trips[i][0]
            if capacity < 0:
                return False
            j = 0
            while j < len(tolist) and tolist[j][2] < trips[i][2]:
                j += 1
            tolist.insert(j, trips[i])
        return True

