# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        MeriNode = ListNode(0)
        Jai = Veeru = MeriNode

        MeriNode.next = head
        while Veeru != None and Veeru.next != None:
            Jai = Jai.next
            Veeru = Veeru.next.next

            if Jai == Veeru:
                return True
            
        return False