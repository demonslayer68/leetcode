class Solution:
    def nextClosestTime(self, time: str) -> str:
        digits = [int(x) for x in time if x.isdigit()]
        digits = sorted(list(set(digits)))

        # lets start from right side and go case by case
        # 4th digit
        fourth = [x for x in digits if x > int(time[4])]
        if fourth:
            return time[:4] + str(fourth[0])

        # 3rd digit
        third = [x for x in digits if x > int(time[3]) and x < 6]
        if third:
            return time[:3] + str(third[0]) + str(digits[0])

        # 2nd digit
        limit = 3 if time[0] == "2" else 9
        second = [x for x in digits if x > int(time[1]) and x <= limit]
        if second:
            return time[0] + str(second[0]) + ":" + str(digits[0]) + str(digits[0])

        # 1st digit
        first = [x for x in digits if x in [0, 1, 2]]
        first_digit = first[(first.index(int(time[0])) + 1) % len(first)]
        return str(first_digit) + str(digits[0]) + ":" + str(digits[0]) + str(digits[0])