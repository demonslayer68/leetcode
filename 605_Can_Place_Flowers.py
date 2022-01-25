class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # setting at 1, to account for left edge
        zcount = 1
        if not n:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i]:
                zcount = 0
            else:
                zcount += 1
                # reset to 1, since we should count the extra 0 we have left for previous plant addition
                if zcount == 3:
                    zcount = 1
                    n -= 1
                    if not n:
                        return True
        # checking to account for right edge
        if zcount == 2:
            n -= 1
        if not n:
            return True
        else:
            return False

