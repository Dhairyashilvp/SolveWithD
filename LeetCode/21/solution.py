class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        node = ListNode(0)
        ans = node
        
        while l1 and l2:
            if l1.val <= l2.val:
                ans.next = ListNode(l1.val)
                ans = ans.next
                l1 = l1.next
            elif l2.val <= l1.val:
                ans.next = ListNode(l2.val)
                ans = ans.next
                l2 = l2.next
        if l1 or l2:
            ans.next = l1 or l2
        return node.next