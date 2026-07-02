# Brute force:
# Keep adding 1, 2, 3, 4... coins until we run out.
# Example: n = 5
# row 1 needs 1 -> remaining 4
# row 2 needs 2 -> remaining 2
# row 3 needs 3 -> not enough
# Answer = 2
#
# This works, but in the worst case we may keep counting row by row
# up to sqrt(n) times.

# Optimized idea:
# Total coins needed for k full rows is:
# 1 + 2 + 3 + ... + k = k(k+1)/2
#
# We want the largest k such that:
# k(k+1)/2 <= n
#
# Since this grows monotonically, we can use binary search.

class Solution:
    def arrangeCoins(self, n: int) -> int:
        l, r = 0, n

        while l <= r:
            mid = (l + r) // 2
            coins = mid * (mid + 1) // 2

            if coins == n:
                return mid
            elif coins < n:
                l = mid + 1
            else:
                r = mid - 1

        return r