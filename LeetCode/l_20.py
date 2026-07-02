# Use a stack.
#
# Whenever we see an opening bracket:
# push it onto the stack.
#
# Whenever we see a closing bracket:
# it should match the most recent opening bracket.
# If it doesn't match (or stack is empty), return False.
#
# At the end, the stack should be empty.
# If it's not, there are unmatched opening brackets.

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }

        for c in s:
            if c in closeToOpen:
                if stack and stack[-1] == closeToOpen[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)

        return len(stack) == 0
#I use a stack because brackets follow a Last-In-First-Out pattern. Every opening bracket is pushed onto the stack. When I encounter a closing bracket, it must match the most recently seen opening bracket, which is on top of the stack. If it doesn't match or the stack is empty, the string is invalid. After processing the entire string, the stack should be empty if all brackets were matched correctly.