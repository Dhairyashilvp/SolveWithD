# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head.next == None:
            return True
        findlen = head
        l = 0
        while findlen:
            findlen = findlen.next
            l += 1
        secondHalf = head
        prev = None
        
        for i in range( l ):
            if i < (l // 2):
                secondHalf = secondHalf.next
            else:
                Next = secondHalf.next
                secondHalf.next = prev
                prev = secondHalf
                secondHalf = Next
        secondHalf = prev
        for _ in range(l//2):
            if head.val != secondHalf.val:
                return False
            else:
                head = head.next
                secondHalf = secondHalf.next
        return True