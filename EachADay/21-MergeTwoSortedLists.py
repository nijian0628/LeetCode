# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode: 
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        
        root = ListNode(-100) # initialize a ListNode that contains only 1 Node (can contain any value)
        tmp = root
        
        while l1 is not None and l2 is not None:
            if l1.val<=l2.val:
                tmp.next=l1
                l1=l1.next
                tmp=tmp.next
            else:
                tmp.next=l2
                l2=l2.next
                tmp=tmp.next
        
        while l1 is not None:
            tmp.next=l1
            l1=l1.next
            tmp=tmp.next
            
        while l2 is not None:
            tmp.next=l2
            l2=l2.next
            tmp=tmp.next
                   
        return(root.next)