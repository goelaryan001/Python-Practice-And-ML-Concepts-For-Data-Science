# Brute force:
# For every character, traverse the entire string again to count
# how many times it appears.
# The first character with frequency 1 is the answer.
# This takes O(N²) time.

# Optimized idea:
# First count the frequency of every character using a hashmap.
# Then traverse the string again.
# The first character whose frequency is 1 is the first unique character.
# If no such character exists, return -1.

class Solution:
    def firstUniqChar(self, s: str) -> int:
        count = {}

        # Count frequency of every character
        for ch in s:
            count[ch] = count.get(ch, 0) + 1

        # Find the first unique character
        for i, ch in enumerate(s):
            if count[ch] == 1:
                return i

        return -1