# Count how many people each person trusts nobody and how many trust them.
# The judge must satisfy:
# - trusted by n-1 people
# - trusts 0 people
#
# We can use two arrays:
# trust_count[i] -> how many people trust i
# out_count[i]   -> how many people i trusts
#
# The judge is the person with:
# trust_count[i] == n - 1 and out_count[i] == 0

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)
        out_count = [0] * (n + 1)

        for a, b in trust:
            out_count[a] += 1
            trust_count[b] += 1

        for person in range(1, n + 1):
            if trust_count[person] == n - 1 and out_count[person] == 0:
                return person

        return -1