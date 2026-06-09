# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
            
        if head.next:
            print(head.next)
            x = self.reverseList(head.next)
            head.next.next = head
            head.next = None
        else:
            print("End", head)
            return head
        return x
        