# Brute force:
# Create a new string and append characters from the end to the start.
# But strings are immutable in Python, so this would take extra space O(N).

# Optimized idea:
# Since the array is mutable, use two pointers:
# one at the start and one at the end.
# Swap the characters, then move both pointers inward.
# This reverses the string in place.

class Solution:
    def reverseString(self, s: List[str]) -> None:
        l, r = 0, len(s) - 1

        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1