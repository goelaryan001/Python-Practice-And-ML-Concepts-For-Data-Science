# Brute force:
# For every operation, we could recalculate the whole score history again
# to find the current total.
# That would be slow because every new operation may require scanning
# all previous results again -> O(N^2) or worse depending on how we do it.

# Optimized idea:
# Use a stack to store the valid round scores.
# Then:
# "C" -> remove last score
# "D" -> push double of last score
# "+" -> push sum of last two scores
# number -> push that number directly
#
# This works because we only need access to the most recent scores,
# and stack gives us that in O(1).

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []

        for op in operations:
            if op == "C":
                stack.pop()

            elif op == "D":
                stack.append(2 * stack[-1])

            elif op == "+":
                stack.append(stack[-1] + stack[-2])

            else:
                stack.append(int(op))

        return sum(stack)
