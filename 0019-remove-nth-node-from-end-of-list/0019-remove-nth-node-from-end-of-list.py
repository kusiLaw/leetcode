# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        cache = {}
        
        current = head
        
        index = 0
        while current:
            index = index + 1
            cache[index] = current
            current = current.next
        
        
        if index - n == 0:
            # node is the head
            return head.next
        else:
            node = cache[index - n ]
            temp = node.next.next
            node.next = temp
            return head 
        
               
        