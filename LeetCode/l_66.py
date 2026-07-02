# Since we only need to add 1, start from the last digit.
# If the digit is less than 9, just add 1 and return.
# If the digit is 9, it becomes 0 and we carry 1 to the left.
# Continue until carry becomes 0.
# If all digits were 9, we need to add a new leading 1.

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0

        return [1] + digits