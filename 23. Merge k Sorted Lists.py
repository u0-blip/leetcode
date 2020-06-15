from heapq import *

class ListNode_lt:
    def __lt__(self, other):
        return self.val < other.val
    
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        record = []
        ListNode.__lt__ = ListNode_lt.__lt__
        
        for root in lists:
            if root is not None:
                heappush(record, root)
        
        head = tail = ListNode(0)
        while record:
            tail.next = heappop(record)
            tail = tail.next
            if tail.next:
                heappush(record, tail.next)
        return head.next