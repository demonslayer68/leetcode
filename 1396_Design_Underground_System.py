'''
marked this mainly for the system design solution. Otherwise its straightforward
'''

from collections import defaultdict

class UndergroundSystem:

    def __init__(self):
        self.checkin = {}
        self.times = defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
         self.checkin[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        in_station, in_t = self.checkin[id]
        self.times[(in_station, stationName)].append(t - in_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        times = self.times[(startStation, endStation)]
        return sum(times) / len(times)


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)