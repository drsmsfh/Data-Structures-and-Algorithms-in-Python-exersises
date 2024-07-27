# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        tmp = head
        listy = []
        while tmp is not None:
            listy.append(tmp.val)
            tmp = tmp.next
        def insertion_sort(my_list):
            for i in range(1, len(my_list)):
                temp = my_list[i]
                j = i-1
                while temp < my_list[j] and j > -1:
                    my_list[j+1] = my_list[j] 
                    my_list[j] = temp
                    j -= 1
            return my_list