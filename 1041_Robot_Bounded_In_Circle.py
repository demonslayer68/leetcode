class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = 0
        vert = 0
        hor = 0
        for i in range(len(instructions)):
            if instructions[i] == "G":
                if direction == 0:
                    hor += 1
                elif direction == 1:
                    vert += 1
                elif direction == 2:
                    hor -= 1
                else:
                    vert -= 1
            elif instructions[i] == "L":
                direction = (direction + 1) % 4
            else:
                direction = (direction - 1) % 4

        if direction == 0:
            return vert == 0 and hor == 0
        else:
            return True

