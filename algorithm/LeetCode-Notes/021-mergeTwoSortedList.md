class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        :type l1:ListNode
        :type l2:ListNode
        :rtype: ListNode
        """
        current=result = ListNode(0)
        
        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next
            
        current.next = l1 or l2
        return result.next
