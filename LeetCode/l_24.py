#here some parts which are tricky is how to connect one with 4, make 3 at end so connect it will null, 
#we will be using a dummy node as head
#d-1-2-3-4
#. p c
#d-2-1-3-4
#.     p.c

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode(0,head)
        prev,curr=dummy,head
        while curr and curr.next:
            #save ptrs
            nxtPair=curr.next.next
            second=curr.next

            #reverse this pair
            second.next=curr
            curr.next=nxtPair
            prev.next=second

            #update ptrs
            prev=curr
            curr=nxtPair
        
        return dummy.next
    return
        