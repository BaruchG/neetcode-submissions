# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head1 = list1
        head2 = list2
        dummy = ListNode()
        pointer = dummy

        while head1 and head2:
            print(list1.val)
            print(list2.val)
            if head1.val > head2.val:
                pointer.next = head2
                head2 = head2.next
            elif head1.val < head2.val:
                pointer.next = head1
                head1 = head1.next
            elif head1.val == head2.val:
                pointer.next = head1
                head1 = head1.next
            pointer = pointer.next
        if head1:
            pointer.next = head1
        elif head2:
            pointer.next = head2

        return dummy.next
            