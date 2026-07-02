# Brute force:
# Keep trying to form the word "balloon" by searching for each required
# character in the string and removing it once used.
# Repeat until one of the required characters is unavailable.
# This would require repeatedly scanning the string, leading to O(N^2).

# Optimized idea:
# Count the frequency of every character once using a hashmap.
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}

        for ch in text:
            count[ch] = count.get(ch, 0) + 1

        return min(
            count.get("b", 0),
            count.get("a", 0),
            count.get("l", 0) // 2,
            count.get("o", 0) // 2,
            count.get("n", 0)
        )