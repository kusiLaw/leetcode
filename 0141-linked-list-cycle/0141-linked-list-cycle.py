# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        current_node = head 
        while current_node:
            if hashmap.get(current_node, None):
                return True
            hashmap[current_node] = current_node
            
            current_node = current_node.next
        
        