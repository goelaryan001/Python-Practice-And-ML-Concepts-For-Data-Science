# Brute force:
# Try every number from 1 to num and check whether i * i == num.
# This works, but it is too slow for large num.
# Time: O(N)

# Optimized idea:
# The square of numbers grows in sorted order:
# 1^2, 2^2, 3^2, 4^2, ...
# So instead of checking every number, use binary search.
# For a middle value mid:
# - if mid * mid == num -> perfect square found
# - if mid * mid < num -> search right half
# - if mid * mid > num -> search left half
#
# This reduces the search space by half each time.

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        l, r = 1, num

        while l <= r:
            mid = (l + r) // 2
            square = mid * mid

            if square == num:
                return True
            elif square < num:
                l = mid + 1
            else:
                r = mid - 1

        return False