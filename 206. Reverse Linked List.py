from copy import copy

#iterative
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         if head == None:
#             return head
#         a = ListNode(head.val)
#         a.next = None
#         next = head.next
#         while(next != None):
#             b = ListNode(next.val)
#             b.next = a
#             a = b
#             next = next.next
#         return a
    
#recursive
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return p