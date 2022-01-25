class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        atmem = {}
        pacmem = {}
        output = []

        def rec_flow(i, j, dir):
            # checking pacific
            if dir == -1 and (i, j) not in pacmem:
                pacmem[(i, j)] = i - 1 < 0 or j - 1 < 0 or (
                            heights[i - 1][j] <= heights[i][j] and rec_flow(i - 1, j, -1)) or (
                                             heights[i][j - 1] <= heights[i][j] and rec_flow(i, j - 1, -1))
                print(i, j, i - 1 < 0 or j - 1 < 0, pacmem[(i, j)])

            if dir == 1 and (i, j) not in atmem:
                atmem[(i, j)] = i + 1 >= len(heights) or j + 1 >= len(heights[0]) or (
                            heights[i + 1][j] <= heights[i][j] and rec_flow(i + 1, j, 1)) or (
                                            heights[i][j + 1] <= heights[i][j] and rec_flow(i, j + 1, 1))
            if dir == 1:
                return atmem[(i, j)]
            else:
                return pacmem[(i, j)]

                # print( i, j, atmem[(i, j)], pacmem[(i, j)] )

        # rec_flow(1, 4, -1)

        for x in range(len(heights)):
            for y in range(len(heights[0])):
                if rec_flow(x, y, 1) and rec_flow(x, y, -1):
                    output.append((x, y))

        return output


obj = Solution()
print(obj.pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))