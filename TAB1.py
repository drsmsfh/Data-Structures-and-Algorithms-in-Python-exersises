class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode()
        cus = dummy
        curry = 0
        while l1 or l2 or curry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            val = v1 + v2 + curry
            curry = val // 10
            val = val % 10
            cus.next = ListNode(val)
            cus = cus.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy.next

def create_linked_list(nums):
    dummy = ListNode()
    curr = dummy
    for num in nums:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

def print_linked_list(node):
    nums = []
    while node:
        nums.append(node.val)
        node = node.next
    return nums

# Test cases
test_cases = [
    ([2, 4, 3], [5, 6, 4]), # Expected output: [7, 0, 8]
    ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]), # Expected output: [8, 9, 9, 9, 0, 0, 0, 1]
    ([0], [0]), # Expected output: [0]
    ([9, 9], [1]), # Expected output: [0, 0, 1]
    ([5], [5]) # Expected output: [0, 1]
]

sol = Solution()

for l1_nums, l2_nums in test_cases:
    l1 = create_linked_list(l1_nums)
    l2 = create_linked_list(l2_nums)
    result = sol.addTwoNumbers(l1, l2)
    print(print_linked_list(result))
