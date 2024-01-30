# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #optimise using two pointer approach
        
        
        # let begin from None and point every next node to previous and
        # return previous as new had when we meet None again
            
        prev, current = None, head
        
        while current: # reach none and stop loop
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev
            
            
        
        
################################### working ########################################
# 44 ms, faster than 32.50% of Python3 online submissions for Reverse Linked List. #
# 17.7 MB, less than 96.12% of Python3 online submissions for Reverse Linked List. #
####################################################################################

#         if not head or head.next == None:
#             return head
        
#         tail = head # head become  tail
#         current_head = head # assum as tail at step 1
        
        
#         current_node = head.next
#         while current_node != None:
#             # let tail point to the current node next item
#             tail.next = current_node.next
            
#             #let the current node point to current head
#             current_node.next = current_head 
            
#             #let the current node be the head        
#             current_head  = current_node 
                
#             if tail.next == None:
#                 # print(current_node,'\n', '---', tail.next)
#                 return current_head
#             else:
               
#                 current_node = tail.next #where the current nod were suppose to point at
 
#         return  current_head
    