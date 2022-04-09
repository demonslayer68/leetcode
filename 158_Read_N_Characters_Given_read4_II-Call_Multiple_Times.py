# The read4 API is already defined for you.
# def read4(buf4: List[str]) -> int:

class Solution:
    leftover = []

    def __init__(self):
        self.leftover = []

    def read(self, buf: List[str], n: int) -> int:
        i = 0
        buf4 = []
        # if there is leftover, then read that first
        while i < n and len(self.leftover):
            buf[i] = self.leftover.pop(0)
            i += 1

        # once leftover is done, start reading data
        while i < n:
            # print("s", i, buf, buf4)
            if not buf4:
                buf4 = [''] * 4
                count = read4(buf4)
                if not count:
                    break
            buf[i] = buf4.pop(0)
            i += 1
            # print(i, buf, buf4)

        # if there is leftover, store it
        while buf4:
            self.leftover.append(buf4.pop(0))
        return i
