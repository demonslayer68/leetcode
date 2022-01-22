class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        output = []
        # find element with binary search
        min = 0
        max = len(arr) - 1
        while min <= max:
            index = (min + max) // 2
            if arr[index] <= x:
                if index == len(arr) - 1 or arr[index + 1] >= x:
                    break
                else:
                    min = index + 1
            else:
                max = index - 1

        left = index
        right = index + 1
        while len(output) < k:
            if left >= 0 and right < len(arr) and x - arr[left] <= arr[right] - x:
                output.insert(0, arr[left])
                left -= 1
            elif left < 0 or right < len(arr) and x - arr[left] > arr[right] - x:
                output.append(arr[right])
                right += 1
            else:
                output.insert(0, arr[left])
                left -= 1
        return output

