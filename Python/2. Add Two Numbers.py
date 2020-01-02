# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    You are given two non-empty linked lists representing two non-negative integers.
    The digits are stored in reverse order and each of their nodes contain a single digit.
    Add the two numbers and return it as a linked list.

    You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    Example:

    Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
    Output: 7 -> 0 -> 8
    Explanation: 342 + 465 = 807.
    """

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Transform ListNode into numbers, and add. Transform back to ListNode.

        """
        # transform input ListNode into two numbers, using string as intermediate data type
        l1_str = str(l1.val)
        l2_str = str(l2.val)
        while l1.next:
            l1 = l1.next
            l1_str = str(l1.val) + l1_str
        while l2.next:
            l2 = l2.next
            l2_str = str(l2.val) + l2_str

        l1_num = int(l1_str)
        l2_num = int(l2_str)
        res_str = str(l1_num + l2_num)

        # transform the result from string to ListNode
        res = ListNode(int(res_str[-1]))
        pointer = res
        for i in reversed(range(len(res_str) - 1)):
            pointer.next = ListNode(int(res_str[i]))
            pointer = pointer.next

        return res


def main():
    # two numbers to add, stored in ListNode
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()

    # my solution
    res = solution.addTwoNumbers(l1, l2)

    res_str = str(res.val)
    while res.next:
        res_str += ' -> '
        res_str += str(res.next.val)
        res = res.next
    print(res_str)


if __name__ == '__main__':
    main()
