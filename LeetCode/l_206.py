# For each node:
# 1. Save the next node
# 2. Reverse curr.next to point to prev
# 3. Move prev and curr one step forward
#
# After the loop finishes, prev will be the new head.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # save next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev forward
            curr = nxt           # move curr forward

        return prev