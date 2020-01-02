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

        Time: O(max(m+n))
        Space: O(max(m+n))
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

    def solution1(self, l1: ListNode, l2: ListNode) -> ListNode:
        """
        Elementary Math

        Time: O(max(m+n))
        Space: O(max(m+n))
        """
        # initialize carry, pointer and dummyHead (used for representing the starting node)
        carry = 0
        pointer = ListNode(None)
        dummy_head = pointer

        while True:
            # retrieve two adders and add them together with the carry from last loop
            add1 = 0 if not l1 else l1.val
            add2 = 0 if not l2 else l2.val
            res_tmp = add1 + add2 + carry

            # if the result is 0, and l1 & l2 reach their end
            if res_tmp == 0 and not l1 and not l2:
                # if [0] + [0], return 0
                if pointer == dummy_head:
                    return ListNode(0)
                else:
                    break

            # check for carry
            if res_tmp >= 10:
                carry = 1
                res_tmp -= 10
            else:
                carry = 0

            # update the result using pointer, and l1 & l2
            pointer.next = ListNode(res_tmp)
            pointer = pointer.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy_head.next


def main():
    # two numbers to add, stored in ListNode
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)

    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)

    solution = Solution()

    # solutions
    # res = solution.addTwoNumbers(l1, l2)
    res = solution.solution1(l1, l2)

    # print the solution
    res_str = str(res.val)
    while res.next:
        res_str += ' -> '
        res_str += str(res.next.val)
        res = res.next
    print(res_str)


if __name__ == '__main__':
    main()
