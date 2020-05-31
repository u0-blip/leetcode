# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head
        if head == None:
            return False
        while fast.next != None and fast.next.next != None:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                current = head
                while current is not slow:
                    current = current.next
                    slow = slow.next
                return slow
        return False

# Runtime: 48 ms, faster than 71.31% of Python3 online submissions for Linked List Cycle.
# Memory Usage: 16.9 MB, less than 100.00% of Python3 online submissions for Linked List Cycle.