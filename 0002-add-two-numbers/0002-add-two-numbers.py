# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def reverse_node_list(node):
         # check firt node 
        if node.next is None: # if next is empty retur the val, the default is zero
            return node.val

        head = [node.val]  # keep firts node val in list
        next_node = node.next  # store next node

        while True:     # keep loop 
            if next_node.next != None :
                head.insert(0, next_node.val)  # since it need the reverse order as result
                next_node = next_node.next  # ref next_node for next iteration
            else:
                head.insert(0, next_node.val) # since no next item grap the val
                break
        return ''.join([str(x) for x in head]) # return result str


    
def insertNode(node, tail_node = None): # take two nod an return the tail node
        node.next = tail_node
        return  tail_node

    
    

class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
            # retrieve each node val in inverse order as string
            # convert to itn and add them
            ans = int(reverse_node_list(l1)) + int(reverse_node_list(l2))
            
            
            # create first node from the result
            ans = list(str(ans)[::-1])  # convert ans to str; reverse it;
            head_node = ListNode( ans[0]) 
            
            tail_node = head_node  # head node is also seen as last node
            
            for x in ans[1:]: # loop from index 1
                # each iteration ref new created node, since the new created node become tail node
                tail_node = insertNode(tail_node, ListNode(x)) 
            

            return head_node   # return instance of a node
            



        