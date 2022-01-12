class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, newColor: int) -> list[list[int]]:
        color = image[sr][sc]
        # in this case, nothing is required
        if color == newColor:
            return image

        def recursive_color(sr, sc):
            # check if we hit the edge, else apply recursion
            if 0 <= sr < len(image) and 0 <= sc < len(image[0]) and color == image[sr][sc]:
                image[sr][sc] = newColor
                for pair in [[sr-1, sc], [sr+1, sc], [sr, sc-1], [sr, sc+1]]:
                    recursive_color(pair[0], pair[1])

        recursive_color(sr, sc)
        return image
