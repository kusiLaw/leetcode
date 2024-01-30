# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if not head or head.next == None:
            return head
        
        tail = head # head become  tail
        current_head = head # assum as tail at step 1
        
        
        current_node = head.next
        while current_node != None:
            # let tail point to the current node next item
            tail.next = current_node.next
            
            #let the current node point to current head
            current_node.next = current_head 
            
            #let the current node be the head        
            current_head  = current_node 
                
            if tail.next == None:
                # print(current_node,'\n', '---', tail.next)
                return current_head
            else:
               
                current_node = tail.next #where the current nod were suppose to point at
 
        return  current_head
    